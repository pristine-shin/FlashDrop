// import React from 'react';
import './RemovePostModal.css';
import '../../context/Modal.css'

const RemovePostModal = ({ postId, onConfirm, onCancel }) => {
  const handleDelete = () => {
    onConfirm(postId);
  };

  return (
    <div className="modal-overlay">
        <div className="modal">
            <div className="modal-header">
                <span>Delete Post?</span>
            </div>
            <div className="confirmation-modal-content">
                <p>Are you sure you want to permanently delete this post?</p>
            </div>
            <div className="modal-buttons">
                <button className="confirm-button" onClick={handleDelete}>Delete Post</button>
                <button className="cancel-button" onClick={onCancel}>Keep Post</button>
            </div>
        </div>
    </div>
  );
};

export default RemovePostModal;
