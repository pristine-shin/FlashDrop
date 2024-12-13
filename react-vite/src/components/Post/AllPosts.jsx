import { useEffect } from "react";
import { Link } from "react-router-dom";
import { thunkGetAllPosts, selectAllPostsArry } from "../../redux/posts";
import { useDispatch, useSelector } from "react-redux";
import "./AllPosts.css";

function AllPosts() {
  const dispatch = useDispatch();
  const allPosts = useSelector(selectAllPostsArry)

  useEffect(() => {
    dispatch(thunkGetAllPosts());
  }, [dispatch]);

  if (!allPosts) {
    return (
      <h1>Loading all posts...</h1>
    )
  }

    return (
        <div className="all-post-row">
        <h2 className="all-posts-heading">Your Feed</h2>
        <div className="all-posts">
          {allPosts.length > 0 ? (
            allPosts.map((post) => (
              <div key={post.id} className="all-post-card">
                <Link to={`/posts/${post.id}`} className="all-post-card-link">
                  <img src={post.imageUrl} alt="post image" className="all-post-image" />
                  <div className="all-post-info">
                    <h3 className="all-post-name">{post.username}</h3>
                    <p className="all-post-price">{post.price}</p>
                    <p className="all-post-style">{post.style}</p>
                    <p className="all-post-size">{post.size}</p>
                    <p className="all-post-available">{post.available}</p>
                    <p className="all-post-caption">{post.caption}</p>
                    <p className="all-post-createdAt">{post.createdAt}</p>
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
