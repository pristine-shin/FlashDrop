from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    base_url = 'https://flashdrop-bucket.s3.us-west-1.amazonaws.com'

    users_data = [
        {
            "email": "inkedbyalex@gmail.com",
            "username": "inked_by_alex",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/inked_by_alex.jpg",
            "bio": "Bay Area. Black and gray realism. DM for bookings."
        },
        {
            "email": "tattoosbyemma@gmail.com",
            "username": "tattoosbyemma",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/tattoosbyemma.jpg",
            "bio": "Fine line & floral specialist 🌸 SF based."
        },
        {
            "email": "linesbyleo@gmail.com",
            "username": "lines_by_leo",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/lines_by_leo.jpg",
            "bio": "Minimalist designs & geometric art 🔺 Oakland studio."
        },
        {
            "email": "artbyella@gmail.com",
            "username": "art_by_ella",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/art_by_ella.jpg",
            "bio": "Nature-inspired tattoos 🌿 SF & Oakland. Booking for 2024!"
        },
        {
            "email": "bayareaink@gmail.com",
            "username": "bay_area_ink",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/bay_area_ink.jpg",
            "bio": "Custom designs & bold colors 🎨 Book now."
        },
        {
            "email": "vividbyvera@gmail.com",
            "username": "vivid_by_vera",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/vivid_by_vera.jpg",
            "bio": "Vivid watercolor & abstract pieces 💧 SF & Berkeley."
        },
        {
            "email": "boldlinesbrian@gmail.com",
            "username": "bold_lines_brian",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/bold_lines_brian.jpg",
            "bio": "Traditional tattoos with a modern twist ✨ DM to book."
        },
        {
            "email": "flowertatts@gmail.com",
            "username": "flower_tatts",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/flower_tatts.jpg",
            "bio": "Floral & nature tattoos 🌼 Oakland. Appointments available."
        },
        {
            "email": "inkbychris@gmail.com",
            "username": "ink_by_chris",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/ink_by_chris.jpg",
            "bio": "Bold and vibrant. Oakland-based artist. Walk-ins welcome!"
        },
        {
            "email": "finelinesf@gmail.com",
            "username": "fine_line_sf",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/fine_line_sf.jpg",
            "bio": "Specializing in intricate fine line tattoos ✏️ SF Bay Area."
        },
        {
            "email": "geotatts@gmail.com",
            "username": "geo_tatts",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/geo_tatts.jpg",
            "bio": "Geometric & abstract designs 📐 Available in SF."
        },
        {
            "email": "artandink@gmail.com",
            "username": "art_and_ink",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/art_and_ink.jpg",
            "bio": "Bay Area artist. Whimsical, hand-drawn vibes. 💫"
        },
        {
            "email": "oaklandtattoos@gmail.com",
            "username": "oakland_tattoos",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/oakland_tattoos.jpg",
            "bio": "Blackwork & stippling specialist. 🌑 Oakland studio."
        },
        {
            "email": "fusiontatts@gmail.com",
            "username": "fusion_tatts",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/fusion_tatts.jpg",
            "bio": "Fusion of traditional & modern styles. 🎭 Open for bookings."
        },
        {
            "email": "smalltattoos@gmail.com",
            "username": "small_tattoos",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/small_tattoos.jpg",
            "bio": "Tiny, detailed tattoos ✨ Oakland."
        },
        {
            "email": "inkbayarea@gmail.com",
            "username": "ink_bay_area",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/ink_bay_area.jpg",
            "bio": "Inspired by the Bay 🌉 Oakland/SF."
        },
        {
            "email": "tattoobylee@gmail.com",
            "username": "tattoo_by_lee",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/tattoo_by_lee.jpg",
            "bio": "Custom designs, modern aesthetics. 🖤 Bay Area."
        },
        {
            "email": "inkedandwild@gmail.com",
            "username": "inked_and_wild",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/inked_and_wild.jpg",
            "bio": "Wild & freehand designs 🐾 Oakland tattoo studio."
        },
        {
            "email": "goldenstatetattoo@gmail.com",
            "username": "golden_state_tattoo",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/golden_state_tattoo.jpg",
            "bio": "Golden State-inspired tattoos 🌞 SF Bay Area."
        },
        {
            "email": "skinstories@gmail.com",
            "username": "skin_stories",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/skin_stories.jpg",
            "bio": "Telling stories through ink. 💌 SF/Oakland."
        },
        {
            "email": "swoopingswallow@gmail.com",
            "username": "swooping_swallow",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/swooping_swallow.jpg",
            "bio": "West Oakland since 1989. DM for sliding scale."
        },
        {
            "email": "pricklypeartatts@gmail.com",
            "username": "prickly_pear_tatts",
            "hashed_password": "hashedpassword123",
            "is_artist": True,
            "profileImageUrl": f"{base_url}/prickly_pear_tatts.jpg",
            "bio": "Specialize in free hand collaborative design. 💌 SF/Oakland."
        },
    ]

    #bulk_insert_mappings do not let our passsword hashing happen because it bypasses the model instantiation. Our @password.setter needs to happen on each user.
    users = [User(**data) for data in users_data]
    db.session.add_all(users)
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
