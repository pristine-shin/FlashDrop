import { useState, useRef } from "react";
import { thunkAddPost } from "../../redux/posts";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import ConfirmationModal from "../../context/ConfirmationModal";
import "./AddPost.css";

function AddPost() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [size, setSize] = useState("");
  const [style, setStyle] = useState("");
  const [price, setPrice] = useState("");
  const [caption, setCaption] = useState("");
  const [available, setAvailable] = useState(true);
  const [imageUrl, setImageUrl] = useState(null);
  const [errors, setErrors] = useState({});
  const fileInputRef = useRef(null);
  const [showConfirmModal, setShowConfirmModal] = useState(false);

  const handleDivClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    setImageUrl(e.target.files[0]);
  };

  const handleCancel = () => {
    navigate(-1);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (sessionUser) {
      setErrors({});

      const formData = new FormData();
      formData.append("size", size);
      formData.append("style", style);
      formData.append("price", price);
      formData.append("caption", caption);
      formData.append("available", available);
      formData.append("imageUrl", imageUrl);

      for (const pair of formData.entries()) {
        console.log(`${pair[0]}: ${pair[1]}`);
      }

      try {
        const serverResponse = await dispatch(
          thunkAddPost(formData)
        );

        if (serverResponse) {
          setErrors(serverResponse);
        } else {
          setShowConfirmModal(true);
          setSize("");
          setStyle("");
          setAvailable(true);
          setPrice("");
          setCaption("");
          setImageUrl(null);
        }
      } catch (error) {
        setErrors({server: error.message});
        console.error("thunkAddPost not working:", error)
      }

    }
  };

  return (
    <div className="add-post-page">
      <div className="container-add-post">
        <form onSubmit={handleSubmit} encType="multipart/form-data" className="add-post-form">
          {/* <div className="post"> */}
          <h2 className="add-edit-header">New Post</h2>

          <div
            className="upload"
            onClick={handleDivClick}
            style={{ cursor: "pointer" }}
          >
            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              ref={fileInputRef}
              style={{ display: "none" }}
            />
            <label className="label imageurl">
              <div className="upload-button">Upload Post Image</div>
              <p className="upload-notes">
                <br></br>
                1400 x 1400 pixels minimum <br></br>(bigger is better)
              </p>
              <p className="upload-notes">
                <br></br>
                .jpg, .gif, or .png, 10MB max
              </p>
            </label>
          </div>
          {errors.imageUrl && <p className="error-message">{errors.imageUrl}</p>}

          <div className="add-post-detail-container">
            {/* <label className="label price">price:</label> */}
            <label className="label us-dollars">
              <input
                type="number"
                step="0.01"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                placeholder="Ex: 350.00"
                min="0.01"
                className="input price"
              />
              US Dollars
            </label>
            {errors.price && <p className="error-message">{errors.price}</p>}

            <label className="label style">
              Style:
              <input
                type="text"
                value={style}
                onChange={(e) => setStyle(e.target.value)}
                placeholder="Ex: American Traditional"
                className="input style"
              />
            </label>
            {errors.style && <p className="error-message">{errors.style}</p>}

            <label className="label size">
              Size:
              <input
                type="text"
                value={size}
                onChange={(e) => setSize(e.target.value)}
                placeholder="Ex: 6-9 inches"
                className="input size"
              />
            </label>
            {errors.size && <p className="error-message">{errors.size}</p>}

            <label className="label caption">Caption:</label>
            <textarea
              value={caption}
              onChange={(e) => setCaption(e.target.value)}
              placeholder="Ex: Want to do more tigers!!! Let's book :)"
              className="input textarea caption"
            />
            {errors.caption && <p className="error-message">{errors.caption}</p>}

            <label className="label available">Available:</label>
            <select
              value={available}
              onChange={(e) => setAvailable(e.target.value)}
              className="input available"
              style={{ color: available === "" ? "#AAA" : "#333" }}
            >
              <option value={true}>Yes</option>
              <option value={false}>No</option>
            </select>
            {errors.available && <p className="error-message">{errors.available}</p>}
          </div>


          <div className="ctas">
            <button type="submit" className="button submit">
              Add Post
            </button>
            <button
              type="button"
              className="button cancel"
              onClick={handleCancel}
            >
              Cancel
            </button>
          </div>
          {/* </div> */}
        </form>

        {showConfirmModal && (
          <ConfirmationModal
            onClose={() => {
              setShowConfirmModal(false)
              navigate(`/profile/session`);
            }}
            message={"You have added this post!"}
          />
        )}
      </div>
    </div>

  );
}

export default AddPost;
