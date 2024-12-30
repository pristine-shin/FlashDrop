import React from 'react'
import 'react-slideshow-image/dist/styles.css'
import { Fade, Zoom, Slide } from 'react-slideshow-image'
import "./HomePage.css";

const slideImages = [
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433277/FNlmDqpWQAcdD-M_l9wusb.jpg",
        caption: "First Slide"
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433266/il_570xN.5667828062_ayy4_b3qs5d.jpg",
        caption: "Second Slide"
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433205/Snapinsta.app_354905846_1189821965028553_6683682679098884190_n_1080_hnq73y.jpg",
        caption: "Third Slide"
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733433036/f73250_8e3799f000af4d0080b350a1bcb55ecc_mv2_eha7k3.webp",
        caption: "Fourth Slide"
    },
    {
        url: "https://res.cloudinary.com/dmvfvyilq/image/upload/v1733432012/il_570xN.5546534375_pnqq_l8hh0m.jpg",
        caption: "Fifth Slide"
    },
]

const ImageSlider = () => {
    return (
        <div className='slide-container'>
            <Fade>
                {slideImages.map((image, index) => (
                    <div key={index}>
                        <div className="preview-image" style={{backgroundImage:`url(${image.url})`}}>
                            <span className='preview-caption'>{image.caption}</span>
                        </div>
                    </div>
                ))}
            </Fade>
        </div>
    )
}

export default ImageSlider
