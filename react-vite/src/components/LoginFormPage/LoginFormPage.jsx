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
  const [passwordVisible, setPasswordVisible] = useState(false);

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
    <div className="login-section">
      <h1 className="app-title">FlashDrop</h1>
      <form className="form-content" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username / Email</label>
          <input
            type="text"
            value={usernameOrEmail}
            onChange={(e) => setUsernameOrEmail(e.target.value)}
          />
          {errors.usernameOrEmail && <p className="error-message">{errors.usernameOrEmail}</p>}
        </div>

        <div className="form-group password-field">
          <label>Password</label>
          <input
            type={passwordVisible ? 'text' : 'password'}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button
            type="button"
            id="show-password"
            onClick={() => setPasswordVisible(!passwordVisible)}
          >
            {passwordVisible ? 'Hide' : 'Show'}
          </button>
          {errors.password && <p className="error-message">{errors.password}</p>}
        </div>

        {errors.general && <p className="error-message">{errors.general}</p>}

        <div className="form-group">
          <button type="submit" id="login-button">Log In</button>
        </div>

        <div className="or-divider">
          <span>OR</span>
        </div>

        <div className="form-group">
          <button type="button" id="demo-login-button" onClick={demoUserLogin}>Demo Login</button>
        </div>
      </form>
      <div className="signup-section">
        <span>Don’t have an account? </span>
        <a href="/signup" className="signup-link">
          Sign up
        </a>
      </div>
    </div>
    </>
  );
}

export default LoginFormPage;
