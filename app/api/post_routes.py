from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import Post, Comment, db, User
from app.forms import EditPostForm
from app.forms import NewPostForm
from app.forms import NewCommentForm
from app.aws_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3, update_file_on_s3
from sqlalchemy.orm import joinedload


post_routes = Blueprint('posts', __name__)

#Get all posts
@post_routes.route('/')
def all_posts():

  limit = request.args.get('limit', type=int)
  if limit and limit > 0:
    posts = Post.query.options(joinedload(Post.user)).limit(limit).all()
  else:
    posts = Post.query.options(joinedload(Post.user)).all()
  allPosts = {
    "posts": [
      {
        "id": post.id,
        "userId": post.userId,
        "size": post.size,
        "style": post.style,
        "price": round(post.price, 2),
        "caption": post.caption,
        "available": post.available,
        "imageUrl": post.imageUrl,
        "createdAt": post.createdAt,
        "updatedAt": post.updatedAt,
      }
      for post in posts
    ]
  }
  return jsonify(allPosts)

#Get details of a Post by id
@post_routes.route('/<int:postId>')
def post(postId):
  post = Post.query.options(joinedload(Post.user)).get(postId)

  if(post is None):
    return {"message": "Post not found!"}, 404

  PostWithArtist = {
    "id": post.id,
    "userId": post.userId,
    "username": post.user.username,
    "artistBio": post.user.bio,
    "profileImageUrl": post.user.profileImageUrl,
    "size": post.size,
    "style": post.style,
    "price": round(post.price, 2),
    "caption": post.caption,
    "available": post.available,
    "imageUrl": post.imageUrl,
    "createdAt": post.createdAt,
    "updatedAt": post.updatedAt,
  }

  return jsonify(PostWithArtist)

#Get current user posts (NOT yet in API docs)
@post_routes.route('/current')
@login_required
def current_posts():
  user = current_user.to_dict()
  return {"posts": user["posts"]}

#Get posts by userId (NOT yet in API docs)
@post_routes.route('/users/<int:userId>')
@login_required
def user_posts(userId):
  user = User.query.get(userId).to_dict()
  return {"posts": user["posts"]}

# Delete an existing post.
@post_routes.route('/<int:postId>', methods=["DELETE"])
@login_required
def delete_post(postId):
  post = Post.query.get(postId)
  if(post):

    # Retrieve the post's image URL
    image_url = post.imageUrl
    # Delete the image from S3 if it exists
    if image_url:
      remove_file_from_s3(image_url)

    db.session.delete(post)
    db.session.commit()
    return {"message": "Post successfully deleted"}
  else:
    return {"message": "Post not found!"}, 404

# Create a Post
@post_routes.route('/', methods=["POST"])
@login_required
def create_post():
  """
  Creates a new Post
  """
  # Below is for when we have a front end form we are getting data from
  form = NewPostForm()

  form["csrf_token"].data = request.cookies.get("csrf_token")

  if form.validate_on_submit():

    image = form.imageUrl.data
    image.filename = get_unique_filename(image.filename)
    upload = upload_file_to_s3(image)

    if "url" not in upload:
      return {"error": upload["errors"]}, 400

    url = upload["url"]

    newPost = Post(
      userId=current_user.id,
      size=form.size.data,
      style=form.style.data,
      price=form.price.data,
      caption=form.caption.data,
      available=form.available.data,
      imageUrl=url
    )

    db.session.add(newPost)
    db.session.commit()
    return newPost.to_dict(), 201

  if form.errors:
    return form.errors, 400

  # this is for testing only, switch back to code above once frontend form exists
  # data = request.get_json()
  # newPost = Post(
  #   userId=current_user.id,
  #   size=data['size'],
  #   style=data['style'],
  #   price=data['price'],
  #   caption=data['caption'],
  #   available=data['available'],
  #   imageUrl=data['imageUrl'])
  # db.session.add(newPost)
  # db.session.commit()
  # return newPost.to_dict(), 201

