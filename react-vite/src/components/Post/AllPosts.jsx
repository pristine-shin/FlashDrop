import { useEffect } from "react";
import { Link } from "react-router-dom";
import { thunkGetAllPosts, selectAllPostsArry } from "../../redux/posts";
import { useDispatch, useSelector } from "react-redux";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPenToSquare, faTrash, faCalendarPlus, faCalendarXmark } from "@fortawesome/free-solid-svg-icons";

import "./AllPosts.css";

import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

function AllPosts() {
  const dispatch = useDispatch();
  const allPosts = useSelector(selectAllPostsArry)

  useEffect(() => {
    dispatch(thunkGetAllPosts());
  }, [dispatch]);

  if (!allPosts) {
    return (
      <Backdrop
      sx={(theme) => ({ color: '#fff', zIndex: theme.zIndex.drawer + 1 })}
      open
    >
      <CircularProgress color="inherit" />
    </Backdrop>
    )
  }

  const calculateDaysAgo = (date) => {
    const createdDate = new Date(date);
    const now = new Date();
    const diffInTime = now - createdDate;
    return Math.floor(diffInTime / (1000 * 3600 * 24));
  };

  const shufflePosts = (posts) => {
    for (let i = posts.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [posts[i], posts[j]] = [posts[j], posts[i]]
    }
  }

  shufflePosts(allPosts);

  return (
    <div className="all-post-container">
      {/* <h2 className="all-posts-heading">Your Feed</h2> */}
      <div className="all-posts">
        {allPosts.length > 0 ? (
          allPosts.map((post) => (
            <div key={post.id} className="all-post-card">
              <Link to={`/profile/${post.userId}`} className="all-post-card-link">
                <div className="all-post-header">
                  <img src={post.profileImageUrl} alt="profile pic" className="profile-pic" />
                  <h3 className="all-post-username">{post.username}</h3>
                </div>
              </Link>
              <Link to={`/posts/${post.id}`} className="all-post-card-link">
                <img src={post.imageUrl} alt="post image" className="all-post-image" />
                <div className="all-post-info">
                <div className="price-with-edit-button">
                    <div className="all-post-price">${post.price}</div>
                    <div className="manage-post-links">
                      <div className="all-post-available">{post.available ? (
                        <div className="booking-icon">
                          <button
                            className="available-post-button"
                            style={{ cursor: "pointer" }}
                            onClick={() => openModal("https://res.cloudinary.com/dmvfvyilq/image/upload/v1735340873/modern-coming-soon-loading-icon-600nw-2506897855_zdkeal.jpg")}
                          >
                            <FontAwesomeIcon icon={faCalendarPlus} />
                          </button>
                          <div className="hide">Book Now</div>
                        </div>
                      ) : (
                        <div className="booking-icon">
                          <button
                            onClick={() => handleOpenModal(post.id)}
                            className="na-post-button"
                          >
                            <FontAwesomeIcon icon={faCalendarXmark} />
                          </button>
                          <div className="hide">Unavailable</div>
                        </div>

                      )}</div>
                    </div>
                  </div>
                  {/* <p className="all-post-price">${post.price}</p> */}
                  <p className="all-post-style">{post.style}</p>
                  <p className="all-post-size">{post.size}</p>
                  {/* <p className="all-post-caption">{post.caption}</p> */}
                  <div className="caption-container">
                      <span className="all-post-username">
                        {post.username}
                      </span>
                    <span className="all-post-caption">
                      {post.caption}
                    </span>
                  </div>
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
}

export default AllPosts;
