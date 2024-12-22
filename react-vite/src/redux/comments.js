import { createSelector } from 'reselect';
import { deletePostComment } from './posts'

const LOAD_USER_COMMENTS = 'comments/load_user_comments';
const LOAD_EDITED_COMMENT = 'comments/load_edited_comment';
const DELETE_COMMENT = 'comments/delete_user_comments';

//action creators
export const loadUserComments = comments => (
  {
    type: LOAD_USER_COMMENTS,
    comments
  }
)

export const loadEditedComment = (comment) => (
  {
    type: LOAD_EDITED_COMMENT,
    comment
  }
)

export const deleteComment = commentId => (
  {
    type: DELETE_COMMENT,
    commentId
  }
)

//thunk action creators

export const thunkGetUserComments = () => async dispatch => {
  try {
    const res = await fetch('/api/comments/current');
    if (res.ok) {
      const userComments = await res.json();
      dispatch(loadUserComments(userComments))
    }
    else if (res.status < 500) {
      const errorMessages = await res.json();
      console.error("Validation Errors:", errorMessages);
      return errorMessages
    }
  } catch (e) {
    console.error("Error in thunkGetUserComments:", e);
    return { server: "Something went wrong. Please try again" }
  }
}

export const thunkRemoveComment = (commentId, postId) => async dispatch => {
  try {
    const res = await fetch(`/api/comments/${commentId}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' }
    })

    if (res.ok) {
      dispatch(deleteComment(commentId))
      dispatch(thunkGetUserComments())
      dispatch(deletePostComment({commentId, postId}))
    }
    else if (res.status < 500) {
      const errorMessages = await res.json();
      console.error("Validation Errors:", errorMessages);
      return errorMessages
    }
  } catch (e) {
    console.error("Error in thunkRemoveComment:", e);
    return { server: "Something went wrong. Please try again" }
  }
}

export const thunkEditComment = (commentId, commentText) => async dispatch => {
  try {
    const res = await fetch(`/api/comments/${commentId}`,
      {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(commentText)
      }
    )
    if (res.ok) {
      const editComment = await res.json();
      dispatch(loadEditedComment(editComment))
      return editComment
    }
    else if (res.status < 500) {
      const errorMessages = await res.json();
      console.error("Validation Errors:", errorMessages);
      return {errors: errorMessages}
    }
  } catch (e) {
    console.error("Error in thunkEditComment:", e);
    return { server: "Something went wrong. Please try again" }
  }

}

//selectors
const selectComment = state => state.comments
export const selectUserComments = createSelector(selectComment, comments => comments.userComments);

const initialState = { userComments: {} }

const commentReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_USER_COMMENTS: {
      const userComments = {}
      if (action.comments) {
        const comments = action.comments
        comments.forEach(comment => {
          userComments[comment.id] = comment
        })
        return { ...state, userComments }
      }
      return state
    }
    case LOAD_EDITED_COMMENT: {
      const { comment } = action.comment
      return {
        ...state,
        userComments: {
          ...state.userComments,
          [comment.id]: comment
        }
      }
    }
    case DELETE_COMMENT: {
      const { commentId } = action;
      const copyState = { ...state }
      delete copyState.userComments[commentId]
      return copyState;
    }
    default:
      return state;
  }
}


export default commentReducer;
