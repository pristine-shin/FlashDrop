import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import {
  thunkEditPost,
  thunkGetPostById,
} from "../../redux/posts";
import "./EditPost.css";
import ConfirmationModal from "../../context/ConfirmationModal";

function EditPost() {
  const { postId } = useParams();
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

  useEffect(() => {
    const fetchPost = async () => {
      const postData = await dispatch(thunkGetPostById(postId));
      if (postData) {
        setSize(postData.size);
        setStyle(postData.style);
        setPrice(postData.price);
        setCaption(postData.caption);
        setAvailable(postData.available);
        setImageUrl(postData.imageUrl);
      } else {
        navigate("/not-found");
      }
    };

    fetchPost();
  }, [dispatch, postId, navigate]);

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
      formData.append("id", postId);
      formData.append("size", size);
      formData.append("style", style);
      formData.append("price", price);
      formData.append("caption", caption);
      formData.append("available", available);
      formData.append("imageUrl", imageUrl);

      try {
        const serverResponse = await dispatch(
          thunkEditPost(formData)
        );

        if (serverResponse) {
          setErrors(serverResponse);
        } else {
          setShowConfirmModal(true);
        }
      } catch (error) {
        setErrors({ server: error.message });
        console.error("thunkEditPost not working:", error);
      }
    }
  };

  return (
    <div className="container-edit-post">
      <form onSubmit={handleSubmit} encType="multipart/form-data" className="edit-post-form">
        <div className="post">
          <h2 className="header">Edit Post</h2>
          <label className="label size">Size:</label>
          <input
            type="text"
            value={size}
            onChange={(e) => setSize(e.target.value)}
            className="input size"
          />
          {errors.size && <p className="error-message">{errors.size}</p>}

          <label className="label style">Style:</label>
          <input
            type="text"
            value={style}
            onChange={(e) => setStyle(e.target.value)}
            className="input style"
          />
          {errors.style && <p className="error-message">{errors.style}</p>}

          <label className="label price">Price:</label>
          <label className="label us-dollars">
            <input
              type="number"
              step="0.01"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              min="0.01"
              className="input price"
            />
            US Dollars
          </label>
          {errors.price && <p className="error-message">{errors.price}</p>}

          <label className="label caption">caption:</label>
          <textarea
            value={caption}
            onChange={(e) => setCaption(e.target.value)}
            className="input textarea caption"
          />
          {errors.caption && <p className="error-message">{errors.caption}</p>}
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
              className="input imageurl"
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

          <label className="label available">available:</label>
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
                  <div className="ctas">
            <button type="submit" className="button submit">
              Update Post
            </button>
            <button
              type="button"
              className="button cancel"
              onClick={handleCancel}
            >
              cancel
            </button>
          </div>
        </div>
      </form>
      {showConfirmModal && (
        <ConfirmationModal
          onClose={() => {
            setShowConfirmModal(false)
            navigate(`/profile/${sessionUser.id}`);
          }}
          message={"You have updated this post!"}
        />
      )}
    </div>
  );
}

export default EditPost;
