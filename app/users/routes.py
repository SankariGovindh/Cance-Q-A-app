# users/routes.py
from flask import Blueprint, request, make_response
from flask import current_app as app
from ..models import User
from datetime import datetime
# from .. import db
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# set up a blueprint
users_bp = Blueprint('users_bp', __name__)


@users_bp.route("/add_user", methods=["POST"])
def add_user():
    """Create a user."""
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    username = request.args.get("username")
    password = request.args.get("password")
    email = request.args.get("email")

    if first_name and last_name and username and email and password:

        # check if a user with this username or email exists already
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f"{username} ({email}) already exists!")

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email,
                        date_created=datetime.now()) # create an instance of the User class
        db.session.add(new_user) # adds a new user to the database
        db.session.commit() # commit all changes to the database

    headers = {"Content-Type": "application/json"}
    return make_response(f"{new_user} successfully created!", 200)
                        #  200,
                        #  headers=headers)


@users_bp.route('/delete_user', methods=['POST'])
def delete_user():
    """Delete user from database."""

    print("TODO")
    return make_response("SAMPLE delete user", 200)


@users_bp.route('/update_user', methods=['PUT'])
def update_user():
    """Update details of a user."""

    print("TODO")