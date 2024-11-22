# **Database Schema**

## `users`

| column name     | data type | details               |
| --------------- | --------- | --------------------- |
| id              | integer   | not null, primary key |
| bio             | string    |                       |
| email           | string    | not null, unique      |
| username        | string    | not null, unique      |
| hashedPassword  | string    | not null, unique      |
| is_artist       | boolean   | not null              |
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
| available   | boolean   | not null, default=true|
| imageUrl    | string    | not null              |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `userId` references `users` table

## `comments`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| content     | string    | not null              |
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
| likesId     | integer   | not null, foreign key |
| createdAt   | datetime  | not null              |

- `postId` references `posts` table
- `likesId` references `likes` table

## `bookings`

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| postId      | integer   | not null, foreign key |
| clientId    | integer   | not null, foreign key |
| artistId    | integer   | not null, foreign key |
| appointment_date | date | not null              |
| deposit     | decimal   | not null              |
| status      | string    | not null, default: "Pending"|
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `postId` references `posts` table
- `clientId` references `users` table if is_artist is `false`
- `artistId` references `users` table if is_artist is `true`

## `messages` JOIN TABLE

| column name | data type | details               |
| ----------- | --------- | --------------------- |
| id          | integer   | not null, primary key |
| senderId    | integer   | not null, foreign key |
| recipientId | integer   | not null, foreign key |
| content     | string    | not null              |
| createdAt   | datetime  | not null              |
| updatedAt   | datetime  | not null              |

- `senderId` references `users` table
- `recipientId` references `users` table


<br><br>
## `Relationships`

* Users → Posts: One-to-Many (artists create multiple posts).

* Posts → Post Images: One-to-Many (each post can have multiple images). (If I do an images table)

* Posts → Comments: One-to-Many (multiple users can comment on a post).

* Posts → Likes: Many-to-Many (a post can have multiple likes, and a user can like multiple posts).

* Posts → Bookings: One-to-Many (clients book for specific posts).

* Users → Messages: Many-to-Many (users send messages to each other).
