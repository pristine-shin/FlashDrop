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
        {'userId': 12},
        {'userId': 13},
        {'userId': 14},
        {'userId': 15},
        {'userId': 16},
        {'userId': 17},
        {'userId': 18},
        {'userId': 19},
        {'userId': 20},
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
        "likeId": 12,
        "postId": 12
      },
      {
        "likeId": 13,
        "postId": 13
      },
      {
        "likeId": 14,
        "postId": 14
      },
      {
        "likeId": 15,
        "postId": 15
      },
      {
        "likeId": 16,
        "postId": 16
      },
      {
        "likeId": 17,
        "postId": 17
      },
      {
        "likeId": 18,
        "postId": 18
      },
      {
        "likeId": 19,
        "postId": 19
      },
      {
        "likeId": 20,
        "postId": 20
      },
      {
        "likeId": 1,
        "postId": 21
      },
      {
        "likeId": 2,
        "postId": 22
      },
      {
        "likeId": 3,
        "postId": 23
      },
      {
        "likeId": 4,
        "postId": 24
      },
      {
        "likeId": 5,
        "postId": 25
      },
      {
        "likeId": 6,
        "postId": 26
      },
      {
        "likeId": 7,
        "postId": 27
      },
      {
        "likeId": 8,
        "postId": 28
      },
      {
        "likeId": 9,
        "postId": 29
      },
      {
        "likeId": 10,
        "postId": 30
      },
      {
        "likeId": 11,
        "postId": 31
      },
      {
        "likeId": 12,
        "postId": 32
      },
      {
        "likeId": 13,
        "postId": 33
      },
      {
        "likeId": 14,
        "postId": 34
      },
      {
        "likeId": 15,
        "postId": 35
      },
      {
        "likeId": 16,
        "postId": 36
      },
      {
        "likeId": 17,
        "postId": 37
      },
      {
        "likeId": 18,
        "postId": 38
      },
      {
        "likeId": 19,
        "postId": 39
      },
      {
        "likeId": 20,
        "postId": 40
      },
      {
        "likeId": 1,
        "postId": 41
      },
      {
        "likeId": 2,
        "postId": 42
      },
      {
        "likeId": 3,
        "postId": 43
      },
      {
        "likeId": 4,
        "postId": 44
      },
      {
        "likeId": 5,
        "postId": 45
      },
      {
        "likeId": 6,
        "postId": 46
      },
      {
        "likeId": 7,
        "postId": 47
      },
      {
        "likeId": 8,
        "postId": 48
      },
      {
        "likeId": 9,
        "postId": 49
      },
      {
        "likeId": 10,
        "postId": 50
      },
      {
        "likeId": 11,
        "postId": 51
      },
      {
        "likeId": 12,
        "postId": 52
      },
      {
        "likeId": 13,
        "postId": 53
      },
      {
        "likeId": 14,
        "postId": 54
      },
      {
        "likeId": 15,
        "postId": 55
      },
      {
        "likeId": 16,
        "postId": 56
      },
      {
        "likeId": 17,
        "postId": 57
      },
      {
        "likeId": 18,
        "postId": 58
      },
      {
        "likeId": 19,
        "postId": 59
      },
      {
        "likeId": 20,
        "postId": 60
      },
      {
        "likeId": 1,
        "postId": 61
      },
      {
        "likeId": 2,
        "postId": 62
      },
      {
        "likeId": 3,
        "postId": 63
      },
      {
        "likeId": 4,
        "postId": 64
      },
      {
        "likeId": 5,
        "postId": 65
      },
      {
        "likeId": 6,
        "postId": 66
      },
      {
        "likeId": 7,
        "postId": 67
      },
      {
        "likeId": 8,
        "postId": 68
      },
      {
        "likeId": 9,
        "postId": 69
      },
      {
        "likeId": 10,
        "postId": 70
      },
      {
        "likeId": 11,
        "postId": 71
      },
      {
        "likeId": 12,
        "postId": 72
      },
      {
        "likeId": 13,
        "postId": 73
      },
      {
        "likeId": 14,
        "postId": 74
      },
      {
        "likeId": 15,
        "postId": 75
      },
      {
        "likeId": 16,
        "postId": 76
      },
      {
        "likeId": 17,
        "postId": 77
      },
      {
        "likeId": 18,
        "postId": 78
      },
      {
        "likeId": 19,
        "postId": 79
      },
      {
        "likeId": 20,
        "postId": 80
      },
      {
        "likeId": 1,
        "postId": 81
      },
      {
        "likeId": 2,
        "postId": 82
      },
      {
        "likeId": 3,
        "postId": 83
      },
      {
        "likeId": 4,
        "postId": 84
      },
      {
        "likeId": 5,
        "postId": 85
      },
      {
        "likeId": 6,
        "postId": 86
      },
      {
        "likeId": 7,
        "postId": 87
      },
      {
        "likeId": 8,
        "postId": 88
      },
      {
        "likeId": 9,
        "postId": 89
      },
      {
        "likeId": 10,
        "postId": 90
      },
      {
        "likeId": 11,
        "postId": 91
      },
      {
        "likeId": 12,
        "postId": 92
      },
      {
        "likeId": 13,
        "postId": 93
      },
      {
        "likeId": 14,
        "postId": 94
      },
      {
        "likeId": 15,
        "postId": 95
      },
      {
        "likeId": 16,
        "postId": 96
      },
      {
        "likeId": 17,
        "postId": 97
      },
      {
        "likeId": 18,
        "postId": 98
      },
      {
        "likeId": 19,
        "postId": 99
      },
      {
        "likeId": 20,
        "postId": 100
      },
      {
        "likeId": 1,
        "postId": 101
      },
      {
        "likeId": 2,
        "postId": 102
      },
      {
        "likeId": 3,
        "postId": 103
      },
      {
        "likeId": 4,
        "postId": 104
      },
      {
        "likeId": 5,
        "postId": 105
      },
      {
        "likeId": 6,
        "postId": 106
      },
      {
        "likeId": 7,
        "postId": 107
      },
      {
        "likeId": 8,
        "postId": 108
      },
      {
        "likeId": 9,
        "postId": 109
      },
      {
        "likeId": 10,
        "postId": 110
      },
      {
        "likeId": 11,
        "postId": 111
      },
      {
        "likeId": 12,
        "postId": 112
      },
      {
        "likeId": 13,
        "postId": 113
      },
      {
        "likeId": 14,
        "postId": 114
      },
      {
        "likeId": 15,
        "postId": 115
      },
      {
        "likeId": 16,
        "postId": 116
      },
      {
        "likeId": 17,
        "postId": 117
      },
      {
        "likeId": 18,
        "postId": 118
      },
      {
        "likeId": 19,
        "postId": 119
      },
      {
        "likeId": 20,
        "postId": 120
      },
      {
        "likeId": 1,
        "postId": 121
      },
      {
        "likeId": 2,
        "postId": 122
      },
      {
        "likeId": 3,
        "postId": 123
      },
      {
        "likeId": 4,
        "postId": 124
      },
      {
        "likeId": 5,
        "postId": 125
      },
      {
        "likeId": 6,
        "postId": 126
      },
      {
        "likeId": 7,
        "postId": 127
      },
      {
        "likeId": 8,
        "postId": 128
      },
      {
        "likeId": 9,
        "postId": 129
      },
      {
        "likeId": 10,
        "postId": 130
      },
      {
        "likeId": 11,
        "postId": 131
      },
      {
        "likeId": 12,
        "postId": 132
      },
      {
        "likeId": 13,
        "postId": 133
      },
      {
        "likeId": 14,
        "postId": 134
      },
      {
        "likeId": 15,
        "postId": 135
      },
      {
        "likeId": 16,
        "postId": 136
      },
      {
        "likeId": 17,
        "postId": 137
      },
      {
        "likeId": 18,
        "postId": 138
      },
      {
        "likeId": 19,
        "postId": 139
      },
      {
        "likeId": 20,
        "postId": 140
      },
      {
        "likeId": 1,
        "postId": 141
      },
      {
        "likeId": 2,
        "postId": 142
      },
      {
        "likeId": 3,
        "postId": 143
      },
      {
        "likeId": 4,
        "postId": 144
      },
      {
        "likeId": 5,
        "postId": 145
      },
      {
        "likeId": 6,
        "postId": 146
      },
      {
        "likeId": 7,
        "postId": 147
      },
      {
        "likeId": 8,
        "postId": 148
      },
      {
        "likeId": 9,
        "postId": 149
      },
      {
        "likeId": 10,
        "postId": 150
      },
      {
        "likeId": 11,
        "postId": 151
      },
      {
        "likeId": 12,
        "postId": 152
      },
      {
        "likeId": 13,
        "postId": 153
      },
      {
        "likeId": 14,
        "postId": 154
      },
      {
        "likeId": 15,
        "postId": 155
      },
      {
        "likeId": 16,
        "postId": 156
      },
      {
        "likeId": 17,
        "postId": 157
      },
      {
        "likeId": 18,
        "postId": 158
      },
      {
        "likeId": 19,
        "postId": 159
      },
      {
        "likeId": 20,
        "postId": 160
      },
      {
        "likeId": 1,
        "postId": 161
      },
      {
        "likeId": 2,
        "postId": 162
      },
      {
        "likeId": 3,
        "postId": 163
      },
      {
        "likeId": 4,
        "postId": 164
      },
      {
        "likeId": 5,
        "postId": 165
      },
      {
        "likeId": 6,
        "postId": 166
      },
      {
        "likeId": 7,
        "postId": 167
      },
      {
        "likeId": 8,
        "postId": 168
      },
      {
        "likeId": 9,
        "postId": 169
      },
      {
        "likeId": 10,
        "postId": 170
      },
      {
        "likeId": 11,
        "postId": 171
      },
      {
        "likeId": 12,
        "postId": 172
      },
      {
        "likeId": 13,
        "postId": 173
      },
      {
        "likeId": 14,
        "postId": 174
      },
      {
        "likeId": 15,
        "postId": 175
      },
      {
        "likeId": 16,
        "postId": 176
      },
      {
        "likeId": 17,
        "postId": 177
      },
      {
        "likeId": 18,
        "postId": 178
      },
      {
        "likeId": 19,
        "postId": 179
      },
      {
        "likeId": 20,
        "postId": 180
      },
      {
        "likeId": 1,
        "postId": 181
      },
      {
        "likeId": 2,
        "postId": 182
      },
      {
        "likeId": 3,
        "postId": 183
      },
      {
        "likeId": 4,
        "postId": 184
      },
      {
        "likeId": 5,
        "postId": 185
      },
      {
        "likeId": 6,
        "postId": 186
      },
      {
        "likeId": 7,
        "postId": 187
      },
      {
        "likeId": 8,
        "postId": 188
      },
      {
        "likeId": 9,
        "postId": 189
      },
      {
        "likeId": 10,
        "postId": 190
      },
      {
        "likeId": 11,
        "postId": 191
      },
      {
        "likeId": 12,
        "postId": 192
      },
      {
        "likeId": 13,
        "postId": 193
      },
      {
        "likeId": 14,
        "postId": 194
      },
      {
        "likeId": 15,
        "postId": 195
      },
      {
        "likeId": 16,
        "postId": 196
      },
      {
        "likeId": 17,
        "postId": 197
      },
      {
        "likeId": 18,
        "postId": 198
      },
      {
        "likeId": 19,
        "postId": 199
      },
      {
        "likeId": 20,
        "postId": 200
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
