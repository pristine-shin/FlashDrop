from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .association import likes_posts

class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    postId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('posts.id')), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    user = db.relationship('User', back_populates='likes')
    post = db.relationship('Post', back_populates='likes')

    # __table_args__ = (db.UniqueConstraint('userId', 'postId', name='unique_user_post_like'),)

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'createdAt': self.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': self.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
            # 'posts': [post.to_dict() for post in self.posts]
        }
