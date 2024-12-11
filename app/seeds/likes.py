from app.models import db, environment, SCHEMA, Like, likes_posts
from sqlalchemy.sql import text

def seed_likes():
    likes_data = [
        {'userId': 1},
        {'userId': 2},
        {'userId': 3},
        {'userId': 4},
        {'userId': 5},
        {'userId': 6},
        {'userId': 7},
        {'userId': 8},
        {'userId': 9},
        {'userId': 10},
        {'userId': 11},
        # {'userId': 12},
        # {'userId': 13},
        # {'userId': 14},
        # {'userId': 15},
        # {'userId': 16},
        # {'userId': 17},
        # {'userId': 18},
        # {'userId': 19},
        # {'userId': 20},
    ]


    db.session.bulk_insert_mappings(Like, likes_data)
    db.session.commit()

    # Create associations between likes and posts
    like_post_data = [
      {
        "likeId": 1,
        "postId": 1
      },
      {
          "likeId": 2,
          "postId": 2
      },
      {
          "likeId": 3,
          "postId": 3
      },
      {
          "likeId": 4,
          "postId": 4
      },
      {
          "likeId": 5,
          "postId": 5
      },
      {
          "likeId": 6,
          "postId": 6
      },
      {
          "likeId": 7,
          "postId": 7
      },
      {
          "likeId": 8,
          "postId": 8
      },
      {
          "likeId": 9,
          "postId": 9
      },
      {
          "likeId": 10,
          "postId": 10
      },
      {
          "likeId": 11,
          "postId": 11
      },
      {
          "likeId": 1,
          "postId": 12
      },
      {
          "likeId": 2,
          "postId": 13
      },
      {
          "likeId": 3,
          "postId": 14
      },
      {
          "likeId": 4,
          "postId": 15
      },
      {
          "likeId": 5,
          "postId": 16
      },
      {
          "likeId": 6,
          "postId": 17
      },
      {
          "likeId": 7,
          "postId": 18
      },
      {
          "likeId": 8,
          "postId": 19
      },
      {
          "likeId": 9,
          "postId": 20
      },
      {
          "likeId": 10,
          "postId": 21
      },
      {
          "likeId": 11,
          "postId": 22
      },
      {
          "likeId": 1,
          "postId": 23
      },
      {
          "likeId": 2,
          "postId": 24
      },
      {
          "likeId": 3,
          "postId": 25
      },
      {
          "likeId": 4,
          "postId": 26
      },
      {
          "likeId": 5,
          "postId": 27
      },
      {
          "likeId": 6,
          "postId": 28
      },
      {
          "likeId": 7,
          "postId": 29
      },
      {
          "likeId": 8,
          "postId": 30
      },
      {
          "likeId": 9,
          "postId": 31
      },
      {
          "likeId": 10,
          "postId": 32
      },
      {
          "likeId": 11,
          "postId": 33
      },
      {
          "likeId": 1,
          "postId": 34
      },
      {
          "likeId": 2,
          "postId": 35
      },
      {
          "likeId": 3,
          "postId": 36
      },
      {
          "likeId": 4,
          "postId": 37
      },
      {
          "likeId": 5,
          "postId": 38
      },
      {
          "likeId": 6,
          "postId": 39
      },
      {
          "likeId": 7,
          "postId": 40
      },
      {
          "likeId": 8,
          "postId": 41
      },
      {
          "likeId": 9,
          "postId": 42
      },
      {
          "likeId": 10,
          "postId": 43
      },
      {
          "likeId": 11,
          "postId": 44
      },
      {
          "likeId": 1,
          "postId": 45
      },
      {
          "likeId": 2,
          "postId": 46
      },
      {
          "likeId": 3,
          "postId": 47
      },
      {
          "likeId": 4,
          "postId": 48
      },
      {
          "likeId": 5,
          "postId": 49
      },
      {
          "likeId": 6,
          "postId": 50
      },
      {
          "likeId": 7,
          "postId": 51
      },
      {
          "likeId": 8,
          "postId": 52
      },
      {
          "likeId": 9,
          "postId": 53
      },
      {
          "likeId": 10,
          "postId": 54
      },
      {
          "likeId": 11,
          "postId": 55
      },
      {
          "likeId": 1,
          "postId": 56
      },
      {
          "likeId": 2,
          "postId": 57
      },
      {
          "likeId": 3,
          "postId": 58
      },
      {
          "likeId": 4,
          "postId": 59
      },
      {
          "likeId": 5,
          "postId": 60
      },
      {
          "likeId": 6,
          "postId": 61
      },
      {
          "likeId": 7,
          "postId": 62
      },
      {
          "likeId": 8,
          "postId": 63
      },
      {
          "likeId": 9,
          "postId": 64
      },
      {
          "likeId": 10,
          "postId": 65
      },
      {
          "likeId": 11,
          "postId": 66
      },
      {
          "likeId": 1,
          "postId": 67
      },
      {
          "likeId": 2,
          "postId": 68
      },
      {
          "likeId": 3,
          "postId": 69
      },
      {
          "likeId": 4,
          "postId": 70
      },
      {
          "likeId": 5,
          "postId": 71
      },
      {
          "likeId": 6,
          "postId": 72
      },
      {
          "likeId": 7,
          "postId": 73
      },
      {
          "likeId": 8,
          "postId": 74
      },
      {
          "likeId": 9,
          "postId": 75
      },
      {
          "likeId": 10,
          "postId": 76
      },
      {
          "likeId": 11,
          "postId": 77
      },
      {
          "likeId": 1,
          "postId": 78
      },
      {
          "likeId": 2,
          "postId": 79
      },
      {
          "likeId": 3,
          "postId": 80
      },
      {
          "likeId": 4,
          "postId": 81
      },
      {
          "likeId": 5,
          "postId": 82
      },
      {
          "likeId": 6,
          "postId": 83
      },
      {
          "likeId": 7,
          "postId": 84
      },
      {
          "likeId": 8,
          "postId": 85
      },
      {
          "likeId": 9,
          "postId": 86
      },
      {
          "likeId": 10,
          "postId": 87
      },
      {
          "likeId": 11,
          "postId": 88
      },
      {
          "likeId": 1,
          "postId": 89
      },
      {
          "likeId": 2,
          "postId": 90
      },
      {
          "likeId": 3,
          "postId": 91
      },
      {
          "likeId": 4,
          "postId": 92
      },
      {
          "likeId": 5,
          "postId": 93
      },
      {
          "likeId": 6,
          "postId": 94
      },
      {
          "likeId": 7,
          "postId": 95
      },
      {
          "likeId": 8,
          "postId": 96
      },
      {
          "likeId": 9,
          "postId": 97
      },
      {
          "likeId": 10,
          "postId": 98
      },
      {
          "likeId": 11,
          "postId": 99
      },
      {
          "likeId": 1,
          "postId": 100
      },
      {
          "likeId": 2,
          "postId": 101
      },
      {
          "likeId": 3,
          "postId": 102
      },
      {
          "likeId": 4,
          "postId": 103
      },
      {
          "likeId": 5,
          "postId": 104
      },
      {
          "likeId": 6,
          "postId": 105
      },
      {
          "likeId": 7,
          "postId": 106
      },
      {
          "likeId": 8,
          "postId": 107
      },
      {
          "likeId": 9,
          "postId": 108
      },
      {
          "likeId": 10,
          "postId": 109
      },
      {
          "likeId": 11,
          "postId": 110
      }
  ]

    # Insert each association individually
    for association in like_post_data:
        db.session.execute(
            likes_posts.insert().values(**association)
        )
    db.session.commit()

def undo_likes():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.likes RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.likes_posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM likes"))
        db.session.execute(text("DELETE FROM likes_posts"))

    db.session.commit()
