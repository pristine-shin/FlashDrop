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
          "postId": 1,
          "userId": 1,
          "size": "2-3 inches",
          "style": "American Traditional",
          "price": 300,
          "caption": "Caption Here",
          "available": true,
          "imageUrl": "image.url"
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
      },
      {
        // more listed products
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

Return all products by specified user's id. Goes to an individual artists profile page.

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
        "productId": 1,
        "name": "Adele - 30",
        "userId": 1,
        "type": "CD",
        "genre": "",
        "price": "14.99",
        "description": "Adele's highly anticipated album showcasing her powerful vocals and emotional lyrics.",
        "imageUrl": ".../seed-images/products/Adele-30(CD).jpg",
        "createdAt": "2024-10-30 23:51:27",
        "updatedAt": "2024-10-30 23:51:27"
      },
      {
        // more listed products
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

### Create a Product

Users should be able to create a Product.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/products
  - **Body**:
    ```json
    {
      "name": "ProductName2",
      "userId": 2,
      "type": "CD",
      "genre": "Rock",
      "price": 4,
      "description": "Description here too",
      "imageUrl": "image.url"
    }
    ```

- **Successful Response**

  - **Status Code**: 201
  - **Body**:
    ```json
    {
      "product": {
        "productId": 2,
        "name": "ProductName2",
        "userId": 2,
        "type": "CD",
        "genre": "Rock",
        "price": 4,
        "description": "Description here too",
        "imageUrl": "image.url"
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
        "name": "Name is required",
        "userId": "User is required",
        "type": "Type is required",
        "price": "Price must be a positive number",
        "description": "Description is required",
        "imageUrl": "Image is required"
      }
    }
    ```

### Update and Return existing Product

Users should be able to update their Product(s).

- **Require authentication**: True
- **Require proper Authentication: Product must belong to the user**
- **Request**

  - **Method**: Put
  - **Route path**: /api/products/:productId
  - **Body**:
    ```json
    {
      "name": "ProductName",
      "userId": 1,
      "type": "CD",
      "genre": "Rock",
      "price": 2,
      "description": "Updated description here",
      "imageUrl": "image.url"
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "product": {
        "productId": 1,
        "name": "ProductName",
        "userId": 1,
        "type": "CD",
        "genre": "Rock",
        "price": 2,
        "description": "Updated description here",
        "imageUrl": "image.url"
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
        "name": "Name is required",
        "userId": "User is required",
        "type": "type is required",
        "price": "Price must be a positive number",
        "description": "Description is required",
        "imageUrl": "Image is required"
      }
    }
    ```
- **Error Response: Couldn't find a product by specified id**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Product could not be found!"
    }
    ```

### Delete an existing product.

Users should be able to delete their Product(s).

- **Require authentication**: True
- **Require proper Authentication: Product must belong to the user**
- **Request**

  - **Method**: DELETE
  - **Route path**: /api/products/:productId
  - **Body**: None

- **Successful Response**
  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Product successfully deleted"
    }
    ```
- **Error Response: Couldn't find a product by specified id**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Product not be found!"
    }
    ```

## Reviews

### Get all reviews by product's id

Users should be able to view all reviews on a Product.

- **Require authentication**: False
- **Request**
  - **Method**: GET
  - **Route path**: /api/products/:productId/reviews
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "reviews": [
        {
          "id": 1,
          "productId": 1,
          "userId": 1,
          "review": "Random comment"
        }
        // more reviews...
      ]
    }
    ```

- **Error Response: Couldn't find a product by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Product could not be found!"
    }
    ```

### Create and return a review for a product by id

Users should be able to create a review for a Product.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/products/:productId/reviews
  - **Body**:
    ```json
    {
      "review": "Random comment"
    }
    ```

- **Successful Response**

  - **Status Code**: 201
  - **Body**:
    ```json
    {
      "review": {
        "id": 2,
        "productId": 1,
        "userId": 2,
        "review": "Random comment"
      }
    }
    ```

- **Error Response: Body Validation Errors**

  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad **Request**",
      "errors": {
        "review": "Review is required"
      }
    }
    ```

