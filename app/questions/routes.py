# questions/routes.py
from flask import Blueprint, request, make_response, jsonify
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from ..models import Question, Comment, User
from datetime import datetime
from flask_login import login_required
from .. import db


# set up a blueprint
questions_bp = Blueprint("questions_bp", __name__)


@questions_bp.route("/add_question", methods=["POST"])
@login_required
def add_question():
    """Add a question to the database.

    Precondition(s):
    - user_id is not None
    - question_text is not None
    - is_anon is not None
    """

    # get query parameters
    user_id = request.args.get("user_id")
    title = request.args.get("title")
    content = request.args.get("content")
    is_anon = int(request.args.get("is_anonymous"))
    source = request.args.get("source")

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    if user_id is not None and content is not None and is_anon is not None:

        # check if a question with this content exists already
        existing_question = Question.query.filter(Question.content == content).first()
        if existing_question:
            return make_response(f"This question already exists!", 400)

        # check if source was provided
        if source is None or len(source) == 0:
            source = "SideEffects App" # default source

        # create new question object
        new_question = Question(user_id=user_id,
                        title=title,
                        content=content,
                        date_created=datetime.now(),
                        date_updated=datetime.now(),
                        is_anonymous=is_anon,
                        source=source,
                        num_comments=0)
        db.session.add(new_question) # adds a new question to the database
        db.session.commit() # commit all changes to the database
        response = {
            "message": f"Question successfully created!",
            "success": True
        }
        return jsonify(response), 200, headers

    # return make_response(f"Unable to create question due to missing information!", 400)
    response = {
        "message": f"Unable to create question due to missing information!",
        "success": False
    }
    return jsonify(response), 200, headers


@questions_bp.route("/get_question", methods=["GET"])
@login_required
def get_question():
    """Return a question from the database with id 'question_id' in JSON format.

    Returns a JSON response containing the question text of the given question_id.
    """

    # get query parameters
    question_id = request.args.get("question_id")

    # query for question
    question = Question.query.get(question_id)

    # format response
    response = []
    response.append({
        "question_id": question_id,
        "question_user_id": question.user_id,
        "question_title": question.title,
        "question_content": question.content,
        "question_date_updated": question.date_updated,
        "question_source": question.source,
        "question_is_anon": question.is_anonymous,
        "question_num_comments": question.num_comments,
        "message": "Successfully retrieved question.",
        "success": True
    })

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    return jsonify(response), 200, headers


@questions_bp.route("/get_recent_questions", methods=["GET"])
@login_required
def get_recent_questions():
    """Return a JSON object of the top 10 most recently updated questions FAQs."""

    # get top 10 questions from database (what metric defines a FAQ?)
    recent_qs = Question.query.order_by(desc(Question.date_updated)).limit(10).all()

    # construct response
    response = []
    for question in recent_qs:

        question_id = question.question_id
        # check if the question is from Facebook
        if question.user_id == 0:
            q_username = "Facebook"
        else:
            q_user = User.query.filter_by(user_id=question.user_id).first()
            q_username = q_user.username

        # get comments associated with the question_id
        comments = Comment.query.filter_by(question_id=question_id).all()
        comment_user_id = []
        comment_username = []
        comment_content = []
        comment_source = []
        comment_is_anon = []
        comment_date_updated = []
        for comment in comments:
            # check if the comment is from Facebook group
            if comment.user_id == 0:
                c_username = "Facebook"
            else:
                # get the user for that comment
                c_user = User.query.filter_by(user_id=comment.user_id).first()
                c_username = c_user.username
            comment_user_id.append(comment.user_id)
            comment_username.append(c_username)
            comment_content.append(comment.content)
            comment_source.append(comment.source)
            comment_is_anon.append(comment.is_anonymous)
            comment_date_updated.append(comment.date_updated)

        # add question data into response
        response.append({
            "id": question.question_id,
            "question_user_id": question.user_id,
            "question_username": q_username,
            "question_title": question.title,
            "question_date_updated": question.date_updated,
            "question_source": question.source,
            "question_content": question.content,
            "question_num_comments": question.num_comments,
            "question_is_anon": question.is_anonymous,
            "comment_content": comment_content,
            "comment_source": comment_source,
            "comment_date_updated": comment_date_updated,
            "comment_is_anon": comment_is_anon,
            "comment_user_id": comment_user_id,
            "comment_username": comment_username
        })

    # prepare headers for response
    headers = {"Content-Type": "application/json"}

    return jsonify(response), 200, headers


