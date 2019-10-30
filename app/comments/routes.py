# comments/routes.py
from flask import Blueprint, request
from flask import current_app as app
# from .. import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# set up a blueprint
comments_bp = Blueprint('comments_bp', __name__)


@comments_bp.route('/add_comment', methods=['POST'])
def add_comment():
    """Add comment to the question thread with id 'question_id'."""

    # get query parameters
    question_id = request.args.get('question_id')
    comment_text = request.args.get('comment_text')
    print("TODO")


@comments_bp.route('/get_comments', methods=['GET'])
def get_comments():
    """Return the comments associated with a specified question_id in JSON format.

    Precondition(s):
    - question_id is not None
    """

    # get query parameters
    question_id = request.args.get('question_id')
    print("TODO")


@comments_bp.route('/update_comment', methods=['PUT'])
def update_comment():
    """Update the comment with id 'comment_id' that is associated with the
    question with id 'question_id'.
    """

    # get query parameters
    question_id = request.args.get('question_id')
    comment_id = request.args.get('comment_id')

    print("TODO")