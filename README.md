# FlashDrop

FlashDrop is a full-stack web application designed as a social media and booking platform exclusively for tattoo artists and clients. Inspired by platforms like Instagram and Depop, FlashDrop provides a space for artists to showcase their work, connect with clients, and manage their portfolio, without the rest of the noise and distraction the infinite scroll on other platforms. Clients can browse through posts, engage with artists, and explore tattoo inspirations all in one place.

## Features
### Current Features:
* CRUD for Posts: Artists can create, read, update, and delete posts to showcase their tattoos or flash designs.

* CRUD for Comments: Users can leave comments on posts, edit their thoughts, and delete them if needed.

* Authentication: Secure user authentication with login, signup, and demo account access.

### Planned Features:
* Likes: Users will be able to like posts to show their appreciation for artists' work. Their likes will be saved in a "Favorites" page for easy access to their collection of liked posts.
* Bookings: Clients will soon be able to book tattoo appointments directly through the platform.
* Messaging: A direct messaging system will allow clients and artists to communicate seamlessly.


## Live link
https://flashdrop.onrender.com/

## Tech Stack

### Frameworks and Libraries
<div style="display: flex; align-items: center; gap: 10px;">
  <img src="https://img.shields.io/badge/-Python-3776ab?logo=python&logoColor=FFFF66&logoWidth=20" alt="Python" height="25">
  <img src="https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&logoWidth=20" alt="Flask" height="25">
  <img src="https://img.shields.io/badge/-Javascript-41454A?logo=javascript&logoColor=F7DF1E&logoWidth=20" alt="Javascript" height="25">
  <img src="https://img.shields.io/badge/-React-263238?logo=react&logoColor=61DAFB&logoWidth=20" alt="React" height="25">
  <img src="https://img.shields.io/badge/-Redux-764ABC?logo=redux&logoColor=white&logoWidth=20" alt="Redux" height="25">
  <img src="https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white&logoWidth=20" alt="CSS3" height="25">
  <img src="https://img.shields.io/badge/-HTML5-E34F26?logo=HTML5&logoColor=white&logoWidth=20" alt="HTML5" height="25">
</div>

### Database:

<img src="https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white&logoWidth=20" alt="PostgreSQL" height="25">

### Hosting:

<img src="https://img.shields.io/badge/-Render-23c43e?logo=render&logoColor=white&logoWidth=20" alt="Render" height="25">

### Index

