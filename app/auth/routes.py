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
# assets = Environment(app)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """User login page."""
    return 1
    # # bypass login page if user is already logged in
    # print("current_user: " + str(current_user))
    # print("Is current user authenticated? " + str(current_user.is_authenticated))
    # if current_user.is_authenticated:
    #     # return redirect(url_for("questions_bp.get_faqs")) # pass Kevin user_id
    #     return     
      
    # # POST: Log in user and take them to FAQs page
    # if request.method == "POST":                                       
    #     # get query arguments
    #     username = request.args.get("username")
    #     password = request.args.get("password")        
        
    #     # validate login attempt
    #     user = User.query.filter_by(username=username).first()        
    #     if user:
    #         if user.check_password(password=password):                
    #             login_user(user)
    #             next = request.args.get("next") # take users to the page that they had attempted to reach prior to logging in
    #             return redirect(next or url_for("questions_bp.get_faqs"))
    #     print("Invalid username or password.") # SEND THIS MESSAGE IN JSON TO FRONTEND
    #     return redirect(url_for("auth_bp.login"))
        
    # # GET: Take user to login page.
    # return redirect(url_for("auth_bp.login"))    


@auth_bp.route("/logout")
@login_required
def logout_page():
    """User logout logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))


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
    print("You must be logged in to view that page.") # SEND THIS MESSAGE IN JSON TO FRONTEND
    return redirect(url_for("auth_bp.login"))


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    """User signup page."""
    signup_form = SignupForm(request.form)
    # POST: Sign up user and take them to the login page.
    if request.method == "POST":
        if signup_form.validate():
            # get form fields
            firstname = request.form.get("firstname")
            lastname = request.form.get("lastname")
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            # check if an account with this email exists already
            existing_user = User.query.filter_by(email=email).first()

            # create user if no account with this username/email exists already
            if existing_user is None:
                new_user = User(firstname=firstname,
                            lastname=lastname,
                            username=username,
                            email=email,
                            password=generate_password_hash(password, method="sha256")
                        )
                db.session.add(new_user)
                db.session.commit()                
                return redirect(url_for("auth_bp.login"))
            print("A user already exists with that username or email.") # SEND THIS MESSAGE IN JSON TO FRONTEND
            return redirect(url_for("auth_bp.signup"))        
            
    # GET: Serve registration page.
    return redirect(url_for("auth_bp.signup"))