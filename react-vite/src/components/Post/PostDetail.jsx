import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import AddCommentModal from "../Comment/AddCommentModal";
import EditCommentModal from "../Comment/EditCommentModal";
import RemoveCommentModal from "../Comment/RemoveCommentModal";
import {
  thunkRemoveComment,
  thunkGetUserComments,
} from "../../redux/comments";
import {
  thunkGetPostComments,
  thunkGetPostById,
} from "../../redux/posts";
// import { thunkAddFavoritesItem, selectFavoritesItem, thunkRemoveFavoritesItem, thunkGetFavorites } from "../../redux/favorites";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHeart,
  faPlus,
  faPenToSquare,
  faTrash,
  faShare,
} from "@fortawesome/free-solid-svg-icons";
import "./PostDetail.css";
import ConfirmationModal from "../../context/ConfirmationModal";

import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

const PostDetail = () => {
  const { postId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  // const favorites = useSelector(state => selectFavoritesItem(state, postId))
  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [showAddModal, setShowAddModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showRemoveModal, setShowRemoveModal] = useState(false);
  // const [showFavoritesConfirmModal, setShowFavoritesConfirmModal] = useState(false);
  // const [showFavoritesRemoveModal, setShowFavoritesRemoveModal] = useState(false);
  const [currentComment, setCurrentComment] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [modalImage, setModalImage] = useState("");
  const dispatch = useDispatch();

  const openModal = (imagePath) => {
    setModalImage(imagePath);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setModalImage("");
  };

  useEffect(() => {
    dispatch(thunkGetPostById(postId)).then((res) => setPost(res));
  }, [postId, dispatch]);

  useEffect(() => {
    dispatch(thunkGetUserComments());
    dispatch(thunkGetPostComments(postId)).then((res) =>
      setComments(res.comments)
    );
  }, [currentComment, dispatch, postId]);

  // useEffect(() => {
  //   if (sessionUser) dispatch(thunkGetFavorites())
  // }, [sessionUser, dispatch])

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  };

  const handleRemoveComment = async (commentId) => {
    dispatch(thunkRemoveComment(commentId, postId)).then(() => setCurrentComment(""));
    closeModals();
  };

  const openAddCommentModal = () => setShowAddModal(true);
  const openEditCommentModal = (comment) => {
    setCurrentComment(comment);
    setShowEditModal(true);
  };
  const openRemoveCommentModal = (comment) => {
    setCurrentComment(comment);
    setShowRemoveModal(true);
  };

  const closeModals = () => {
    setShowAddModal(false);
    setShowEditModal(false);
    setShowRemoveModal(false);
    setCurrentComment(null);
  };

  // const addToFavorites = async (postId) => {
  //   dispatch(thunkAddFavoritesItem(postId));
  //   setShowFavoritesConfirmModal(true);
  // };

  // const removeFromFavorites = async (postId) => {
  //   dispatch(thunkRemoveFavoritesItem(postId));
  //   setShowFavoritesRemoveModal(true);
  // }

  if (!post) return (
    <Backdrop
      sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
      open
    >
      <CircularProgress color="inherit" />
    </Backdrop>
  );

  return (
    <div className="post-detail-page">
      {/* Dynamic Modal */}
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
      <div className="post-row">
        <div className="post-detail">
          <div className="post-column">
            {/* <div className="post-meta"> */}

            <div className="post-image-column">
              <img
                src={post.imageUrl}
                alt="post image"
                className="post-image-big"
              />
              <button
                className="post-detail-button"
                style={{ cursor: "pointer" }}
                onClick={() => openModal("https://res.cloudinary.com/dmvfvyilq/image/upload/v1735340873/modern-coming-soon-loading-icon-600nw-2506897855_zdkeal.jpg")}
              >
                <FontAwesomeIcon icon={faShare} className="nav-icon" /> Share
                / Embed
              </button>
              {/* Favorites Button */}
              {/* {sessionUser &&
                  (favorites[postId] ?
                    <button
                      onClick={() => removeFromFavorites(postId)}
                      className="post-detail-button"
                      style={{ color: 'grey' }}
                    >
                      <FontAwesomeIcon icon={faHeart} className="nav-icon" />{" "}
                      Favorites
                    </button>
                    :
                    <button
                      onClick={() => addToFavorites(postId)}
                      className="post-detail-button"
                    >
                      <FontAwesomeIcon icon={faHeart} className="nav-icon" />{" "}
                      Favorites
                    </button>
                  )} */}
              <div className="post-caption-area">
                <Link to={`/profile/${post.userId}`} className="username-link">
                  <span className="post-artist-name">
                    {post.username}
                  </span>
                </Link>
                <span>
                  {post.caption}
                </span>
              </div>
              <p className="post-created-time">
                {formatDate(post.createdAt)}
              </p>
              {/* Comments Section */}
              <div className="comments-section">
                <p className="comments-title">Comments</p>
                {comments.length > 0 ? (
                  <>
                    {comments.map((comment, index) => (
                      <div className="comment" key={index}>
                        <div className="comment-image">
                          <img
                            src={comment.profileImageUrl}
                            alt={`${comment.username}'s profile pic`}
                            className="profile-image"
                          />
                        </div>
                        <div className="comment-info">
                          <p className="comment-content">
                            <span className="comment-name">
                              <strong>
                                {comment.username || "Anonymous"}
                              </strong>
                            </span>
                            {comment.content}
                          </p>
                          {sessionUser && sessionUser.id === comment.userId ? (
                            <>
                              <button
                                onClick={() => openEditCommentModal(comment)}
                                className="post-detail-button"
                              >
                                <FontAwesomeIcon
                                  icon={faPenToSquare}
                                  className="nav-icon"
                                />
                                Edit
                              </button>
                              <button
                                onClick={() => openRemoveCommentModal(comment)}
                                className="post-detail-button"
                              >
                                <FontAwesomeIcon
                                  icon={faTrash}
                                  className="nav-icon"
                                />
                                Remove
                              </button>
                            </>
                          ) : (
                            <div></div>
                          )}
                        </div>
                      </div>
                    ))}
                  </>
                ) : (
                  <p>No comments available for this post.</p>
                )}
                {sessionUser &&
                  post.userId !== sessionUser.id &&
                  !comments.find(
                    (comment) => comment.userId === sessionUser.id
                  ) ? (
                  <button
                    onClick={openAddCommentModal}
                    className="post-detail-button"
                  >
                    <FontAwesomeIcon icon={faPlus} className="nav-icon" />
                    Add
                  </button>
                ) : (
                  <div></div>
                )}
              </div>
            </div>
            {/* </div> */}
          </div>
          <div className="artist-column">
            <Link to={`/profile/${post.userId}`} className="username-link">

              <img
                src={post.profileImageUrl}
                alt={`${post.username}'s profile`}
                className="profile-image-small"
              />
              <p className="post-artist">@{post.username}</p>
            </Link>
            <button
              className="follow"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("https://res.cloudinary.com/dmvfvyilq/image/upload/v1735340873/modern-coming-soon-loading-icon-600nw-2506897855_zdkeal.jpg")}
            >
              Follow
            </button>
            <p className="detail-artist-bio">
              {post.artistBio}<br></br>
              <br></br>
            </p>
            <p className="artist-contact">Contact / Help</p>
            <p
              className="bio-more"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("https://res.cloudinary.com/dmvfvyilq/image/upload/v1735340873/modern-coming-soon-loading-icon-600nw-2506897855_zdkeal.jpg")}
            >
              <br></br>Contact {post.username}
              <br></br>
              <br></br>Report this post or account
            </p>
          </div>
        </div>

        {/* Modals */}
        {showAddModal && (
          <AddCommentModal onClose={closeModals}
            setCurrentComment={setCurrentComment} postId={postId} />
        )}

        {showEditModal && currentComment && (
          <EditCommentModal
            comment={currentComment}
            onClose={closeModals}
            setCurrentComment={setCurrentComment}
          />
        )}

        {showRemoveModal && currentComment && (
          <RemoveCommentModal
            comment={currentComment}
            onClose={closeModals}
            onConfirm={() => handleRemoveComment(currentComment.id)}
          />
        )}

        {/* {showFavoritesRemoveModal && (
          <ConfirmationModal
            onClose={() => {
              setShowFavoritesRemoveModal(false);
            }}
            message={"You have removed the post to your favorites!"}
          />
        )};

        {showFavoritesConfirmModal && (
          <ConfirmationModal
            onClose={() => {
              setShowFavoritesConfirmModal(false)
            }}
            message={"You have added the post to your favorites!"}
          />
        )}; */}

      </div>
    </div>
  );
};

export default PostDetail;
