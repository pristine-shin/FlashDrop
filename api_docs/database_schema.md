# **Database Schema**

## `users`

| column name     | data type | details               |
| --------------- | --------- | --------------------- |
| id              | integer   | not null, primary key |
| firstName       | string    | not null              |
| lastName        | string    | not null              |
| bio             | string    |                       |
| email           | string    | not null, unique      |
| username        | string    | not null, unique      |
| hashedPassword  | string    | not null, unique      |
| profileImageUrl | string    | not null              |
| createdAt       | datetime  | not null              |
| updatedAt       | datetime  | not null              |

## `posts`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| style       | string    | not null              |
| size        | string    | not null              |
| price       | decimal   | not null              |
| caption     | string    | not null              |
| available   | boolean   | not null              |
| imageUrl    | string    | not null              |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `userId` references `users` table

## `comments`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| comment     | string    | not null              |
| postId      | integer   | not null, foreign key |
| userId      | integer   | not null, foreign key |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `userId` references `users` table
- `postId` references `posts` table

## `likes`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `userId` references `users` table

## `likes_posts` JOIN TABLE

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| postId      | integer   | not null, foreign key |
| likesId     | integer  | not null, foreign key |
| createdAt   | datetime  | not null              |

- `postId` references `posts` table
- `likesId` references `likes` table

## `carts`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| userId      | integer   | not null, foreign key |
| subtotal    | decimal   | not null              |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `userId` references `users` table

## `carts_products` JOIN TABLE

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| cartId      | integer   | not null, foreign key |
| productId   | integer   | not null, foreign key |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `cartId` references `carts` table
- `productId` references `products` table
