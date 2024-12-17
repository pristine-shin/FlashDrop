// import { NavLink } from "react-router-dom";
// import ProfileButton from "./ProfileButton";
// import "./Navigation.css";

// function Navigation() {
//   return (
//     <nav>
//       <ul>
//         <li>
//           <NavLink to="/">Home</NavLink>
//         </li>

//         <li>
//           <ProfileButton />
//         </li>
//       </ul>
//     </nav>
//   );
// }

// export default Navigation;


// Navigation.jsx
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
// import AddButton from "./AddButton"
// import logo from "../../../src/flashdrop-logo.jpg"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart } from '@fortawesome/free-regular-svg-icons';
import "./Navigation.css";
import { useEffect } from "react";

function Navigation() {
  const user = useSelector((store) => store.session.user);

  return (
    <nav>
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
              {/* <AddButton /> */}
            </li>
            <li className="nav-right">
              <NavLink to="/wishlist" className="nav-icon-link">
                <FontAwesomeIcon icon={faHeart} className="nav-icon" />
              </NavLink>
            </li>
            <li className="nav-right">
              <ProfileButton buttonClass="profile-button" />
            </li>
          </>
        ) : (
          <>
            <li className="nav-right">
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
            </li>
          </>
        )}
      </ul>
    </nav>
  );
}

export default Navigation;