- **Error Response: Couldn't find a product by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Product could not be found"
    }
    ```

- **Error Response: Review from the current user already Exists for the Product**

  - **Status Code**: 500
  - **Body**:
    ```json
    {
      "message": "User already has a review for this product"
    }
    ```

### Update and return an existing review

Users should be able to update their review for a Product.

- **Require authentication**: True
- **Request**

  - **Method**: Put
  - **Route path**: /api/reviews/:reviewId
  - **Body**:
    ```json
    {
      "review": "Random updated comment"
    }
    ```

- **Successful Response**
  - **Status Code**: 200
  - **Body**:

```json
{
  "review": {
    "id": 2,
    "productId": 1,
    "userId": 2,
    "review": "Random updated comment"
  }
}
```

- **Error Response: Body Validation Errors**

  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Bad **Request**",
      "errors": {
        "review": "Review is required"
      }
    }
    ```

- **Error Response: Couldn't find a product by specified id**

  - **Status Code**: 404
  - **Body**:

    ```json
    {
      "message": "Product could not be found!"
    }
    ```

  - **Error Response: Couldn't find a product by specified id**

  - **Status Code**: 403
  - **Body**:
    ```json
    {
      "message": "Requires proper authorization"
    }
    ```

### Delete an existing Review

Users should be able to delete their review from a Product.

- **Require authentication**: True
- **Request**
  - **Method**: DELETE
  - **Route path**: /api/reviews/:reviewId
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Review successfully deleted"
    }
    ```

- **Error Response: Couldn't find a review by specified id**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Review couldn't be found"
    }
    ```

## Shopping Cart

### View all products in the cart.

Users should be able to view all products added to their cart.

- **Require authentication**: True
- **Request**
  - **Method**: GET
  - **Route path**: /api/cart
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "cart": {
        "id": 1,
        "products": [
          {
            "productId": 1,
            "name": "ProductName",
            "quantity": 2,
            "price": 2
          }
          // more products in cart
        ]
      }
    }
    ```

- **Error Response: User not logged in**

  - **Status Code**: 401
  - **Body**:
    ```json
    {
      "message": "Unauthorized"
    }
    ```

### Add product to shopping cart

Users should be able to add products to their shopping cart.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/cart
  - **Body**:
    ```json
    {
      "productId": 1,
      "quantity": 2
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Product has been added to cart",
      "cart": {
        "id": 1
        "products": [
          {
            "productId": 1,
            "name": "ProductName",
            "quantity": 2,
            "price": 2
          }
        ]
      }
    }
    ```

- **Error Response: Body Validation Errors**

  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Product not found"
    }
    ```

### Remove product from shopping cart

Users should be able to remove products from their shopping cart.

- **Require authentication**: True
- **Request**
  - **Method**: DELETE
  - **Route path**: /api/cart/:productId
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Product removed from Cart"
    }
    ```

- **Error Response: Can't find product**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Can't find product in Cart"
    }
    ```

### Perform a "transaction"

Users should be able to perform a "transaction" to complete their purchase.

- **Require authentication**: True
- **Request**
  - **Method**: POST
  - **Route path**: /api/cart/checkout
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Your transaction of 19.98 was successful"
    }
    ```

- **Error Response**

  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Your cart is empty"
    }
    ```

## Wishlist

### View wishlist

Users should be able to view all of their wishlisted products.

- **Require authentication**: True
- **Request**
  - **Method**: GET
  - **Route path**: /api/wishlist
  - **Body**: None
- **Successful Response**
  - **Status Code**: 200
  - **Body**:

```json
{
  "wishlist": [
    {
      "productId": 1,
      "productName": "ProductName",
      "userId": 1,
      "price": 2
    },
    {
      "productId": 2,
      "name": "ProductName2",
      "userId": 1,
      "price": 4
    }
  ]
}
```

### Add product to Wishlist

Users should be able to wishlisted products.

- **Require authentication**: True
- **Request**

  - **Method**: POST
  - **Route path**: /api/wishlist
  - **Body**:
    ```json
    {
      "productId": 1
    }
    ```

- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Product added to the wishlist"
      "wishlist": [
        {
          "productId": 1,
          "productName": "ProductName",
          "userId": 2,
          "price": 2
        }
      ]
    }
    ```

- **Error Response: Product already exists in wishlist**
  - **Status Code**: 400
  - **Body**:
    ```json
    {
      "message": "Product is already in the wishlist"
    }
    ```

### Delete product from Wishlist

Users should be able to delete products from their Wishlist.

- **Request** Authentication: True
- **Request**
  - **Method**: DELETE
  - **Route path**: /api/wishlist/:productId
  - **Body**: None
- **Successful Response**

  - **Status Code**: 200
  - **Body**:
    ```json
    {
      "message": "Product removed from the wishlist"
    }
    ```

- **Error Response**
  - **Status Code**: 404
  - **Body**:
    ```json
    {
      "message": "Product not found in wishlist"
    }
    ```
