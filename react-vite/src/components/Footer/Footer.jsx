// import React from "react";
import "./Footer.css";
import "./Footer.css";
import linkedinLogo from "../../../../readme-logos/linkedin-logo.png";
import githubLogo from "../../../../readme-logos/github-logo.png";

const Footer = () => {
  return (

    <footer className="footer">
      <div className="footer-links">
        <a href="https://github.com/pristine-shin/FlashDrop">GitHub</a>
        <a href="https://www.linkedin.com/in/pristine-shin/">LinkedIn</a>
        <a href="mailto:shin.pristine@gmail.com">Email</a>
      </div>
      <div className="footer-meta">&copy; 2024 FlashDrop from Pristine</div>
    </footer>
  );
};

export default Footer;
