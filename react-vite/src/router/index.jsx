import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import HomePage from '../components/Home/HomePage';
import AllPosts from '../components/Post/AllPosts';
import ProfilePage from '../components/UserProfilePage/UserProfile';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "/posts",
        element: <AllPosts />,
      },
      {
        path: "/profile/session",
        element: <ProfilePage />,
      },
    ],
  },
]);
