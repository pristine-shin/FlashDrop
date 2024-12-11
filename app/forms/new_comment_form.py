from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Comment


class NewCommentForm(FlaskForm):
  content = StringField('content', validators=[DataRequired(message='Please enter a comment for this post.')])
