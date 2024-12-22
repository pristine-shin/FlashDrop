import { useState, useEffect } from 'react';
import '../../context/Modal.css';
import { thunkEditComment } from '../../redux/comments';
import { useDispatch } from 'react-redux';

const EditCommentModal = ({ comment, onClose, setCurrentComment}) => {
  const [commentText, setCommentText] = useState('');
  const [errors, setErrors] = useState(null);
  const dispatch = useDispatch()

  useEffect(() => {
    if (comment && comment.content) {
      setCommentText(comment.content);
    }
  }, [comment]);

  const handleEdit = async () => {
    setErrors({});
    const res = await dispatch(thunkEditComment(comment.id, { content: commentText }))
    if (res.errors) setErrors(res.errors);
    else {
      setCurrentComment(res)
      onClose()
    }
  };

  return (
    <div id="modal">
      <div id="modal-background" onClick={onClose}></div>
      <div id="modal-content">
        <h3 className="modal-title">Edit Comment</h3>
        <div className="modal-content">
          <textarea
            value={commentText}
            onChange={(e) => setCommentText(e.target.value)}
            placeholder="Edit your comment..."
            style={{ width: '100%', height: '80px', padding: '10px' }}
          />
          {errors && <p className="error-message">{errors.comment}</p>}
          <div className="form-group">
            <button onClick={handleEdit}>Save</button>
            <button onClick={onClose} style={{ backgroundColor: 'gray', marginLeft: '10px' }}>Cancel</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditCommentModal;
