import { createSelector } from 'reselect';

const LOAD_ALL_POSTS = 'posts/load_all_posts';
const LOAD_LIMITED_POSTS = 'posts/load_limited_posts';
const LOAD_POST_BY_ID = 'posts/load_post_by_id';
const LOAD_POST_COMMENTS = 'posts/load_post_comments';
const CREATE_POST_COMMENT = 'posts/create_post_comment';
const CREATE_POST = 'posts/create_post';
const DELETE_POST = 'posts/delete_post';
const DELETE_POST_COMMENT = 'posts/delete_post_comment';

//action creators
export const loadAllPosts = posts => (
    {
        type: LOAD_ALL_POSTS,
        posts
    }
)

export const loadLimitedPosts = posts => (
    {
        type: LOAD_LIMITED_POSTS,
        posts
    }
)

export const loadPostById = post => (
    {
        type: LOAD_POST_BY_ID,
        post
    }
)

export const loadPostComments = comments => (
    {
        type: LOAD_POST_COMMENTS,
        comments
    }
)

export const createPostComment = comment => (
    {
        type: CREATE_POST_COMMENT,
        comment
    }
)

export const createPost = post => ({
    type: CREATE_POST,
    post
});

export const deletePost = postId => (
    {
        type: DELETE_POST,
        postId
    }
)

export const deletePostComment = comment => (
    {
        type: DELETE_POST_COMMENT,
        comment
    }
)

