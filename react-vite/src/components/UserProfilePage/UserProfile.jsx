import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
// import RemovePostModal from "../Post/RemovePostModal";
// import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faPenToSquare, faTrash } from "@fortawesome/free-solid-svg-icons";
// import "../Post/PostDetail.css";
import "./UserProfile.css";

// import Backdrop from '@mui/material/Backdrop';
// import CircularProgress from '@mui/material/CircularProgress';

const ProfilePage = () => {
    const [user, setUser] = useState(null);
    const [error, setError] = useState("");
    //   const [showModal, setShowModal] = useState(false);
    //   const [postIdToDelete, setPostIdToDelete] = useState(null);

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
    }, []);

    //   const handleOpenModal = (postId) => {
    //     setPostIdToDelete(postId);
    //     setShowModal(true);
    //   };

    //   const handleCloseModal = () => {
    //     setShowModal(false);
    //     setPostIdToDelete(null);
    //   };

    //   const handleDeletePost = async (postId) => {
    //     try {
    //       const response = await fetch(`/api/posts/${postId}`, {
    //         method: "DELETE",
    //       });
    //       if (!response.ok) {
    //         const errorData = await response.json();
    //         throw new Error(errorData.message || "Failed to delete post");
    //       }
    //       setUser((prevUser) => ({
    //         ...prevUser,
    //         posts: prevUser.posts.filter(
    //           (post) => post.postId !== postId
    //         ),
    //       }));
    //       handleCloseModal();
    //     } catch (err) {
    //       setError(err.message);
    //     }
    //   };

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
        // <Backdrop
        //   sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
        //   open
        // >
        //   <CircularProgress color="inherit" />
        // </Backdrop>
        <h1>Loading profile...</h1>
    );


    return (
        <div className="all-post-row">
            <div className="profile-header">
                <img src={user.profileImageUrl} alt="profile pic" id="big-profile-pic"/>
                <h2 className="all-posts-heading">@{user.username}</h2>
            </div>
            <div className="all-posts">
                {user.posts && user.posts.length > 0 ? (
                    user.posts.map((post) => (
                        <div key={post.id} className="all-post-card">
                            <Link to={`/posts/${post.id}`} className="all-post-card-link">
                                <div className="all-post-header">
                                    <h3 className="all-post-username">{post.username}</h3>
                                </div>
                                <img src={post.imageUrl} alt="post image" className="all-post-image" />
                                <div className="all-post-info">
                                    <p className="all-post-price">${post.price}</p>
                                    <p className="all-post-style">{post.style}</p>
                                    <p className="all-post-size">{post.size}</p>
                                    <p className="all-post-available">{post.available}</p>
                                    <p className="all-post-caption">{post.caption}</p>
                                    <p className="all-post-createdAt">{calculateDaysAgo(post.createdAt)} days ago</p>
                                </div>
                            </Link>
                        </div>
                    ))
                ) : (
                    <p>No posts available.</p>
                )}
            </div>
        </div>
    );
};

export default ProfilePage;
