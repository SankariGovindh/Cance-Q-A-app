# users/routes.py
from flask import Blueprint, request, make_response, jsonify
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from datetime import datetime
# from flask_login import login_required
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
    password = generate_password_hash(request.args.get("password"))
    email = request.args.get("email") # add email format verification?

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    if first_name and last_name and username and email and password:

        # check if a user with this username or email exists already
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:            
            response = {
                "message": f"{username} ({email}) already exists!",
                "success": False
                        }
            return jsonify(response), 409, headers

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email,
                        date_created=datetime.now()) # create an instance of the User class
        db.session.add(new_user) # adds a new user to the database
        db.session.commit() # commit all changes to the database
    
    response = {
        "message": f"{new_user} successfully created!",
        "success": True
    }
    return jsonify(response), 200, headers    


@users_bp.route("/get_user_info", methods=["GET"])
# @login_required
def get_user_info():
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
# @login_required
def delete_user():
    """Delete user from database.
    
    Precondition: user_id exists in the 'user' table
    """

    # get arguments
    user_id = request.args.get("user_id")

    # delete user
    user = User.query.get(user_id)
    db.session.delete(user)    
    db.session.commit()    
    return make_response(f"{user} successfully deleted.", 200)


@users_bp.route("/update_user", methods=["PUT"])
# @login_required
def update_user():
    """Update details of a user.
    
    Precondition(s):
    - user_id is not null
    """

    # get arguments
    user_id = request.args.get("user_id")
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")

    # get desired user
    user  = User.query.get(user_id)

    # get details about current user in database
    curr_username = user.username
    curr_email = user.email

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    # make sure username don't already exist in database (excluding user's current username)
    if username != curr_username and User.query.filter_by(username=username).count() > 0:
        # return make_response(f"Unable to update user. Username \"{username}\" is already taken.")
        response = {
            "message": f"Unable to update user. Username \"{username}\" is already taken.",
            "success": False
        }
        return jsonify(response), 409

    # make sure email don't already exist in database (excluding user's current email)
    if email != curr_email and User.query.filter_by(email=email).count() > 0:
        # return make_response(f"Unable to update email. \"{email}\" is already associated with another account.")
        response = {
            "message": f"Unable to update email. \"{email}\" is already associated with another account.",
            "success": False
        }
        return jsonify(response), 409

    # update user details
    if len(first_name) != 0 and first_name is not None:
        user.first_name = first_name
    if len(last_name) != 0 and last_name is not None:
        user.last_name = last_name    
    if len(username) != 0 and username is not None:
        user.username = username    
    if len(email) != 0 and email is not None: # add email format verification here or in client-side code?
        user.email = email
    if len(password) != 0 and password is not None:
        user.password = generate_password_hash(password)
    
    # update database entry
    db.session.commit()
    
    # return make_response(f"{user} successfully updated.", 200)
    response = {
        "message": f"{user} successfully updated.",
        "success": True
    }
    return jsonify(response), 200, headers