# Update and Return existing Post
@post_routes.route('edit/<int:postId>', methods=["PUT"])
@login_required
def update_post(postId):
  """
  Update a User's post
  """
  # Below is for when we have a front end form we are getting data from
  post = Post.query.get(postId)

  if post is None:
    return {'message': 'Post could not be found!'}, 404

  if(post.get_userId != current_user.id):
    return {'message': 'Requires proper authorization!'}, 403

  form = EditPostForm()
  form['csrf_token'].data = request.cookies['csrf_token']

  if form.validate_on_submit():
    # post.userId = current_user.id, not sure if i need this
    post.size=form.size.data,
    post.style=form.style.data,
    post.price=form.price.data,
    post.caption=form.caption.data,
    post.available=form.available.data,

    if form.imageUrl.data:
      new_image = form.imageUrl.data
      new_image.filename = get_unique_filename(new_image.filename)

      old_image_url = post.imageUrl
      upload = update_file_on_s3(new_image, old_image_url=old_image_url)

      if "url" not in upload:
        return {"errors": upload["errors"]}, 400

      post.imageUrl = upload["url"]

    db.session.commit()

    updated_post = {
      "id": post.id,
      "userId": post.userId,
      "size": post.size,
      "style": post.style,
      "price": round(post.price, 2),
      "caption": post.caption,
      "available": post.available,
      "imageUrl": post.imageUrl,
      "createdAt": post.createdAt,
      "updatedAt": post.updatedAt,
    }

    return updated_post, 200
    # return {"message": "Post updated successfully.", "post": updated_post.to_dict()}, 200

  if form.errors:
    return form.errors, 400

  #just in case in other errors
  return {"errors": "Invalid requests"}, 400

  # post = Post.query.get(postId)
  # data = request.get_json()
  # if(post):
  #   if(post.get_userId != current_user.id):
  #     return {'message': 'Requires proper authorization!'}, 403
  #   if "size" in data:
  #     post.size = data["size"]
  #   if "style" in data:
  #     post.style = data["style"]
  #   if "price" in data:
  #     post.price = data["price"]
  #   if "caption" in data:
  #     post.caption = data["caption"]
  #   if "available" in data:
  #     post.available = data["available"]
  #   if "imageUrl" in data:
  #     post.imageUrl = data["imageUrl"]
  #   try:
  #     db.session.commit()
  #     return {'post': post.to_dict()}
  #   except Exception as e:
  #     db.session.rollback()
  #     return {'message': 'Error updating Post', 'error': str(e)}, 400
  # else:
  #   return {'message': 'Post could not be found!'}, 404


# COMMENTS Get all comments by post's id
@post_routes.route('/<int:postId>/comments')
def post_comments(postId):
  # Load post with comments and user data in a single query
  post = Post.query.options(
      joinedload(Post.comments).joinedload(Comment.user)
  ).filter_by(id=postId).first()

  if not post:
      return {'message': 'Post could not be found!'}, 404

  post_comments = [
      {
          **comment.to_dict(),
          "artistName": comment.user.artistName,
          "profileImageUrl": comment.user.profileImageUrl
      }
      for comment in post.comments
  ]

  return jsonify({"comments": post_comments})

# COMMENTS Create and return a comment for a post by id
  """
  add validations:
    user cant comment their own posts
    user can only leave ONE comment per post
  """
@post_routes.route('/<int:postId>/comments', methods=["POST"])
@login_required
def create_comment(postId):

  post = Post.query.get(postId)
  if post is None:
    return {'message': 'Post could not be found!'}, 404
  form = NewCommentForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    newComment = Comment(
      userId = current_user.id,
      comment = form.comment.data,
      postId = postId,
    )
    db.session.add(newComment)
    db.session.commit()
    return {"comment": newComment.to_dict()}
  if form.errors:
    return form.errors, 400
