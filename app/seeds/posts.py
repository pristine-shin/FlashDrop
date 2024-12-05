from app.models import db, environment, SCHEMA, Post
from sqlalchemy.sql import text

def seed_posts():
    # base_url = 'https://flashdrop-bucket.s3.us-west-1.amazonaws.com'

    posts_data = [
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post1.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-3 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post2.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user1_post3.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post4.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-2 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post5.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user1_post6.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post7.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post8.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user1_post9.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "price": 100.0,
            "size": "1-2 inches",
            "caption": "A beautiful custom design. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user1_post10.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post1.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post2.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user2_post3.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post4.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post5.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user2_post6.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post7.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post8.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user2_post9.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user2_post10.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post1.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post2.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user3_post3.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post4.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post5.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user3_post6.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post7.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post8.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user3_post9.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user3_post10.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post1.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post2.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user4_post3.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post4.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post5.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user4_post6.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post7.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post8.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user4_post9.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user4_post10.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post1.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post2.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user5_post3.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post4.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post5.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user5_post6.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post7.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post8.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user5_post9.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user5_post10.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post1.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post2.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user6_post3.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post4.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post5.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user6_post6.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post7.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post8.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user6_post9.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user6_post10.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post1.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post2.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user7_post3.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post4.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post5.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user7_post6.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post7.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post8.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user7_post9.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user7_post10.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post1.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post2.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user8_post3.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post4.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post5.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user8_post6.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post7.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post8.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user8_post9.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user8_post10.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post1.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post2.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user9_post3.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post4.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post5.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user9_post6.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post7.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post8.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user9_post9.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user9_post10.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post1.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post2.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: American Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user10_post3.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post4.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post5.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: American Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user10_post6.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post7.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post8.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: American Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user10_post9.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user10_post10.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post1.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post2.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Fine Line.",
            "available": False,
            "imageUrl": "https://example.com/images/user11_post3.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post4.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post5.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Fine Line.",
            "available": False,
            "imageUrl": "https://example.com/images/user11_post6.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post7.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post8.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Fine Line.",
            "available": False,
            "imageUrl": "https://example.com/images/user11_post9.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://example.com/images/user11_post10.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post1.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post2.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user12_post3.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post4.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post5.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user12_post6.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post7.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post8.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://example.com/images/user12_post9.jpg"
        },
        {
            "userId": 12,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://example.com/images/user12_post10.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post1.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post2.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user13_post3.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post4.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post5.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user13_post6.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post7.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post8.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://example.com/images/user13_post9.jpg"
        },
        {
            "userId": 13,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://example.com/images/user13_post10.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post1.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post2.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user14_post3.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post4.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post5.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user14_post6.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post7.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post8.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://example.com/images/user14_post9.jpg"
        },
        {
            "userId": 14,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://example.com/images/user14_post10.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post1.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post2.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user15_post3.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post4.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post5.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user15_post6.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post7.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post8.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Realism.",
            "available": False,
            "imageUrl": "https://example.com/images/user15_post9.jpg"
        },
        {
            "userId": 15,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Realism.",
            "available": True,
            "imageUrl": "https://example.com/images/user15_post10.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post1.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post2.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user16_post3.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post4.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post5.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user16_post6.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post7.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post8.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://example.com/images/user16_post9.jpg"
        },
        {
            "userId": 16,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://example.com/images/user16_post10.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post1.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post2.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user17_post3.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post4.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post5.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user17_post6.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post7.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post8.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Geometric.",
            "available": False,
            "imageUrl": "https://example.com/images/user17_post9.jpg"
        },
        {
            "userId": 17,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Geometric.",
            "available": True,
            "imageUrl": "https://example.com/images/user17_post10.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post1.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post2.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user18_post3.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post4.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post5.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user18_post6.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post7.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post8.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Tribal.",
            "available": False,
            "imageUrl": "https://example.com/images/user18_post9.jpg"
        },
        {
            "userId": 18,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Tribal.",
            "available": True,
            "imageUrl": "https://example.com/images/user18_post10.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post1.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post2.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user19_post3.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post4.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post5.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user19_post6.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post7.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post8.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://example.com/images/user19_post9.jpg"
        },
        {
            "userId": 19,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://example.com/images/user19_post10.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post1.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post2.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user20_post3.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post4.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post5.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user20_post6.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post7.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post8.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://example.com/images/user20_post9.jpg"
        },
        {
            "userId": 20,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://example.com/images/user20_post10.jpg"
        }
    ]

    db.session.bulk_insert_mappings(Post, posts_data)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
