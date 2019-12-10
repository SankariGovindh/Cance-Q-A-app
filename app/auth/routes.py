# auth/routes.py
from flask import Blueprint, redirect, request, make_response, session, url_for, jsonify
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from ..models import User
from .. import db, login_manager


# set up a blueprint
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """User login page.

    Upon GET request, the user is taken to the login page if they are not 
    already logged in. Otherwise, the user is taken to the 'search'/home page.
    Upon POST request, the user is logged in if their credentials are authenticated.
    Otherwise, an error message is returned.

    Returns:
        A JSON response of success/failure of logging in.
    """

    # get query parameters
    message = request.args.get("message")

    # bypass login page if user is already logged in
    print("current_user: " + str(current_user))
    print("Is current user authenticated? " + str(current_user.is_authenticated))

    # prepare headers for response
    headers = {"Content-Type": "application/json"}
    
    if current_user.is_authenticated:        
        next = request.args.get("next") # take users to the page that they had attempted to reach prior to logging in        
        response = {
                "message": "User was already logged in.",
                "success": True,
                "user_id": current_user.user_id
            }         
        return redirect(url_for("questions_bp.get_recent_questions", 
                                user_id=current_user.user_id, 
                                username=current_user.username), code=302)

    # POST: Log in user and take them to FAQs page
    if request.method == "POST":
        # get query arguments
        username = str(request.args.get("username"))
        password = str(request.args.get("password"))        

        # validate login attempt
        user = User.query.filter_by(username=username).first()
        
        if user:            
            if check_password_hash(user.password, password):            
                login_user(user)
                next = request.args.get("next") # take users to the page that they had attempted to reach prior to logging in                
                response = {
                    "message": "Successful login.",
                    "success": True,
                    "user_id": user.user_id
                }                  
                return redirect(url_for("questions_bp.get_recent_questions", 
                                user_id=current_user.user_id, 
                                username=current_user.username), code=302)        

        response = {
            "message": "Invalid username or password.",
            "success": False
        }
        return jsonify(response), 401, headers

    # GET: Take user to login page.
    response = {
        "message": "You have reached the login page.",
        "success": True
    }
    return jsonify(response), 200, headers    


@auth_bp.route("/logout")
@login_required
def logout_page():
    """User logout logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"), code=302)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    response = {
        "message": "",
        "success": False
    }

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    return jsonify(response), 401, headers


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to login page."""    
    return redirect(url_for("auth_bp.login", 
                    message="You must be logged in to view that page."),
                    code=302)