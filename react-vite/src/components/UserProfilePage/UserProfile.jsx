import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import RemovePostModal from "../Post/RemovePostModal";
import { thunkRemovePost } from "../../redux/posts";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPenToSquare, faTrash } from "@fortawesome/free-solid-svg-icons";
// import "../Post/PostDetail.css";
import "./UserProfile.css";

import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

const ProfilePage = () => {
    const dispatch = useDispatch();
    const defaultProfileURL = "https://res.cloudinary.com/dmvfvyilq/image/upload/v1737061535/default-avatar-icon-of-social-media-user-vector_oz28zo.jpg";
    const [user, setUser] = useState(null);
    const [error, setError] = useState("");
    const [showModal, setShowModal] = useState(false);
    const [modalImage, setModalImage] = useState("");
    const [postIdToDelete, setPostIdToDelete] = useState(null);

    const openModal = (imagePath) => {
        setModalImage(imagePath);
        setShowModal(true);
    };

    const closeModal = () => {
        setShowModal(false);
        setModalImage("");
    };

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await fetch("/api/users/session");
                if (!response.ok) {
                    throw new Error("Failed to fetch user data");
                }
                const data = await response.json();
                setUser(data);
            } catch (err) {
                setError(err.message);
            }
        };

        fetchUser();
    }, [postIdToDelete, dispatch]);

    const handleOpenModal = (postId) => {
        setPostIdToDelete(postId);
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
        // setPostIdToDelete(null);
    };

    const handleOverlayClick = (event) => {
        // If the click happens directly on the overlay (not inside the modal), close the modal
        if (event.target.classList.contains("modal-overlay")) {
            handleCloseModal();
        }
    };

    const handleDeletePost = async (postId) => {
        dispatch(thunkRemovePost(postId)).then(() => setPostIdToDelete(null))
        // setUser((prevUser) => ({
        //     ...prevUser,
        //     posts: prevUser.posts.filter(
        //         (post) => post.postId !== postId
        //     ),
        // }));
        handleCloseModal();
    };


    // const formatDate = (dateString) => {
    //     const date = new Date(dateString);
    //     return date.toLocaleDateString("en-US", {
    //         year: "numeric",
    //         month: "long",
    //         day: "numeric",
    //     });
    // };
    const calculateDaysAgo = (date) => {
        const createdDate = new Date(date);
        const now = new Date();
        const diffInTime = now - createdDate;
        return Math.floor(diffInTime / (1000 * 3600 * 24));
    };

    if (error) return <p>{error}</p>;
    if (!user) return (
        <Backdrop
            sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
            open
        >
            <CircularProgress color="inherit" />
        </Backdrop>
    );


    return (
        <div className="profile-page-container">
            <div className="all-post-row">
                <div className="profile-header">
                    <div className="profile-header-row-1">
                        <img src={user.profileImageUrl ? (user.profileImageUrl) : (defaultProfileURL)} alt="profile pic" id="big-profile-pic" />
                        <div className="profile-header-details">{user.posts.length} posts</div>
                        <div className="profile-header-details">121 followers</div>
                        <div className="profile-header-details">33 follows</div>
                    </div>
                    <div className="profile-header-row-2">
                        <h2 className="profile-username">{user.username}</h2>
                        <h3 className="profile-bio">{user.bio}</h3>
                    </div>
                </div>
                <div className="all-posts">
                    {user.posts && user.posts.length > 0 ? (
                        user.posts.map((post) => (
                            <div key={post.id} className="all-post-card">
                                <Link to={`/posts/${post.id}`} className="all-post-card-link">
                                    <img src={post.imageUrl} alt="post image" className="all-post-image" />
                                </Link>
                                <div className="all-post-info">
                                    <div className="price-with-edit-button">
                                        <div className="all-post-price">${post.price}</div>
                                        <div className="manage-post-links">
                                            <Link
                                                to={`/posts/edit/${post.id}`}
                                                className="manage-post-button"
                                            >
                                                <FontAwesomeIcon icon={faPenToSquare} />
                                            </Link>
                                            <button
                                                onClick={() => handleOpenModal(post.id)}
                                                className="manage-post-button"
                                            >
                                                <FontAwesomeIcon icon={faTrash} />
                                            </button>
                                        </div>
                                    </div>
                                    <p className="all-post-style">{post.style}</p>
                                    <p className="all-post-size">{post.size}</p>
                                    <div className="caption-container">
                                        <span className="all-post-size">
                                            {user.username}
                                        </span>
                                        <span className="all-post-caption">
                                            {post.caption}
                                        </span>
                                    </div>
                                    <p className="all-post-createdAt">{calculateDaysAgo(post.createdAt)} days ago</p>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p>No posts available.</p>
                    )}

                    {/* Modals
                    {showModal && (
                        <RemovePostModal
                            postId={postIdToDelete}
                            onConfirm={handleDeletePost}
                            onCancel={handleCloseModal}
                        />
                    )} */}

                    {/* Modals */}
                    {showModal && (
                        <div
                            className="modal-overlay"
                            onClick={handleOverlayClick}
                        >
                            <div className="modal-content">
                                <RemovePostModal
                                    postId={postIdToDelete}
                                    onConfirm={handleDeletePost}
                                    onCancel={handleCloseModal}
                                />
                            </div>
                        </div>
                    )}

                </div>
            </div>
        </div>
    );
};

export default ProfilePage;
