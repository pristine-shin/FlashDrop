import LoginFormPage from "../LoginFormPage";
import "./HomePage.css";

function HomePage() {

    return (
        <body className="homepage">
            <div className="homepage-content">
                <div className="login-section">
                    <h1 className="app-title">FlashDrop</h1>
                    <LoginFormPage />

                    <div className="signup-section">
                        <span>Don’t have an account? </span>
                        <a href="/signup" className="signup-link">
                            Sign up
                        </a>
                    </div>
                </div>
            </div>
        </body>
    )
}

export default HomePage
