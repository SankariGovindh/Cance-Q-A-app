# models.py
from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager


class User(UserMixin, db.Model):
    """User class to create User objects to interact with the database.
    
    The User class inherits from the built-in UserMixin class provided by 
    the flask_login module, which provides default implementations for several 
    properties and methods.

    Ref: https://flask-login.readthedocs.io/en/latest/#your-user-class

    Attributes:
        user_id (db.Integer): a unique ID auto-assigned upon user creation
        first_name (db.String): first name of the user
        last_name (db.String): last name of the user
        email (db.String): email of the user
        password (db.String): password of the user
        date_created (db.DateTime): the datetime that the user was created    

    """
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)    
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False) # length 200 to store hashed password
    date_created = db.Column(db.DateTime, default=db.func.now())

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def get_id(self):
        """Override default get_id()."""
        return self.user_id

    def __repr__(self):
        return "<User {}>".format(self.username)    


class Question(db.Model):
    """Question class to create Question objects to interact with the database.
    
    Attributes:
        question_id (db.Integer): a unique ID auto-assigned upon question creation
        user_id (db.Integer): the user ID that created the question
        title (db.String): the title of the question (optional)
        content (db.String): the content of the question
        date_created (db.DateTime): the datetime that the question was created
        date_updated (db.DateTime): the datetime that the question was last updated (e.g. original poster edits question, comment was added, etc.)
        is_anonymous (db.Boolean): True/False whether the poster of the question wants their name to be shown publicly or not
        source (db.String): the source of where the question came from (defaults to 'SideEffects App')
        num_comments (db.Integer): the number of comments contained underneath the question
    
    """
    question_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(200))
    content = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, default=db.func.now())
    is_anonymous = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(25), default="SideEffects App")
    num_comments = db.Column(db.Integer)

    def __repr__(self):
        return "<Question {}>".format(self.content)


class Comment(db.Model):
    """Comment class to create Comment objects to interact with the database.
    
    Attributes:
        comment_id (db.Integer): a unique ID auto-assigned upon comment creation
        user_id (db.Integer): the user ID of the user that created the comment
        question_id (db.Integer): the ID of the question that the comment is associated with
        content (db.String): the content of the comment
        date_created (db.DateTime): the datetime that the comment was created
        date_updated (db.DateTime): the datetime that the comment was last updated
        is_anonymous (db.Boolean): True/False on whether the comment's creator wants to remain anonymous
        source (db.String): the source of the comment (defaults to 'SideEffects App')
    
    """
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, default=db.func.now())
    is_anonymous = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(25), default="SideEffects App")

    def __repr__(self):
        return "<Comment {}>".format(self.content)
