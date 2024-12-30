import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import LoginFormPage from "../LoginFormPage";
import AllPosts from "../Post/AllPosts";
import "./HomePage.css";

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
                            <LoginFormPage />
                        </div>
                    </div>
                </div>

            )}
        </>
    )
}

export default HomePage
