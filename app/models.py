# models.py
from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)    
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False) # length 200 to store hashed password
    date_created = db.Column(db.DateTime, default=db.func.now())
    # cancer_history = db.Column(db.) # SQLAlchemy doesn't have JSON type; https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
    # gender_id = db.Column(db.Integer) # associate gender_id with gender_table?
    # age = db.Column(db.Integer)
    # cancer_type_id = db.Column(db.Integer) # associate cancer_type_id with cancer_type table?
    # treatments = alternative to JSON? # SQLAlchemy doesn't have JSON type; https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(200))
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, default=db.func.now())
    is_anonymous = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(25), default="SideEffects App")
    num_comments = db.Column(db.Integer)

    def __repr__(self):
        return "<Question {}>".format(self.content)


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(750), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, default=db.func.now())
    is_anonymous = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(25), default="SideEffects App")

    def __repr__(self):
        return "<Comment {}>".format(self.content)
