from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Like, db, Post, likes_posts

like_routes = Blueprint('likes', __name__)

#View likes
@like_routes.route('/session') #test if this works without/session later
@login_required
def view_likes():
  likes = current_user.likes

  result =[]

  for post in likes.posts:
    like_post = db.session.query(likes_posts).filter_by(likeId=like_post.id, postId=post.id).first()

    if like_post:
      result.append({
        "postId": post.id,
        "userId": post.userId,
        "size": post.size,
        "style": post.style,
        "price": round(post.price, 2),
        "caption": post.caption,
        "available": post.available,
        "imageUrl": post.imageUrl,
        # "username": post.user.username,
        "createdAt": post.createdAt,
        "updatedAt": post.updatedAt,
    })

  return {'likes': result}


#Add a post to likes page and add a like to a post
@like_routes.route('/session', methods=["POST"])
@login_required
def add_to_likes():
  data = request.get_json()
  post_id = data.get('postId')
  post = Post.query.get(post_id)
  if post:
    like_post = db.session.query(likes_posts).filter_by(
      likeId=current_user.like.id,
      postId=post_id
    ).first()

    if like_post:
      return {"message": "Post is already liked"}, 400
    else:
      db.session.execute(
        likes_posts.insert().values(likeId=current_user.like.id, postId=post_id)
      )
      db.session.commit()

      like = current_user.to_dict()["likes"]
      result =[]

      for post in like["posts"]:
        dict_post = {
          "postId": post["postId"],
          "userId": post["userId"],
          "size": post["size"],
          "style": post["style"],
          "price": post["price"],
          "caption": post["caption"],
          "available": post["available"],
          "imageUrl": post["imageUrl"],
          "createdAt": post["createdAt"],
          "updatedAt": post["updatedAt"],
        }
        result.append(dict_post)

      return {
        "message": "Post added to the like",
        'like': result
      }
  else:
    return {"message": "Post not found"}, 404

#Remove a post from likes page and remove a like from a post
@like_routes.route('/<int:postId>', methods=["DELETE"])
@login_required
def delete_like_post(postId):
  post = Post.query.get(postId)

  if post:
    like_post = db.session.query(likes_posts).filter_by(
      likeId=current_user.like.id,
      postId=postId
    ).first()

    if like_post:
      db.session.execute(
        likes_posts.delete().where(
          likes_posts.c.likeId == current_user.like.id,
          likes_posts.c.postId == postId
        )
      )

      db.session.commit()
      return {"message": "Post removed from the like"}
    else:
      return {"message": "Post not found in like"}, 404
  else:
    return {"message": "Post not found"}, 404