[Feature List](https://github.com/pristine-shin/FlashDrop/wiki/Features) | [Database Schema](https://github.com/pristine-shin/FlashDrop/wiki/DB-Schema) | [User Stories](https://github.com/pristine-shin/FlashDrop/wiki/User-Stories)

### Landing Page

![ScreenRecording2025-01-13at10 11 41AM-ezgif com-optimize](https://github.com/user-attachments/assets/aaa59767-ea2f-4b5b-b2ba-b5a6d37aed0d)

### Posts 

![ScreenRecording2025-01-13at11 31 46PM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/875c157e-6259-4ab9-99c8-4f040baeb112)

### Comments

![ScreenRecording2025-01-13at10 55 21AM-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/ca0800ca-4fa7-4e3e-ba06-022dac8c97e4)

### Connect With Me:

[<img align="left" alt="PristineShin | LinkedIn" width="22px" src="./readme-logos/linkedin-logo.png" style="margin: 5px;" />][pristine-linkedin]

[pristine-linkedin]: https://www.linkedin.com/in/pristine-shin/

[<img align="left" alt="ZechariahDominguez | Gmail" width="22px" src="./readme-logos/gmail.png" style="margin: 5px;" />][pristine-email]<br>

[pristine-email]: mailto:shin.pristine@gmail.com



<br></br>

# API Routes

## Users

### User Login

Users can log in using their email or username.

- **Require authentication**: False
- **Request**

  - **Method**: POST
  - **Route path**: /api/auth/login
  - **Body**:
    ```json
    {
      "email_or_username": "user@example.com or username",
      "password": "your_password"
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "username": "username",
      "bio": "example bio here",
      "is_artist": true,
      "profileImageUrl": "exampleprofile.url",
      "createdAt": "2024-10-30 23:51:27",
      "updatedAt": "2024-10-30 23:51:27",
      "posts": ["postList with their info"],
    }
    ```

- **Error Response: Couldn't find user with given credentials**
  - **Status Code**: 404
  - **Body**:

```json
{
  "message": "Login failed. Please check your credentials and try again."
}
```

### User Logout

Users should be able to logout if they are currently logged in

- **Require authentication**: True
- **Request**

  - **Method**: GET
  - **Route path**: /api/auth/logout
  - **Body**: None

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "User logged out"
    }
    ```

### User Signup

Users can create a new account by signing up.

- **Require authentication**: False
- **Request**

  - **Method**: POST
  - **Route path**: /api/auth/signup
  - **Body**:
    ```json
    {
      "username": "desired_username",
      "email": "user@example.com",
      "password": "your_password",
      "is_artist": true,
      "profileImageUrl": "exampleImage.jpeg",
      "bio": "example bio" || "",
      "confirm_password": "your_password"
    }
    ```

- **Successful Response**

  - **Status Code**: 201
  - **Body**:
    ```json
    {
      "id": 21,
      "username": "desired_username",
      "email": "user@example.com",
      "bio": "",
      "is_artist": true,
      "profileImageUrl": "exampleImage.jpeg",
      "createdAt": "2024-11-01 02:12:32",
      "updatedAt": "2024-11-01 02:12:32",
      "posts": []
    }
    ```

- **Error Response: User already exists**
  - **Status Code**: 409
  - **Body**:
    ```json
    {
      "message": "Username or email already exists."
    }
    ```

### User Delete

Users can delete their account.

- **Require authentication**: True
- **Request**

  - **Method**: DELETE
  - **Route path**: /api/users/session
  - **Body**: None

- **Successful Response**

  - **Status Code**: 204
  - **Body**:
    ```json
    {
      "message": "User deleted successfully."
    }
    ```

- **Error Response: User is not authenticated**
  - **Status Code**: 401
  - **Body**:
    ```json
    {
      "message": "Unauthorized"
    }
    ```

### Get Current User

Users can retrieve their own user information. (Profile page)

- **Require authentication**: True
- **Request**

  - **Method**: GET
  - **Route path**: /api/users/session
  - **Body**: None

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "id": 1,
      "username": "current_username",
      "email": "current_user@example.com",
      "bio": "Current user's bio",
      "is_artist": true,
      "profileImageUrl": "currentprofile.url",
      "createdAt": "2024-10-30 23:51:27",
      "updatedAt": "2024-10-30 23:51:27",
      "posts": ["posts list here"]
    }
    ```

- **Error Response: User is not logged in**
  - **Status Code**: 401
  - **Body**:
    ```json
    {
      "message": "Unauthorized"
    }
    ```

## Posts

### Get all Posts

Users should be able to view all Posts.

- **Require authentication**: false
- **Request**
  - **Method**: GET
  - **Route path**: /api/posts
  - **Body**: none
- **Successful Response**

  - **Status Code**: 200
  - **Body**:

    ```json
    {
      "posts": [
        {
          "id": 1,
          "userId": 1,
          "size": "2-3 inches",
          "style": "American Traditional",
          "price": 300,
          "caption": "Caption Here",
          "available": true,
          "imageUrl": "image.url",
          "createdAt": "2024-10-29 18:38:09.043894",
          "updatedAt": "2024-10-29 18:38:09.043894"
        }
        // more posts...
      ]
    }
    ```

### Get details of a Post by id

Return details of a post specified by its id.

- **Require Authentication**: False
- **Request**

  - **Method**: GET
  - **Route path**: /api/post/:postId
  - **Body**: None

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "id": 1,
      "userId": 1,
      "size": "2-3 inches",
      "style": "American Traditional",
      "price": 300,
      "caption": "Caption Here",
      "available": true,
      "imageUrl": "image.url",
      "createdAt": "2024-10-29 18:38:09.043894",
      "updatedAt": "2024-10-29 18:38:09.043894"
    }
    ```

- **Error Response**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post not found!"
    }
    ```

### Get current user's posts

Return details of a post of the current session user. Takes user to their profile page that displays all of their posts.

- **Require Authentication**: True
- **Request**

  - **Method**: GET
  - **Route path**: /api/posts/current
  - **Body**: None

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "userId": 1,
        "size": "2-3 inches",
        "style": "American Traditional",
        "price": 300,
        "caption": "Caption Here",
        "available": true,
        "imageUrl": "image.url",
        "createdAt": "2024-10-29 18:38:09.043894",
        "updatedAt": "2024-10-29 18:38:09.043894"
      },
      {
        // more listed posts
      }
    ]
    ```

- **Error Response**
  - **Status Code**: 401
  - **Body**:
    ```json
    {
      "message": "Unauthorized"
    }
    ```

### Get all Posts by a user's Id

Return all posts by specified user's id. Goes to an individual artists profile page.

- **Require Authentication**: False
- **Request**

  - **Method**: GET
  - **Route path**: /api/posts/:userId
  - **Body**: None

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    [
      {
        "id": 2,
        "userId": 3,
        "size": "5-6 inches",
        "style": "Black and Grey Botanicals",
        "price": 600,
        "caption": "Caption Here",
        "available": false,
        "imageUrl": "image.url",
        "createdAt": "2024-10-29 18:38:09.043894",
        "updatedAt": "2024-10-29 18:38:09.043894"
      },
      {
        // more listed posts
      }
    ]
    ```

