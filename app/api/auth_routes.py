from flask import Blueprint, request
from app.models import User, db, Like #Booking later
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': {'message': 'Unauthorized'}}, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        #check for email or username in the singular field
        email_or_username = form.data['email_or_username']
        password = form.data['password']

        user = User.query.filter((User.email == email_or_username) | (User.username == email_or_username)).first()

        # Add the user to the session, we are logged in!
        if user and user.check_password(password):
            login_user(user)
            return user.to_dict()

        return {'message': "Login failed. Please check your credentials and try again."}, 401

    return form.errors, 401


@auth_routes.route('/logout')
@login_required
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            email=form.data['email'],
            username=form.data['username'],
            password=form.data['password'],
            is_artist=form.data['is_artist'],
        )
        db.session.add(user)
        db.session.commit()

        new_likes = Like(userId=user.id)

        db.session.add(new_likes)
        db.session.commit()

        login_user(user)
        return user.to_dict()

    return form.errors, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': {'message': 'Unauthorized'}}, 401