@questions_bp.route("/delete_question", methods=["DELETE"])
@login_required
def delete_question():
    # get query parameters
    question_id = request.args.get("question_id")

    # check if question_id is None or not
    if question_id is not None:
        # get the question that needs to be deleted
        delete_q = Question.query.filter_by(question_id=question_id).first()
        db.session.delete(delete_q)

        db.session.commit()
        return make_response(f"Question successfully deleted!", 200)
    
    # if question_id is None
    return make_response(f"Unable to delete the question due to missing question_id!", 400)


@questions_bp.route("/update_question", methods=["PUT"])
@login_required
def update_question():
    # get query parameters
    question_id = request.args.get("question_id")
    new_title = request.args.get("title")
    new_content = request.args.get("content")
    is_anon = int(request.args.get("is_anonymous"))

    # check if there is missing variable
    if question_id is not None and new_content is not None and is_anon is not None:
        # get the question that needs to be updated
        update_q = Question.query.filter_by(question_id=question_id).first()
        # update the following fields of the question
        update_q.title = new_title
        update_q.content = new_content
        update_q.date_updated = datetime.now()
        update_q.is_anonymous = is_anon

        db.session.commit()
        return make_response(f"Question successfully updated!", 200)
    
    # if there is missing variable
    return make_response(f"Unable to update the question due to missing information!", 400)


@questions_bp.route("/get_question_history", methods=["GET"])
@login_required
def get_question_history():
    """Return a JSON object of all the questions asked by the user with user_id"""

    # get query parameters
    user_id = request.args.get("user_id")

    if user_id:
        # get all history questions for that user
        all_question = Question.query.filter_by(user_id=user_id).all()

        # construct response
        response = []
        if len(all_question) == 0:
            response = {
                "id": [],
                "question_user_id": [],
                "question_title": [],
                "question_date_updated": [],
                "question_source": [],
                "question_content": [],
                "question_num_comments": [],
                "question_is_anon": [],
                "comment_content": [],
                "comment_source": [],
                "comment_date_updated": [],
                "comment_is_anon": [],
                "comment_user_id": []
            }
        for question in all_question:

            question_id = question.question_id
            # check if the question is from Facebook
            if question.user_id == 0:
                q_username = "Facebook"
            else:
                q_user = User.query.filter_by(user_id=question.user_id).first()
                q_username = q_user.username

            # get comments associated with the question_id
            comments = Comment.query.filter_by(question_id=question_id).all()
            comment_user_id = []
            comment_username = []
            comment_content = []
            comment_source = []
            comment_is_anon = []
            comment_date_updated = []
            for comment in comments:
                # check if the comment is from Facebook group
                if comment.user_id == 0:
                    c_username = "Facebook"
                else:
                    # get the user for that comment
                    c_user = User.query.filter_by(user_id=comment.user_id).first()
                    c_username = c_user.username

                comment_user_id.append(comment.user_id)
                comment_username.append(c_username)
                comment_content.append(comment.content)
                comment_source.append(comment.source)
                comment_is_anon.append(comment.is_anonymous)
                comment_date_updated.append(comment.date_updated)

            # add question data into response
            response.append({
                "id": question.question_id,
                "question_user_id": question.user_id,
                "question_username": q_username,
                "question_title": question.title,
                "question_date_updated": question.date_updated,
                "question_source": question.source,
                "question_content": question.content,
                "question_num_comments": question.num_comments,
                "question_is_anon": question.is_anonymous,
                "comment_content": comment_content,
                "comment_source": comment_source,
                "comment_date_updated": comment_date_updated,
                "comment_is_anon": comment_is_anon,
                "comment_user_id": comment_user_id,
                "comment_username": comment_username
            })

        # prepare headers for response
        headers = {"Content-Type": "application/json"}

        return jsonify(response), 200, headers    
    return make_response(f"Unable to get questions due to missing user_id!", 400)
