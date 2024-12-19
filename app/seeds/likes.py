from app.models import db, environment, SCHEMA, Like, Post, User
from sqlalchemy.sql import text
import random

def seed_likes():
    # Fetch all users and posts
    users = User.query.all()
    posts = Post.query.all()

    if not users or not posts:
        print("No users or posts available to seed likes.")
        return

    likes = []
    # Generate 50 random likes
    for _ in range(50):
        user = random.choice(users)
        post = random.choice(posts)

        # Ensure the like is unique
        if not Like.query.filter_by(userId=user.id, postId=post.id).first():
            like = Like(userId=user.id, postId=post.id)
            likes.append(like)

    # Bulk insert likes
    db.session.bulk_save_objects(likes)
    db.session.commit()
    print(f"Seeded {len(likes)} likes.")

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.likes RESTART IDENTITY CASCADE;")
    else:
        # Delete all rows and reset the primary key sequence in development
        db.session.execute(text("DELETE FROM likes"))
        # db.session.execute(text("ALTER SEQUENCE likes_id_seq RESTART WITH 1;"))
    db.session.commit()
