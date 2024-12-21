import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
// import AddCommentModal from "../Comment/AddCommentModal";
// import EditCommentModal from "../Comment/EditCommentModal";
// import RemoveCommentModal from "../Comment/RemoveCommentModal";
// import {
//   thunkRemoveComment,
//   thunkGetUserComments,
// } from "../../redux/comments";
import {
//   thunkGetPostComments,
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

  // useEffect(() => {
  //   dispatch(thunkGetUserComments());
  //   dispatch(thunkGetPostComments(postId)).then((res) =>
  //     setComments(res.comments)
  //   );
  // }, [currentComment, dispatch, postId]);

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
            className="confirmation-modal-content"
            onClick={(e) => e.stopPropagation()}
          >
            <img src={modalImage} alt="Modal Content" className="modal-image" />
          </div>
        </div>
      )}
      <div className="post-row">
        <div className="banner-container">
          {/* Banner Section */}
          {post?.bannerImageUrl && (
            <div
              className="banner"
              style={{ backgroundImage: `url(${post.bannerImageUrl})` }}
            />
          )}
        </div>
        <div className="post-detail">
          <div className="post-column">
            <div className="post-meta">
              <div className="post-info-column">
                <h2 className="post-name">{post.name}</h2>
                <p className="post-artist">
                  by{" "}
                  <span
                    className="post-artist-name"
                    style={{ cursor: "pointer" }}
                    onClick={() => openModal("/images/meme.jpg")}
                  >
                    {post.artistName}
                  </span>
                </p>
                {[
                  "music",
                  "cd",
                  "cassette",
                  "vinyl_lp",
                  "double_vinyl_lp",
                  "vinyl_7",
                  "vinyl_box_set",
                  "other_vinyl",
                  "CD",
                  "Vinyl",
                ].includes(post.type) && (
                    <img
                      src="/images/play.png"
                      alt="Post Image"
                      className="post-play"
                      style={{ cursor: "pointer" }}
                      onClick={() => openModal("/images/meme.jpg")}
                    />
                  )}
                {showModal && (
                  <div
                    className="confirmation-modal-overlay"
                    onClick={closeModal}
                  >
                    <div
                      className="confirmation-modal-content"
                      onClick={(e) => e.stopPropagation()}
                    >
                      <img
                        src={modalImage}
                        alt="Modal Content"
                        className="modal-image"
                      />
                    </div>
                  </div>
                )}

                <p className="post-type">{post.type}</p>
                <p className="post-genre">
                  {post.genre ? post.genre : "Streaming + Download"}
                </p>
                <p className="post-description">{post.description}</p>
                <p className="download-available">
                  Download available in 16-bit/44.1kHz.
                </p>
                <p className="post-price">
                  ${post.price}
                  <span className="USD">USD</span>
                  <span className="or-more">or more</span>
                </p>
                <p className="lyric">
                  {post.artistName} ๏ vocals, guitars, charango, cellos,
                  percussions
                  <br></br>
                  Tuulia ๏ vocals<br></br>
                  Misha Mullov-Abbado ๏ double bass<br></br>
                  Shir-Ran Yinon ๏ violin<br></br>
                  <br></br>
                  <br></br>
                  Spririts around we’re grateful for your presence<br></br>
                  Ancestors around we hear your songs in the wind<br></br>
                  We walk on holy ground<br></br>
                  listen to the ancient sound<br></br>
                  Spirits around we’re dancing with you<br></br>
                  <br></br>
                  Andelelele<br></br>
                  Andelelele<br></br>
                  Andelelele leyo<br></br>
                  <br></br>
                  <br></br>
                  from {post.artistName}, released February 3, 2023<br></br>
                  Music & lyrics by {post.artistName}
                  <br></br>
                  <br></br>
                  <br></br>
                  all rights reserved<br></br>
                </p>
                <p className="tag-title">Tags</p>
                <p
                  className="tags"
                  style={{ cursor: "pointer" }}
                  onClick={() => openModal("/images/meme.jpg")}
                >
                  #world #medicinemusic world medicina medicine music medicine
                  songs world music Leipzig
                </p>
              </div>
              <div className="post-image-column">
                <img
                  src={post.imageUrl}
                  alt={post.name}
                  className="post-image-big"
                />
                <button
                  className="post-detail-button"
                  style={{ cursor: "pointer" }}
                  onClick={() => openModal("/images/meme.jpg")}
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
                {/* Comments Section */}
                <div className="comments-section">
                  <p className="comments-title">supported by</p>
                  {comments.length > 0 ? (
                    <>
                      {comments.map((comment, index) => (
                        <div className="comment" key={index}>
                          <div className="comment-image">
                            <img
                              src={comment.profileImageUrl}
                              alt={`${comment.artistName}'s profile`}
                              className="profile-image"
                            />
                          </div>
                          <div className="comment-info">
                            <p className="comment-content">
                              <span className="comment-name">
                                <strong>
                                  {comment.artistName || "Anonymous"}
                                </strong>
                              </span>
                              {comment.comment}
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
                      <p
                        className="more"
                        style={{ cursor: "pointer" }}
                        onClick={() => openModal("/images/meme.jpg")}
                      >
                        more...
                      </p>
                      <img
                        src="/images/supporters.png"
                        alt="Supporter Icon"
                        className="supporter-image"
                      />
                      <p
                        className="more"
                        style={{ cursor: "pointer" }}
                        onClick={() => openModal("/images/meme.jpg")}
                      >
                        more...
                      </p>
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
            </div>
          </div>
          <div className="artist-column">

            <img
              src={post.profileImageUrl}
              alt={`${post.artistName}'s profile`}
              className="profile-image-small"
            />
            <p className="post-artist">{post.artistName}</p>
            <p className="US">US</p>
            <button
              className="follow"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("/images/meme.jpg")}
            >
              Follow
            </button>
            <p className="artist-bio">
              {post.artistBio}<br></br>
              <br></br>
            </p>
            <p
              className="bio-more"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("/images/meme.jpg")}
            >
              more<br></br>
              <br></br>aquario-music.com
            </p>
            <p className="artist-discography">discography</p>
            <img
              src={post.imageUrl}
              alt={post.name}
              className="post-image-small"
            />
            <p
              className="post-name-small"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("/images/meme.jpg")}
            >
              {post.name}
            </p>
            <p className="post-created-time">
              {formatDate(post.createdAt)}
            </p>
            <p className="artist-contact">contact / help</p>
            <p
              className="bio-more"
              style={{ cursor: "pointer" }}
              onClick={() => openModal("/images/meme.jpg")}
            >
              <br></br>Contact {post.artistName}
              <br></br>
              <br></br>Streaming and Download help
              <br></br>
              <br></br>Report this album or account
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
