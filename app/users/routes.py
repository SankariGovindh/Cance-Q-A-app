# users/routes.py
from flask import Blueprint, request, make_response, jsonify
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from ..models import User
from datetime import datetime
from .. import db


# set up a blueprint
users_bp = Blueprint('users_bp', __name__)


@users_bp.route("/add_user", methods=["POST"])
def add_user():
    """Create a user."""

    # get arguments
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


@users_bp.route("/get_user", methods=["GET"])
def get_user():
    """Get user information."""

    # get arguments
    user_id = request.args.get("user_id")

    # get user info
    user = User.query.get(user_id)

    # construct response
    response = []
    response.append({
        "user_id": user.user_id,                
        "user_first_name": user.first_name,
        "user_last_name": user.last_name,
        "user_username": user.username,
        "user_email": user.email,
        "user_date_created": user.date_created
    })

    return jsonify(response)


@users_bp.route("/delete_user", methods=["DELETE"])
def delete_user():
    """Delete user from database.
    
    Precondition: user_id exists in the 'user' table
    """

    # get arguments
    user_id = request.args.get("user_id")

    # delete user
    user = User.query.get(user_id)
    db.session.delete(user)
    # User.query.filter_by(user_id=user_id).delete()
    db.session.commit()    
    return make_response(f"{user} successfully deleted.", 200)


@users_bp.route("/update_user", methods=["PUT"])
def update_user():
    """Update details of a user."""

    print("TODO")
    return make_response(f"{user} successfully updated.", 200)