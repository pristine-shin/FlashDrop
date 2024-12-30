// import React from 'react';
import '../../context/Modal.css';

const RemoveCommentModal = ({ comment, onClose, onConfirm }) => {
  return (
    <div id="modal">
      <div id="modal-background" onClick={onClose}></div>
      <div id="modal-content">
        <h3 className="modal-title" >Are you sure you want to remove this comment?</h3>
        <div className="modal-content">
          <p className='delete-comment-content'>"{comment.content}"</p>
          <div className="comment-form-group">
            <button className='submit-delete-comment' onClick={onConfirm}>Yes, Remove</button>
            <button className='cancel-delete-comment' onClick={onClose} style={{ backgroundColor: 'gray', marginLeft: '10px' }}>Cancel</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RemoveCommentModal;
