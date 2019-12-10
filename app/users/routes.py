# users/routes.py
from flask import Blueprint, request, make_response, jsonify
from flask import current_app as app
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from datetime import datetime
from flask_login import login_required
from .. import db


# set up a blueprint
users_bp = Blueprint('users_bp', __name__)


@users_bp.route("/add_user", methods=["POST"])
def add_user():
    """Create a user.

    Returns:
        A JSON response containing a success/failure message.
    """

    # get query parameters
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
                        date_created=datetime.now())
        db.session.add(new_user)
        db.session.commit()

    response = {
        "message": f"{new_user} successfully created!",
        "success": True
    }
    return jsonify(response), 200, headers


@users_bp.route("/get_user_info", methods=["GET"])
@login_required
def get_user_info():
    """Returns a JSON response containing a user's information.

    Returns:
        On success, returns a JSON response containing a user's information. On
        failure, returns a JSON response containing an error message.
    """

    # get query parameters
    user_id = request.args.get("user_id")    
    user = User.query.get(user_id)

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    # get user info if user_id exists in the database
    if user:
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

        return jsonify(response), 200, headers

    # user with user_id does not exist in the database
    response = {
        "message": f"User with user_id {user_id} does not exist in the database. Unable to get user information.",
        "success": False
    }

    return jsonify(response), 400, headers


@users_bp.route("/delete_user", methods=["DELETE"])
@login_required
def delete_user():
    """Delete a user from database.

    Returns:
        A JSON response containing a success/failure message.
    """

    # get query parameters
    user_id = request.args.get("user_id")

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    # delete user if user_id is found
    if user_id:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        response = {
            "message": f"{user} successfully deleted.",
            "success": True
        }

        return jsonify(response), 200, headers

    # user with user_id does not exist in the database
    response = {
        "message": f"User with user_id {user_id} does not exist in the database. Unable to delete.",
        "success": False
    }

    return jsonify(response), 400, headers


@users_bp.route("/update_user", methods=["PUT"])
@login_required
def update_user():
    """Update details of a user.

    Returns:
        A JSON response containing a success/failure message.
    """

    # get query parameters
    user_id = request.args.get("user_id")
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")

    # get desired user
    user  = User.query.get(user_id)

    # prepare headers for response
    headers = {"Content-Type": "application/json"}
    
    # only allow current user to allow their own profile    
    if user_id != current_user.user_id:
        response = {
            "message": f"You are not authorized to update that user profile. Unable to update.",
            "success": False
        }

        return jsonify(response), 400, headers
    
    # update user information is user_id is found
    if user:

        # get details about current user in database
        curr_username = user.username
        curr_email = user.email        

        # update user details
        if len(first_name) != 0 and first_name is not None:
            print("Updating first name...")
            user.first_name = first_name
        if len(last_name) != 0 and last_name is not None:
            print("Updating last name...")
            user.last_name = last_name
        if len(username) != 0 and username is not None:
            print("Updating username...")
            user.username = username
        if len(email) != 0 and email is not None: # add email format verification here or in client-side code?
            print("Updating email...")
            user.email = email
        if len(password) != 0 and password is not None:
            print("Updating password...")
            user.password = generate_password_hash(password)
        
        db.session.commit()
        
        response = {
            "message": f"{user} successfully updated.",
            "success": True
        }
        return jsonify(response), 200, headers

    # user with user_id does not exist in the database
    response = {
        "message": f"User with user_id {user_id} does not exist in the database. Unable to update.",
        "success": False
    }

    return jsonify(response), 400, headers