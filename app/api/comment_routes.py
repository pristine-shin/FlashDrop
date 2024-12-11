from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Comment, db
from app.forms import EditCommentForm

comment_routes = Blueprint('comments', __name__)

# Update and return an existing comment
@comment_routes.route('/<int:commentId>', methods=['PUT'])
@login_required
def edit_comment(commentId):
  comment = Comment.query.get(commentId)
  if comment is None:
    return {'message': 'Comment could not be found!'}, 404
  if(comment.get_userId != current_user.id):
    return {'message': 'Requires proper authorization!'}, 403

  form = EditCommentForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    comment.content = form.content.data
  if(form.errors):
    return form.errors, 400
  try:
    db.session.commit()
    return {'comment': comment.to_dict()}
  except Exception as e:
    db.session.rollback()
    return {'message': 'Error updating Product', 'error': str(e)}, 400

# Delete an existing comment
@comment_routes.route('/<int:commentId>', methods=['DELETE'])
@login_required
def delete_comment(commentId):
  comment = Comment.query.get(commentId)
  if comment is None:
    return {'message': 'Comment could not be found!'}, 404
  if(comment.get_userId != current_user.id):
      return {'message': 'Requires proper authorization!'}, 403
  if(comment):
    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment successfully deleted"}

# Get current User's comments (not yet in API docs, also might not need this)
@comment_routes.route('/current')
@login_required
def user_comments():
  user = current_user.to_dict()
  return user["comments"]
