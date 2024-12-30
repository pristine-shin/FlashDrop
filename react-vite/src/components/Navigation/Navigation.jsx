// Navigation.jsx
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import AddButton from "./AddButton"
// import logo from "../../../src/flashdrop-logo.jpg"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart } from '@fortawesome/free-regular-svg-icons';
import "./Navigation.css";
import { useEffect } from "react";

function Navigation() {
  const user = useSelector((store) => store.session.user);
  const [showModal, setShowModal] = useState(false);
  const [modalImage, setModalImage] = useState("");

  const openModal = (imagePath) => {
    setModalImage(imagePath);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setModalImage("");
  };

  return (
    <nav>
      {showModal && (
        <div className="confirmation-modal-overlay" onClick={closeModal}>
          <div
            className="tbd-confirmation-modal-content"
            onClick={(e) => e.stopPropagation()}
          >
            <img src={modalImage} alt="Modal Content" className="modal-image" />
          </div>
        </div>
      )}
      <ul className="nav-right">
        <li className="nav-logo">
          <NavLink to="/">
            {/* <img src={logo} alt="Logo" className="logo" /> */}
            FlashDrop
          </NavLink>
        </li>
        {user ? (
          <>
            <li className="nav-right">
              <AddButton />
            </li>
            <li className="nav-right">
              {/* <NavLink to="/likes" className="nav-icon-link"> */}
              <button
                className="nav-likes-button"
                onClick={() => openModal("https://res.cloudinary.com/dmvfvyilq/image/upload/v1735340873/modern-coming-soon-loading-icon-600nw-2506897855_zdkeal.jpg")}
              >
                <FontAwesomeIcon icon={faHeart} className="nav-icon-link" />
              </button>
              {/* </NavLink> */}
            </li>
            <li className="nav-right">
              <ProfileButton />
            </li>
          </>
        ) : (
          <>
            {/* <li className="nav-right">
              <OpenModalMenuItem
                itemText="Log In"
                modalComponent={<LoginFormModal />}
                buttonClass="login-button"
              />
            </li>
            <li className="nav-right">
              <OpenModalMenuItem
                itemText="Sign Up"
                modalComponent={<SignupFormModal />}
                buttonClass="signup-button"
              />
            </li> */}
          </>
        )}
      </ul>
    </nav>
  );
}

export default Navigation;