//thunk action creators
export const thunkGetAllPosts = () => async dispatch => {
    try {
        const res = await fetch('/api/posts');
        if (res.ok) {
            const posts = await res.json()
            if (posts.errors) return posts.errors
            dispatch(loadAllPosts(posts["posts"]))
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkGetAllPosts:", e);
        return { server: "Something went wrong. Please try again" }
    }
}

export const thunkGetLimitedPosts = (limit = 20) => async dispatch => {
    try {
        const res = await fetch(`/api/posts?limit=${limit}`);
        if (res.ok) {
            const posts = await res.json()
            if (posts.errors) return posts.errors
            dispatch(loadLimitedPosts(posts["posts"]))
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkGetLimitedPosts:", e);
        return { server: "Something went wrong. Please try again" }
    }
}

export const thunkGetPostById = postId => async dispatch => {
    try {
        const res = await fetch(`/api/posts/${postId}`);
        if (res.ok) {
            const post = await res.json()
            if (post.errors) return post.errors
            dispatch(loadPostById(post))
            return post
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkGetPostById:", e);
        return { server: "Something went wrong. Please try again" }
    }
}

export const thunkAddPost = (post) => async dispatch => {
    try {
        const res = await fetch("/api/posts/", {
            method: "POST",
            // headers: { "Content-Type": "application/json" },
            // body: JSON.stringify(post)
            // this is different because of AWS
            body: post
        });
        if (res.ok) {
            const newPost = await res.json();
            dispatch(createPost(newPost));
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkAddPost:", e);
        return { server: "Something went wrong. Please try again" }
    }

};

export const thunkEditPost = (post) => async dispatch => {
    try {
        const postId = post.get("id");

        const editRes = await fetch(`/api/posts/edit/${postId}`,
            {
                method: 'PUT',
                // headers: { 'Content-Type': 'application/json' },
                // body: JSON.stringify(post)
                // this is different because of AWS
                body: post
            }
        )
        if (editRes.ok) {
            const editPost = await editRes.json()
            dispatch(loadPostById(editPost))
        } else if (editRes.status < 500) {
            const errorMessages = await editRes.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        } else {
            console.error("Server Error");
            return { server: "Something went wrong. Please try again" }
        }
    } catch (error) {
        console.error("Error in thunkEditPost:", error);
        return { error: "Something went wrong. Please try again." };
    }
}

export const thunkRemovePost = postId => async dispatch => {
    try {
        const res = await fetch(`/api/posts/${postId}`,
            {
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' }
            }
        )
        if (res.ok) {
            const deleted = await res.json();
            if (deleted.errors) return deleted.errors
            dispatch(deletePost(postId))
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkRemovePost:", e);
        return { server: "Something went wrong. Please try again" }
    }
}

export const thunkGetPostComments = postId => async dispatch => {
    try {
        const res = await fetch(`/api/posts/${postId}/comments`);
        if (!res.ok) throw new Error("Something is wrong in thunk")
        const comments = await res.json()
        if (comments.errors) return comments.errors
        dispatch(loadPostComments(comments['comments']))
        return comments
    } catch (err) {
        console.error(err)
    }
}

export const thunkAddAPostComment = (postId, comment) => async dispatch => {
    try {
        const res = await fetch(`/api/posts/${postId}/comments`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(comment)
        })
        if (res.ok) {
            const newComment = await res.json()
            if (newComment.errors) return newComment.errors
            dispatch(createPostComment(newComment.comment))
            return res
        }
        else if (res.status < 500) {
            const errorMessages = await res.json();
            console.error("Validation Errors:", errorMessages);
            return errorMessages
        }
    } catch (e) {
        console.error("Error in thunkAddAPostComment:", e);
        return { server: "Something went wrong. Please try again" }
    }
}

//selectors
export const selectPost = state => state.posts;
export const selectAllPostsArry = createSelector(selectPost, posts => Object.values(posts.allPosts));
export const selectLtdPostsArry = createSelector(selectPost, posts => Object.values(posts.ltdPosts));

//reducer
const initialState = {
    ltdPosts: {},
    allPosts: {},
    loading: false,
};

function postsReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_ALL_POSTS: {
            const allPosts = {};
            action.posts.forEach(post => allPosts[post.postId] = post)
            return {
                ...state,
                loading: false,
                allPosts,
            };
        }
        case LOAD_LIMITED_POSTS: {
            const ltdPosts = {};
            action.posts.forEach(post => ltdPosts[post.postId] = post)
            return {
                ...state,
                loading: false,
                ltdPosts,
            };
        }
        case LOAD_POST_BY_ID: {
            const post = action.post
            return {
                ...state,
                allPosts: {
                    ...state.allPosts,
                    [post.postId]: post
                },
            };
        }
        case LOAD_POST_COMMENTS: {
            const comments = action.comments;
            const allComments = {}
            let postId;
            if (comments.length > 0) {
                postId = comments[0].postId
                comments.forEach(comment => {
                    allComments[comment.id] = comment
                })
                return {
                    ...state,
                    allPosts: {
                        ...state.allPosts,
                        [postId]: {
                            ...state.allPosts[postId],
                            comments: allComments
                        }
                    }
                }
            }
            return { ...state }
        }
        case CREATE_POST_COMMENT: {
            const { postId } = action.comment
            const comment = action.comment
            const currentComments = state.allPosts[postId]?.comments || {};
            console.log("testing:", state.allPosts[postId].comments)
            return {
                ...state,
                allPosts: {
                    [postId]: {
                        ...state.allPosts[postId],
                        comments: { ...currentComments, [comment.commentId]: comment }
                    }
                }
            }
        }
        case CREATE_POST: {
            const postId = action.post.id;
            return {
                ...state,
                allPosts: {
                    ...state.allPosts,
                    [postId]: action.post
                }
            };
        }
        case DELETE_POST: {
            const { postId } = action
            const copyState = { ...state }
            delete copyState.allPosts[postId]
            if (copyState.ltdPosts[postId]) {
                delete copyState.ltdPosts[postId]
            }
            return copyState
        }

        case DELETE_POST_COMMENT: {
            const { postId, commentId } = action.comment
            const copyState = { ...state }
            delete copyState.allPosts[postId].comments[commentId]
            return copyState
        }
        default:
            return state;
    }
}

export default postsReducer;