- **Error Response - User not found**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Artist not found"
    }
    ```

### Delete an existing post.

Users should be able to delete their Post(s).

- **Require authentication**: True
- **Require proper Authentication: Post must belong to the user**
- **Request**

  - **Method**: DELETE
  - **Route path**: /api/posts/:postId
  - **Body**: None

- **Successful Response**
  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Post successfully deleted"
    }
    ```
- **Error Response: Couldn't find a post by specified id**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post not be found!"
    }
    ```


### Create a Post

Artists (users) should be able to create a Post.

- **Require authentication**: True
- **Validations**: User must be an artist in order to create a post
- **Request**

  - **Method**: POST
  - **Route path**: /api/posts
  - **Body**:
    ```json
    {
      "userId": 3,
      "size": "5-6 inches",
      "style": "Black and Grey Botanicals",
      "price": 600,
      "caption": "Caption Here",
      "available": true,
      "imageUrl": "image.url",
    }
    ```

- **Successful Response**

  - **Status Code**: 201
  - **Body**:
    ```json
    {
      "post": {
        "id": 2,
        "userId": 3,
        "size": "5-6 inches",
        "style": "Black and Grey Botanicals",
        "price": 600,
        "caption": "Caption Here",
        "available": false,
        "imageUrl": "image.url",
        "createdAt": "2024-10-29 18:38:09.043894",
        "updatedAt": "2024-10-29 18:38:09.043894"
      }
    }
    ```

- **Error Response: Body Validation Errors**
  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "userId": "User is required",
        "size": "Size is required",
        "style": "Style is required",
        "price": "Price must be a positive number",
        "caption": "Caption is required",
        "imageUrl": "Image is required"
      }
    }
    ```

### Update and Return existing Post

Users should be able to update their Post(s).

- **Require authentication**: True
- **Require proper Authentication: Post must belong to the user**
- **Request**

  - **Method**: Put
  - **Route path**: /api/posts/:postId
  - **Body**:
    ```json
    {
      "userId": 3,
      "size": "5-6 inches",
      "style": "Black and Grey Botanicals",
      "price": 700,
      "caption": "Edited caption Here",
      "available": false,
      "imageUrl": "image.url",
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "post": {
        "id": 2,
        "userId": 3,
        "size": "5-6 inches",
        "style": "Black and Grey Botanicals",
        "price": 600,
        "caption": "Caption Here",
        "available": false,
        "imageUrl": "image.url",
        "createdAt": "2024-10-29 18:38:09.043894",
        "updatedAt": "2024-10-29 18:38:09.043894"
      }
    }
    ```

- **Error Response: Body Validation Errors**
  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "userId": "User is required",
        "size": "Size is required",
        "style": "Style is required",
        "price": "Price must be a positive number",
        "caption": "Caption is required",
        "imageUrl": "Image is required"
      }
    }
    ```
- **Error Response: Couldn't find a post by specified id**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post could not be found!"
    }
    ```


## Comments

### Get all comments by post's id

Users should be able to view all comments on a Post.

- **Require authentication**: False
- **Request**
  - **Method**: GET
  - **Route path**: /api/posts/:postId/comments
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "comments": [
        {
          "id": 1,
          "postId": 1,
          "userId": 1,
          "content": "Ooooh so sick!",
          "createdAt": "2024-11-29 19:38:09.043894",
          "updatedAt": "2024-11-29 19:38:09.043894",
          "username": "siiickdude",
          "profileImageUrl": "example_profile_pic.jpg"
        }
        // more comments...
      ]
    }
    ```

- **Error Response: Couldn't find a post by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post could not be found!"
    }
    ```

### Create and return a comment for a post by id

Users should be able to create a comment for a Post.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/posts/:postId/comments
  - **Body**:
    ```json
    {
      "comment": "Need to get this!!"
    }
    ```

- **Successful Response**

  - **Status Code**: 201
  - **Body**:
    ```json
    {
      "comment": {
        "id": 2,
        "postId": 2,
        "userId": 1,
        "content": "Need to get this!!",
        "createdAt": "2024-11-29 19:38:09.043894",
        "updatedAt": "2024-11-29 19:38:09.043894"
      }
    }
    ```

- **Error Response: Body Validation Errors**

  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "comment": "Comment is required"
      }
    }
    ```

- **Error Response: Couldn't find a post by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post could not be found"
    }
    ```

- **Error Response: Comment from the current user already exists for the Post**

  - **Status Code**: 500
  - **Body**:
    ```json
    {
      "message": "User already has a comment for this post"
    }
    ```

