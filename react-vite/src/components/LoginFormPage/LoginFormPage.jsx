import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import '../../../src/index.css';
import "./LoginForm.css";
import { useNavigate } from "react-router-dom";

function LoginFormPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [usernameOrEmail, setUsernameOrEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    const newErrors = {};

    if (!usernameOrEmail) {
      newErrors.usernameOrEmail = "Please enter your username/email.";
    }

    if (!password) {
      newErrors.password = "Please enter your password.";
    }

    // If there are errors, update state and return early
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    const serverResponse = await dispatch(
      thunkLogin({
        email_or_username: usernameOrEmail,
        password,
      })
    );

    if (serverResponse) {
      setErrors({
        general: "Login failed. Please check your credentials and try again."
      });
    } else {
      navigate('/')
    }
  };

  const demoUserLogin = async (e) => {
    e.preventDefault();

    setErrors({});

    const serverResponse = await dispatch(
      thunkLogin({
        email_or_username: "inkedbyalex@gmail.com",
        password: "hashedpassword123"
      })
    );

    if (serverResponse) {
      setErrors({
        general: "Login failed. Please check your credentials and try again."
      });
    } else {
      navigate('/')
    }
  };

  return (
    <>
      <form className="modal-content" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username / Email</label>
          <input
            type="text"
            value={usernameOrEmail}
            onChange={(e) => setUsernameOrEmail(e.target.value)}
          />
          {errors.usernameOrEmail && <p className="error-message">{errors.usernameOrEmail}</p>}
        </div>

        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {errors.password && <p className="error-message">{errors.password}</p>}
        </div>

        {errors.general && <p className="error-message">{errors.general}</p>}

        <div className="form-group">
          <button type="submit">Log In</button>
        </div>

        <div className="or-divider">
          <span>OR</span>
        </div>

        <div className="form-group">
          <button type="button" onClick={demoUserLogin}>Demo Login</button>
        </div>
      </form>
    </>
  );
}

export default LoginFormPage;



// import { useState } from "react";
// import { thunkLogin } from "../../redux/session";
// import { useDispatch, useSelector } from "react-redux";
// import { Navigate, useNavigate } from "react-router-dom";
// import "./LoginForm.css";

// function LoginFormPage() {
//   const navigate = useNavigate();
//   const dispatch = useDispatch();
//   const sessionUser = useSelector((state) => state.session.user);
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [errors, setErrors] = useState({});

//   if (sessionUser) return <Navigate to="/" replace={true} />;

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     const serverResponse = await dispatch(
//       thunkLogin({
//         email,
//         password,
//       })
//     );

//     if (serverResponse) {
//       setErrors(serverResponse);
//     } else {
//       navigate("/");
//     }
//   };

//   return (
//     <>
//       {/* <h1>Log In</h1> */}
//       {errors.length > 0 &&
//         errors.map((message) => <p key={message}>{message}</p>)}
//       <form onSubmit={handleSubmit}>
//         <label>
//           Email
//           <input
//             type="text"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             required
//           />
//         </label>
//         {errors.email && <p>{errors.email}</p>}
//         <label>
//           Password
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </label>
//         {errors.password && <p>{errors.password}</p>}
//         <button type="submit">Log In</button>
//       </form>
//     </>
//   );
// }

// export default LoginFormPage;
