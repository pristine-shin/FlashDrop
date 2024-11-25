from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod

# Join table for likes and posts
likes_posts = db.Table(
    'likes_posts',
    db.Column('postId', db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')), primary_key=True),
    db.Column('likeId', db.Integer, db.ForeignKey(add_prefix_for_prod('likes.id')), primary_key=True),
    db.Column('createdAt', db.DateTime, default=datetime.now, nullable=False),
)


if environment == "postion":
    likes_posts.schema = SCHEMA
