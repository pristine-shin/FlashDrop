import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { thunkSignup } from "../../redux/session";
import "../../../src/index.css";
import "./SignupForm.css";
import "../LoginFormPage/LoginForm.css"

function SignupFormPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [is_artist, setIsArtist] = useState(false);
  const [password, setPassword] = useState("");
  const [passwordVisible, setPasswordVisible] = useState(false);
  const [password2Visible, setPassword2Visible] = useState(false);
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});

  if (sessionUser) return <Navigate to="/" replace={true} />;

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

    const serverResponse = await dispatch(
      thunkSignup({
        email,
        username,
        password,
        is_artist
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      navigate("/");
    }
  };

  return (
    <>
    <div className="signup-page">
      <div className="signup-content">
        <div className="login-section">
          <p id="signup-header">Sign up to get access to your artist&apos;s next FlashDrop!</p>
          {errors.server && <p>{errors.server}</p>}
          <form className="form-content" onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="label-name">Email</label>
              <div className="input-error">
                <input
                  type="text"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />

                {errors.email && <p className="error-message">{errors.email}</p>}
              </div>
            </div>
            <div className="form-group">
              <label className="label-name">Username</label>
              <div className="input-error">
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />

                {errors.username && (
                  <p className="error-message">{errors.username}</p>
                )}
              </div>
            </div>
            <div className="form-group" id="artist-checkbox-container">
              <label className="label-name">I am a tattoo artist</label>
              <div className="input-error">
                <input
                  id="artist-checkbox"
                  type="checkbox"
                  value={is_artist}
                  onChange={() => setIsArtist(!is_artist)}
                />
                {errors.is_artist && (
                  <p className="error-message">{errors.is_artist}</p>
                )}
              </div>
            </div>
            <div className="form-group password-field">
              <label className="label-name">Password</label>
              <div className="input-error">
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
                {errors.password && (
                  <p className="error-message">{errors.password}</p>
                )}
              </div>
            </div>
            <div className="form-group password-field">
              <label className="label-name">Confirm Password</label>
              <div className="input-error">
                <input
                  type={password2Visible ? 'text' : 'password'}
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
                <button
                  type="button"
                  id="show-password"
                  onClick={() => setPassword2Visible(!password2Visible)}
                >
                  {password2Visible ? 'Hide' : 'Show'}
                </button>
                {errors.confirmPassword && (
                  <p className="error-message">{errors.confirmPassword}</p>
                )}
              </div>
            </div>
            <div className="form-group">
              <button type="submit" id="signup-button">Sign Up</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    </>
  );
}

export default SignupFormPage;
