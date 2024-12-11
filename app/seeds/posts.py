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
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432011/IMG_5325_1800x_tvythx.jpg",
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-3 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432011/ue65cutsdr051_ue4r4i.jpg",
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432011/tattoo-smart-flash-stamps-japanese-vol-4-32721303961783_jyqole.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432012/il_570xN.5546534375_pnqq_l8hh0m.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-2 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432012/japanese-tattoos-set_fht9qe.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432012/3nltk2mn1cmb1_okc5gr.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432013/2921235542_f1d860b3b3_z_zffzyj.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432013/tattoo-smart-flash-stamps-japanese-vol-2-29864566161591_3700x_pvallv.png"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "size": "2-3 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Traditional Japanese.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432014/image-asset_yfpft1.jpg"
        },
        {
            "userId": 1,
            "style": "Traditional Japanese",
            "price": 100.0,
            "size": "1-2 inches",
            "caption": "A beautiful custom design. Style: Traditional Japanese.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432014/swqrikss9q4c1_ykvmpq.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432150/8dh3nyhoseub1_a6uliy.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432150/silly-question-for-a-silly-goose-would-this-be-considered-v0-2n904a06syeb1_efhvvc.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432151/neo-traditional-raven-done-by-jjclaudio-at-blacksail-studios-v0-rjuoqldlcg8c1_mked4e.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432151/DALL_C2_B7E_2023-11-22_14.15.22_-_A_photorealistic_image_of_a_neo-traditional_bird_tattoo_design_2C_suitable_for_placement_on_the_chest._The_bird_is_depicted_in_mid-flight_with_its_wings_jhqrvi.png"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432152/20220421_iIXqTEzAFp7m7cK_byl6nq.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "1-2 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432152/Pony_Lighthouse-1024x1024_qiu31t.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432152/neo_traditional_tattoo_flash_by_ivebeencalledmax_den9nz6-fullview.jpg_uqbqu8.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432153/bg_f8f8f8-flat_750x_075_f-pad_750x1000_f8f8f8_ax77bf.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Neo-Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432153/IMG_1336_npthyz.jpg"
        },
        {
            "userId": 2,
            "style": "Neo-Traditional",
            "size": "2-3 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Neo-Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432154/Moondal_CatFace_jsiv8p.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432206/08iupy43up211_mryc5l.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432207/image-asset_s4eb8p.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432207/IMG_4542_claetf.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432207/IMG_5204_tuyovw.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432208/RenyTattoos-Floral-Thigh-Rose-Peony-Jewelry_vikf6x.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432209/Screenshot_20201224-135426_Instagram_s4wu1f.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "2-3 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432209/IMG_4672-1-scaled_wnhbal.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432209/Sunflower_Tattoo_33_v1rav7.png"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Black and Grey.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432211/black-and-grey-tiger-tattoo-17_lia3qq.jpg"
        },
        {
            "userId": 3,
            "style": "Black and Grey",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Black and Grey.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432210/linework_20-_20black_20and_20Grey_20-_20illustrated_20-blackwork_20-_20illustrative_b8nl4g.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432302/chronic-ink-tk-realism-tattoo-swing-water_uaselw.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432303/34982375_212046306281436_2570810193222828032_n.4985cc4b0df849c031e0d07d0eaa1040_ceaagk.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Realism.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432304/MantleTattoo_Los-Angeles_realism_statue-tattoo-1024x1024_arhlq0.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432305/BlogThumbnail_Realism_Tattoo_v0qk9j.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432305/realistic_angel_m4w4g6.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Realism.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432305/AdobeStock_853671964-1080x675_tq4fpt.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432306/IMG-2092_twupbt.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432316/vv9gz7qy034NpJrw_of9cvw.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Realism.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432317/z2aD_Dc1JOvwiHEu_zhkqwe.jpg"
        },
        {
            "userId": 4,
            "style": "Realism",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Realism.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432318/realism-flash-art-by-a-tattoo-artist_zlol9i.png"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432394/minimal-creative-tattoo-design-set_53876-115576_sevdvw.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432392/hand-drawn-human-heart-sunburst-anatomically-correct-art-flash-tattoo-print-design-vector-illustration-100732645_i11dj2.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Illustrative.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432392/il_570xN.5539828186_2iee_aa2ut0.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432391/edgy-black-and-white-tattoo-flash-set_sc9cq6.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432391/1000_F_571578863_fyWZxWXrRZvDRwMEJ4KHENY04pn5yJXS_o56ucz.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432390/5-16-12-8-21-36-45m_zhvdty.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432389/Tattoo_Flash_Sheet_II_dy0yaq.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432389/Tattoo_Flash_Sheet_IV_oxeybw.png"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Illustrative.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432394/1000_F_318430092_Pp6koctH2NMJLcuoGgnGTLQejfqGvEuB_u3orhk.jpg"
        },
        {
            "userId": 5,
            "style": "Illustrative",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Illustrative.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432394/IMG_6321_1800x_arskb8.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433035/thumb_b9Eqtk2R1nMDHUjF_1080_1080_enu8kq.png"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433034/geometric-mandala-shoulder-tattoo-men-texas_x0nfz8.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Geometric.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433034/3d-geometric-tattoo-forearm_tvvxm3.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433025/Alexander-Lazo_qzktvv.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433020/bjornwallman_beautiful_geometric_tattoo_is_a_type_of_body_art_t_9586d685-1d84-4555-bcec-6c60724727a2_rq9pp8.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Geometric.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433020/t8shwd3c51311_jyhhxf.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433019/hand_geo_cassady_Web_qwnpdv.png"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433019/geometric-tattoo-artist-v0-9m4xufdni36a1_vaqoy2.jpg"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Geometric.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433036/f73250_8e3799f000af4d0080b350a1bcb55ecc_mv2_eha7k3.webp"
        },
        {
            "userId": 6,
            "style": "Geometric",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Geometric.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433040/geometrical-pattern-sleeve-tattoo_jfa9pl.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433076/phoenix-modern-tribal-tattoo-abstract-line-art-animals-minimalist-contour-vector_894890-63_zbgpag.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433075/wt8e32vlu6c71_hijycz.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Tribal.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433073/tribal_tattoo_design_vector_02_by_zymanko_dg8vuop-fullview.jpg_wq1wur.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433071/71p52vgdLQL._AC_UF1000_1000_QL80__pdsch9.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433071/360_F_526576605_Ty0m79gC26ZjlVOw1RIrtpSOim5evUaz_mnktc8.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Tribal.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433068/zg4a71vlu6c71_u8udek.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433066/2022-10-22-03.01.20-2954152452510370469_16100532_480x480_wsci5x.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433065/tribal-tattoo-designs_ddvpqm.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Tribal.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433077/tribal-tattoo-designs-and-patterns-vector-26200645_qudktd.jpg"
        },
        {
            "userId": 7,
            "style": "Tribal",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Tribal.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433080/Tribal_Tattoo_dqm87v.png"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433127/Watercolor-Tattoo-2-968x1024_yfbebo.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433126/Monty_YinYang_b4t003.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Watercolor.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433123/c846aba-7285-c5-66ee-c1364bc61a_Celebrate_the_Beauty_of_Nature_with_these_Inspirational_Sunflower_Tattoos_n7kojl.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433123/Copy_of_Water_Color_Tattoo___Braxton_Puckett___Edit___Photo___2022-4_wc9xyi.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433122/njxDO9ASdatTAScCe9Xe_file_wqkjcm.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433118/56zs3vmpbmw81_tslpcx.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433118/iss1fmf59pfc1_mxtbv6.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433117/18d1125-eef2-0d-185c-e8a8811f6d4d_Javi_Wolf_vjhg10.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Watercolor.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433128/10597517_556102737850360_1285715768_n-640x500_orvlvp.jpg"
        },
        {
            "userId": 8,
            "style": "Watercolor",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Watercolor.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433130/watercolour-tattoos_xo1mfi.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433205/Snapinsta.app_354905846_1189821965028553_6683682679098884190_n_1080_hnq73y.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433203/08m3psny5lxb1_zlxwub.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Dotwork.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433203/stunning-dotwork-tattoo-style_frj2ay.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433203/Dotwork_Tattoo_1_1024x1024_pd5yxe.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433203/Dotwork-Tattoo-Styles-7_hsii7o.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433199/BATM5BaJ04JZB5LrQDeHXeaMQ5z_cFSHiMWqP5Ncfns_iexhlz.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433198/dotwork-tatuaje_p2UXRrK.max-1000x1000.format-webp_xbspwv.webp"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433197/Snapinsta.app_398734820_1257615914917457_7944149893517495480_n_1080_pc74gf.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Dotwork.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433209/dotwork-lotus-ornamental-tattoo-design-lotus-flowers-57_ljo39u.jpg"
        },
        {
            "userId": 9,
            "style": "Dotwork",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Dotwork.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433209/pierog-dotwork-tattoo-from-this-week-polish-dumpling-v0-oj3qvp6igz1b1_mefrkz.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433276/duis5qsktjz81_f05xco.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433274/lc6p24h480h21_qvmcfx.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: American Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433273/815tGYN-N6L_lddydz.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433270/toad-with-a-blade-in-american-traditional-style-tattoo-v0-2xgakpd7g4jc1_hwvnbg.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433270/360_F_317106375_1jZgt43g4veCk14LXQbyMvM4YJyXqY8i_uo1axc.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: American Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433270/360_F_317106375_1jZgt43g4veCk14LXQbyMvM4YJyXqY8i_uo1axc.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433265/Don_TraditionalCompilation-1024x1024_c8t8mc.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433265/American-Traditional-Tattoo_eofhmt.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: American Traditional.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433277/FNlmDqpWQAcdD-M_l9wusb.jpg"
        },
        {
            "userId": 10,
            "style": "American Traditional",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: American Traditional.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433278/il_570xN.2985186778_spnb_qe2cxs.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Inspired by classic art styles. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433516/IMG_4668_tmgsvg.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "Another piece I loved working on. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433479/fineline_landing-2_cyr6bn.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "A bold statement for my client! Style: Fine Line.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433476/285273044_698612014528452_9205282709400539843_n_rnmmaj.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "Refining my craft with this one. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433475/nolen-nail-spa-nolensville-tn-37135-y23_zmmakj.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "Custom artwork made for you. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433473/IMG_9367-1_gs5izv.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 150.0,
            "caption": "Always thrilled to work on such intricate designs. Style: Fine Line.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433473/recent-botanical-fine-line-tattoo-done-by-kodi-in-frankfurt-v0-iqqp9pm1qrhc1_jpsw5p.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 200.0,
            "caption": "A meaningful piece for a special client. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433473/healed-fineline-tattoo-on-hand-artist-jess-nardo-at-crown-v0-ddbty31hhatc1_yxbeuv.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 250.0,
            "caption": "One of my favorite styles to work in. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433472/advice-new-fine-line-tattoo-v0-9r5at6w0593b1_yfcase.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 300.0,
            "caption": "An iconic piece for a unique individual. Style: Fine Line.",
            "available": False,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433516/e7vtrnaqnnb51_ifhgjy.jpg"
        },
        {
            "userId": 11,
            "style": "Fine Line",
            "size": "3-4 inches",
            "price": 100.0,
            "caption": "A beautiful custom design. Style: Fine Line.",
            "available": True,
            "imageUrl": "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433517/cfc8ff2e-6667-4d40-af19-814662fdbf44_x9c8n7.jpg"
        },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post1.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post2.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Traditional Japanese.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user12_post3.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post4.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post5.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Traditional Japanese.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user12_post6.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post7.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post8.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Traditional Japanese.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user12_post9.jpg"
        # },
        # {
        #     "userId": 12,
        #     "style": "Traditional Japanese",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Traditional Japanese.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user12_post10.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post1.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post2.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Neo-Traditional.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user13_post3.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post4.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post5.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Neo-Traditional.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user13_post6.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post7.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post8.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Neo-Traditional.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user13_post9.jpg"
        # },
        # {
        #     "userId": 13,
        #     "style": "Neo-Traditional",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Neo-Traditional.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user13_post10.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post1.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post2.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Black and Grey.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user14_post3.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post4.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post5.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Black and Grey.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user14_post6.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post7.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post8.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Black and Grey.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user14_post9.jpg"
        # },
        # {
        #     "userId": 14,
        #     "style": "Black and Grey",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Black and Grey.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user14_post10.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post1.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post2.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Realism.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user15_post3.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post4.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post5.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Realism.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user15_post6.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post7.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post8.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Realism.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user15_post9.jpg"
        # },
        # {
        #     "userId": 15,
        #     "style": "Realism",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Realism.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user15_post10.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post1.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post2.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Illustrative.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user16_post3.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post4.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post5.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Illustrative.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user16_post6.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post7.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post8.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Illustrative.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user16_post9.jpg"
        # },
        # {
        #     "userId": 16,
        #     "style": "Illustrative",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Illustrative.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user16_post10.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post1.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post2.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Geometric.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user17_post3.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post4.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post5.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Geometric.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user17_post6.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post7.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post8.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Geometric.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user17_post9.jpg"
        # },
        # {
        #     "userId": 17,
        #     "style": "Geometric",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Geometric.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user17_post10.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post1.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post2.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Tribal.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user18_post3.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post4.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post5.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Tribal.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user18_post6.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post7.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post8.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Tribal.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user18_post9.jpg"
        # },
        # {
        #     "userId": 18,
        #     "style": "Tribal",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Tribal.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user18_post10.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post1.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post2.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Watercolor.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user19_post3.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post4.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post5.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Watercolor.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user19_post6.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post7.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post8.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Watercolor.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user19_post9.jpg"
        # },
        # {
        #     "userId": 19,
        #     "style": "Watercolor",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Watercolor.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user19_post10.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Inspired by classic art styles. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post1.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "Another piece I loved working on. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post2.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "A bold statement for my client! Style: Dotwork.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user20_post3.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "Refining my craft with this one. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post4.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "Custom artwork made for you. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post5.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 150.0,
        #     "caption": "Always thrilled to work on such intricate designs. Style: Dotwork.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user20_post6.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 200.0,
        #     "caption": "A meaningful piece for a special client. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post7.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 250.0,
        #     "caption": "One of my favorite styles to work in. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post8.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 300.0,
        #     "caption": "An iconic piece for a unique individual. Style: Dotwork.",
        #     "available": False,
        #     "imageUrl": "https://example.com/images/user20_post9.jpg"
        # },
        # {
        #     "userId": 20,
        #     "style": "Dotwork",
        #     "size": "3-4 inches",
        #     "price": 100.0,
        #     "caption": "A beautiful custom design. Style: Dotwork.",
        #     "available": True,
        #     "imageUrl": "https://example.com/images/user20_post10.jpg"
        # }
    ]

    db.session.bulk_insert_mappings(Post, posts_data)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE TABLE {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
