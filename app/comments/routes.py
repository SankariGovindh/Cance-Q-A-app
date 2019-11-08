# comments/routes.py
from flask import Blueprint, request
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from ..models import Question, Comment
from .. import db


# set up a blueprint
comments_bp = Blueprint('comments_bp', __name__)


@comments_bp.route('/add_comment', methods=['POST'])
# @login_required
def add_comment():
    """Add comment to the question thread with id 'question_id'."""

    # get query parameters from the frontend?
    user_id = request.args.get('user_id')
    question_id = request.args.get('question_id')
    content = request.args.get('content')
    date_posted = request.args.get('date_posted')
    date_updated = request.args.get('date_updated')
    is_anon = int(request.args.get('is_anonymous'))
    source = ('source')

    # check if user_id, content, is_anon are None or not
    if user_id is not None and content is not None and is_anon is not None:
        
        # check if source was provided
        if source is None:
            source = "SideEffects App" # default source

        # create new comment object
        new_comment = Comment(user_id=user_id,
                                question_id=question_id,
                                content=content,
                                date_posted=date_posted,
                                date_updated=date_updated,
                                is_anonymous=is_anon,
                                source=source)
        db.session.add(new_comment) # adds a new comment to the database
        db.session.commit() # commit all changes to the database

        ###TODO
        # need to add 1 to "num_comments" column of that question        
        
        return make_response(f"Comment successfully created!", 200)

    return make_response(f"Unable to create a comment due to missing information!", 400) 
    # print("TODO")


@comments_bp.route('/get_comments', methods=['GET'])
# @login_required
def get_comments():
    """Return the comments associated with a specified question_id in JSON format.

    Precondition(s):
    - question_id is not None
    """

    # get query parameters
    question_id = request.args.get('question_id')

    # check if question_is is None or not
    if question_id is not None:
        # get all comments that is from the question_id
        comments = Comment.query.filter_by(question_id=question_id).all()


@comments_bp.route('/update_comment', methods=['PUT'])
def update_comment():
    """Update the comment with id 'comment_id' that is associated with the
    question with id 'question_id'.

    Not sure if we need question_id or not?
    """

    # get query parameters
    # question_id = request.args.get('question_id')
    comment_id = request.args.get('comment_id')
    comment_new = request.args.get('content')
    date_updated = request.args.get('date_updated')
    is_anon = int(request.args.get('is_anonymous'))

    # query the comment that need to be updated
    update = Comment.query.filter_by(comment_id=comment_id)
    # update the following fields for the comment
    update.content = comment_new
    update.date_updated = date_updated
    update.is_anonymous = is_anon

    db.session.commit()
    return make_response(f"Comment successfully updated!", 200)


@comments_bp.route('/delete_comment', methods=['DELETE'])
def delete_comment():
    """Delete the comment with id 'comment_id' that is associated with the
    question with id 'question_id'.
    """

    # get query parameters
    question_id = request.args.get('question_id')
    comment_id = request.args.get('comment_id')

    # query the comment with the id of comment_id
    delete_com = Comment.query.filter_by(comment_id=comment_id)
    # delete the comment from the database
    db.session.delete(delete_com)

    # num_comments in the question table need to subtract 1
    question = Question.query.filter_by(question_id=question_id)
    old_num = question.num_comments # get the current num_comments
    # subtract by 1 and update the num_comments
    question.num_comments = old_num - 1
    
    db.session.commit()
    
    return make_response(f"Comment successfully deleted!", 200)    