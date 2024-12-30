import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import 'react-slideshow-image/dist/styles.css'
import { Fade, Zoom, Slide } from 'react-slideshow-image'
import "./HomePage.css";
import LoginFormPage from "../LoginFormPage";
import AllPosts from "../Post/AllPosts";
// import logo from "../../../src/flashdrop-logo.jpg"
import "./HomePage.css";

const slideImages = [
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433277/FNlmDqpWQAcdD-M_l9wusb.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433266/il_570xN.5667828062_ayy4_b3qs5d.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433205/Snapinsta.app_354905846_1189821965028553_6683682679098884190_n_1080_hnq73y.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433036/f73250_8e3799f000af4d0080b350a1bcb55ecc_mv2_eha7k3.webp",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432012/il_570xN.5546534375_pnqq_l8hh0m.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432013/tattoo-smart-flash-stamps-japanese-vol-2-29864566161591_3700x_pvallv.png",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432153/bg_f8f8f8-flat_750x_075_f-pad_750x1000_f8f8f8_ax77bf.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432316/vv9gz7qy034NpJrw_of9cvw.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432391/1000_F_571578863_fyWZxWXrRZvDRwMEJ4KHENY04pn5yJXS_o56ucz.jpg",
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432392/il_570xN.5539828186_2iee_aa2ut0.jpg",
    },
]

function HomePage() {
    const user = useSelector((store) => store.session.user);

    return (
        <>
            {user ? (
                <AllPosts />
            ) : (
                <div className="background">
                    <div className="homepage">
                        <div className="homepage-content">
                            <div className="homepage-preview">
                                <div className="preview-title">Find your next flash today. Discover. Book. Ink.</div>
                                <Fade>
                                    {slideImages.map((image, index) => (
                                        <div key={index}>
                                            <div className="preview-image" style={{ backgroundImage: `url(${image.url})` }}>
                                            </div>
                                        </div>
                                    ))}
                                </Fade>
                            </div>
                            <div className="login-form-container">
                                <LoginFormPage />
                            </div>
                        </div>
                    </div>
                </div>

            )}
        </>
    )
}

export default HomePage
