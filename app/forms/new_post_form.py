from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, DecimalField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange, URL
from app.models import Post
from app.aws_helpers import ALLOWED_EXTENSIONS


class NewPostForm(FlaskForm):
  size = StringField('size', validators=[DataRequired(message='Please enter a size.')])
  style = StringField('style', validators=[DataRequired(message='Please enter a style.')])
  price = DecimalField('price', validators=[DataRequired(message="Please enter a price."), NumberRange(min=0.01, message='Price must be a positive number!')])
  caption = StringField('caption', validators=[DataRequired(message="Please provide a caption for this post.")])
  available = BooleanField('available', validators=[DataRequired()])
  # imageUrl = URLField('imageUrl', validators=[DataRequired(message="Please provide an image of this item."), URL()])
  imageUrl = FileField('imageUrl', validators=[FileRequired(message="Please provide an image."), FileAllowed(list(ALLOWED_EXTENSIONS))])
