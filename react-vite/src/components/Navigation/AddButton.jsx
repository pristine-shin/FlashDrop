import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSquarePlus } from '@fortawesome/free-regular-svg-icons';
import "./Navigation.css";

function AddButton() {
  const user = useSelector((store) => store.session.user);

  if (!user) return null;

  return (
    <Link to="/posts/new" className="add-button-link">
      <FontAwesomeIcon icon={faSquarePlus} />
    </Link>
  );
}

export default AddButton;