### Update and return an existing comment

Users should be able to update their comment for a Post.

- **Require authentication**: True
- **Request**

  - **Method**: Put
  - **Route path**: /api/comments/:commentId
  - **Body**:
    ```json
    {
      "comment": "Rex was awesome!! Super kind with a light touch. I love my tattoo!"
    }
    ```

- **Successful Response**
  - **Status Code**: 200
  - **Body**:

```json
{
  "comment": {
    "id": 2,
    "postId": 1,
    "userId": 2,
    "content": "Rex was awesome!! Super kind with a light touch. I love my tattoo!",
    "createdAt": "2024-11-29 19:38:09.043894",
    "updatedAt": "2024-11-29 19:38:09.043894"
  }
}
```

- **Error Response: Body Validation Errors**

  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad Request",
      "errors": {
        "comment": "Comment is required"
      }
    }
    ```

- **Error Response: Couldn't find a post by specified id**

  - **Status Code**: 404
  - **Body**:

    ```json
    {
      "message": "Post could not be found!"
    }
    ```

- **Error Response: User is not logged in**

  - **Status Code**: 403
  - **Body**:
    ```json
    {
      "message": "Requires proper authorization"
    }
    ```

### Delete an existing comment

Users should be able to delete their comment from a post.

- **Require authentication**: True
- **Request**
  - **Method**: DELETE
  - **Route path**: /api/comments/:commentId
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Comment successfully deleted"
    }
    ```

- **Error Response: Couldn't find a comment by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "comment couldn't be found"
    }
    ```

## Likes

### View likes

Users should be able to view all of their liked posts.

- **Require authentication**: True
- **Request**
  - **Method**: GET
  - **Route path**: /api/likes
  - **Body**: None
- **Successful Response**
  - **Status Code**: 200
  - **Body**:

```json
{
  "likes": [
    {
      "postId": 1,
      "userId": 1,
      "size": "2-3 inches",
      "style": "American Traditional",
      "price": 300,
      "caption": "Caption Here",
      "available": true,
      "imageUrl": "image.url",
      "username": "rexxx",
      "createdAt": "2024-10-29 18:38:09.043894",
      "updatedAt": "2024-10-29 18:38:09.043894"
    },
    {
      "postId": 2,
      "userId": 3,
      "size": "5-6 inches",
      "style": "Black and Grey Botanicals",
      "price": 600,
      "caption": "Caption Here",
      "available": false,
      "imageUrl": "image.url",
      "username": "ryanashley",
      "createdAt": "2024-10-29 18:38:09.043894",
      "updatedAt": "2024-10-29 18:38:09.043894"
    }
  ]
}
```

### Add post to likes

Users should be able to like posts. This should increment the number next to the "likes" on the post itself, as well as add the post to the users "likes" page.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/likes
  - **Body**:
    ```json
    {
      "postId": 1
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "post added to the likes",
      "likes": [
        {
          "postId": 1,
          "userId": 1,
          "size": "2-3 inches",
          "style": "American Traditional",
          "price": 300,
          "caption": "Caption Here",
          "available": true,
          "imageUrl": "image.url",
          "createdAt": "2024-10-29 18:38:09.043894",
          "updatedAt": "2024-10-29 18:38:09.043894"
        }
      ]
    }
    ```

- **Error Response: post already exists in likes**
  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Post is already in the likes"
    }
    ```

### Delete post from likes

Users should be able to delete posts from their likes.

- **Request** Authentication: True
- **Request**
  - **Method**: DELETE
  - **Route path**: /api/likes/:postId
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Post removed from the likes"
    }
    ```

- **Error Response**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Post not found in likes"
    }
    ```

## Bookings TBD until requirements complete

## Messages TBD until requirements complete


## Getting started

1. Clone this repository (only this branch).

2. Install dependencies.

   ```bash
   pipenv install -r requirements.txt
   ```

3. Create a __.env__ file based on the example with proper settings for your
   development environment.

4. Make sure the SQLite3 database connection URL is in the __.env__ file.

5. This starter organizes all tables inside the `flask_schema` schema, defined
   by the `SCHEMA` environment variable.  Replace the value for
   `SCHEMA` with a unique name, **making sure you use the snake_case
   convention.**

6. Get into your pipenv, migrate your database, seed your database, and run your
   Flask app:

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

7. To run the React frontend in development, `cd` into the __react-vite__
   directory and run `npm i` to install dependencies. Next, run `npm run build`
   to create the `dist` folder. The starter has modified the `npm run build`
   command to include the `--watch` flag. This flag will rebuild the __dist__
   folder whenever you change your code, keeping the production version up to
   date.
