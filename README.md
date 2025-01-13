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



### Posts Page



### Connect With Me:

[<img align="left" alt="PristineShin | LinkedIn" width="22px" src="./readme-logos/linkedin-logo.png" style="margin: 5px;" />][pristine-linkedin]

[pristine-linkedin]: https://www.linkedin.com/in/pristine-shin/

[<img align="left" alt="ZechariahDominguez | Gmail" width="22px" src="./readme-logos/gmail.png" style="margin: 5px;" />][pristine-email]<br>

[pristine-email]: mailto:shin.pristine@gmail.com



<br></br>

# Flask React Project

This is the starter for the Flask React project.

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

7. The React frontend has no styling applied. Copy the __.css__ files from your
   Authenticate Me project into the corresponding locations in the
   __react-vite__ folder to give your project a unique look.

8. To run the React frontend in development, `cd` into the __react-vite__
   directory and run `npm i` to install dependencies. Next, run `npm run build`
   to create the `dist` folder. The starter has modified the `npm run build`
   command to include the `--watch` flag. This flag will rebuild the __dist__
   folder whenever you change your code, keeping the production version up to
   date.

## Deployment through Render.com

First, recall that Vite is a development dependency, so it will not be used in
production. This means that you must already have the __dist__ folder located in
the root of your __react-vite__ folder when you push to GitHub. This __dist__
folder contains your React code and all necessary dependencies minified and
bundled into a smaller footprint, ready to be served from your Python API.

Begin deployment by running `npm run build` in your __react-vite__ folder and
pushing any changes to GitHub.

Refer to your Render.com deployment articles for more detailed instructions
about getting started with [Render.com], creating a production database, and
deployment debugging tips.

From the Render [Dashboard], click on the "New +" button in the navigation bar,
and click on "Web Service" to create the application that will be deployed.

Select that you want to "Build and deploy from a Git repository" and click
"Next". On the next page, find the name of the application repo you want to
deploy and click the "Connect" button to the right of the name.

Now you need to fill out the form to configure your app. Most of the setup will
be handled by the __Dockerfile__, but you do need to fill in a few fields.

Start by giving your application a name.

Make sure the Region is set to the location closest to you, the Branch is set to
"main", and Runtime is set to "Docker". You can leave the Root Directory field
blank. (By default, Render will run commands from the root directory.)

Select "Free" as your Instance Type.

### Add environment variables

In the development environment, you have been securing your environment
variables in a __.env__ file, which has been removed from source control (i.e.,
the file is gitignored). In this step, you will need to input the keys and
values for the environment variables you need for production into the Render
GUI.

Add the following keys and values in the Render GUI form:

- SECRET_KEY (click "Generate" to generate a secure secret for production)
- FLASK_ENV production
- FLASK_APP app
- SCHEMA (your unique schema name, in snake_case)

In a new tab, navigate to your dashboard and click on your Postgres database
instance.

Add the following keys and values:

- DATABASE_URL (copy value from the **External Database URL** field)

**Note:** Add any other keys and values that may be present in your local
__.env__ file. As you work to further develop your project, you may need to add
more environment variables to your local __.env__ file. Make sure you add these
environment variables to the Render GUI as well for the next deployment.

### Deploy

Now you are finally ready to deploy! Click "Create Web Service" to deploy your
project. The deployment process will likely take about 10-15 minutes if
everything works as expected. You can monitor the logs to see your Dockerfile
commands being executed and any errors that occur.

When deployment is complete, open your deployed site and check to see that you
have successfully deployed your Flask application to Render! You can find the
URL for your site just below the name of the Web Service at the top of the page.

**Note:** By default, Render will set Auto-Deploy for your project to true. This
setting will cause Render to re-deploy your application every time you push to
main, always keeping it up to date.

[Render.com]: https://render.com/
[Dashboard]: https://dashboard.render.com/
