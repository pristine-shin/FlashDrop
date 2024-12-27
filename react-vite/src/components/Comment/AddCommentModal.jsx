import { useState } from 'react';
import '../../context/Modal.css';
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
    <div id="modal">
      <div id="modal-background" onClick={onClose}></div>
      <div id="modal-content">
        {/* <h3 className="modal-title">Add a Comment</h3> */}
        <div className="modal-content">
          <textarea
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder="Write your comment here..."
            style={{ width: '100%', height: '80px', padding: '10px' }}
          />
          {errors.comment && <p className="error-message">{errors.comment}</p>}
          <div className="form-group">
            <button onClick={handleSubmit}>Submit</button>
            <button onClick={()=>{
              setErrors({})
              onClose()
            }
            } style={{ backgroundColor: 'gray', marginLeft: '10px' }}>Cancel</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AddCommentModal;
