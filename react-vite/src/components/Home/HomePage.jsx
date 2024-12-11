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

            <footer className="homepage-footer">
                <div className="footer-links">
                    <a href="#">About</a>
                    <a href="#">Blog</a>
                    <a href="#">Jobs</a>
                    <a href="#">Help</a>
                    <a href="#">Privacy</a>
                    <a href="#">Terms</a>
                </div>
                <div className="footer-meta">&copy; 2024 Flashbop from Pristine</div>
            </footer>
        </body>
    )
}

export default HomePage
