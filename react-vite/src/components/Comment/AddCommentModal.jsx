import { useState } from 'react';
import '../../context/Modal.css';
import './CommentModal.css';
import { useDispatch } from 'react-redux';
import {
  thunkAddAPostComment,
} from "../../redux/posts";

const AddCommentModal = ({ onClose, setCurrentComment, postId }) => {
  const [commentText, setCommentText] = useState('');
  const [errors, setErrors] = useState({});
  const dispatch = useDispatch()

  const handleSubmit = async () => {
    setErrors({})
    await dispatch(thunkAddAPostComment(postId, { content: commentText })).then(
      async (res) => {
        await res.content ? setErrors(res) : setCurrentComment(res)
      });

    if(commentText) {
      setCurrentComment(commentText)
      setCommentText('');
      onClose();
    }
  };

  return (
    <div id="add-comment-modal">
      <div id="add-comment-modal-background" onClick={onClose}></div>
      <div id="add-comment-modal-content">
        {/* <h3 className="add-comment-modal-title">Add a Comment</h3> */}
        <div className="add-comment-modal-content">
          <textarea
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder="Write your comment here..."
            className='comment-area'
          />
          {errors.comment && <p className="error-message">{errors.comment}</p>}
          <div className="comment-form-group">
            <button className='submit-comment' onClick={handleSubmit}>Submit</button>
            <button className='cancel-comment'
            onClick={()=>{
              setErrors({})
              onClose()
            }}
            // style={{ backgroundColor: 'gray', marginLeft: '10px' }}
            >Cancel</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AddCommentModal;
