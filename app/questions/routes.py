# questions/routes.py
from flask import Blueprint, request, redirect, url_for, jsonify
from flask import current_app as app
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from ..models import Question, Comment, User
from datetime import datetime
from flask_login import login_required
from .. import db

# 'search' method imports
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import joblib
import nltk
import re
import string
import math
import scipy
import string
import json
import pickle
import os

nltk.download("averaged_perceptron_tagger")
nltk.download("stopwords")
nltk.download("wordnet")

# set up a blueprint
questions_bp = Blueprint("questions_bp", __name__)


@questions_bp.route("/add_question", methods=["POST"])
@login_required
def add_question():
    """Add a question to the database.
    """

    # get query parameters
    user_id = request.args.get("user_id")
    title = request.args.get("title")
    content = request.args.get("content")
    is_anon = int(request.args.get("is_anonymous"))
    source = request.args.get("source")

    if user_id is not None and content is not None and is_anon is not None:

        # check if a question with this content exists already
        existing_question = Question.query.filter(Question.content == content).first()
        if existing_question:
            return redirect(url_for("questions_bp.get_recent_questions",
                            user_id=current_user.user_id,
                            username=current_user.username,
                            message="This question already exists!"), code=302)

        # make sure title is not None
        if title is None:
            title = ""

        # check if source was provided
        if source is None or len(source) == 0:
            source = "SideEffects App" # default source

        # create new Question object
        new_question = Question(user_id=user_id,
                        title=title,
                        content=content,
                        date_created=datetime.now(),
                        date_updated=datetime.now(),
                        is_anonymous=is_anon,
                        source=source,
                        num_comments=0)
        db.session.add(new_question) # adds a new Question to the database
        db.session.commit() # commit all changes to the database

        return redirect(url_for("questions_bp.get_recent_questions",
                        user_id=current_user.user_id,
                        username=current_user.username,
                        message="Question successfully created!"), code=302)

    return redirect(url_for("questions_bp.get_recent_questions",
                    user_id=current_user.user_id,
                    username=current_user.username,
                    message="Unable to create question due to missing information."), code=302)


@questions_bp.route("/get_question", methods=["GET"])
@login_required
def get_question():
    """Return JSON response with information of a question.
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
    """Return a JSON response of the 10 most recently updated questions.
    """

    # get query parameters
    user_id = request.args.get("user_id")
    username = request.args.get("username")

    # get most recently updated questions from database
    count = 10
    recent_questions = Question.query.order_by(desc(Question.date_updated)).limit(count).all()

    # construct response
    response = []
    for question in recent_questions:

        question_id = question.question_id

        # check if the question is from Facebook
        if question.user_id == 0:
            question_username = "Facebook"
        else:
            question_user = User.query.filter_by(user_id=question.user_id).first()
            question_username = question_user.username

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
                comment_username.append("Facebook")
            else:
                # get the user for that comment
                comment_user = User.query.filter_by(user_id=comment.user_id).first()
                comment_username.append(comment_user.username)
            comment_user_id.append(comment.user_id)
            comment_content.append(comment.content)
            comment_source.append(comment.source)
            comment_is_anon.append(comment.is_anonymous)
            comment_date_updated.append(comment.date_updated)

        # add question data into response
        response.append({
            "user_id": user_id,
            "username": username,
            "id": question.question_id,
            "question_user_id": question.user_id,
            "question_username": question_username,
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
    """Delete a question from the database.
    """
    # get query parameters
    question_id = request.args.get("question_id")

    # check if question_id is None or not
    if question_id is not None:
        # get the question that needs to be deleted
        question = Question.query.filter_by(question_id=question_id).first()
        db.session.delete(question)

        db.session.commit()
        return redirect(url_for("questions_bp.get_recent_questions",
                            user_id=current_user.user_id,
                            username=current_user.username,
                            message="Question successfully deleted."), code=302)

    return redirect(url_for("questions_bp.get_recent_questions",
                            user_id=current_user.user_id,
                            username=current_user.username,
                            message="Unable to delete the question."), code=302)


@questions_bp.route("/update_question", methods=["PUT"])
@login_required
def update_question():
    """Update a question in the database.
    """
    # get query parameters
    question_id = request.args.get("question_id")
    new_title = request.args.get("title")
    new_content = request.args.get("content")
    is_anon = int(request.args.get("is_anonymous"))

    # check for missing required variables
    if question_id is not None and new_content is not None and is_anon is not None:
        # get the question that needs to be updated
        question = Question.query.filter_by(question_id=question_id).first()

        # update the following fields of the question
        if new_title is not None:
            question.title = new_title
        question.content = new_content
        question.date_updated = datetime.now()
        question.is_anonymous = is_anon

        db.session.commit()
        return redirect(url_for("questions_bp.get_recent_questions",
                                user_id=current_user.user_id,
                                username=current_user.username,
                                message="Question successfully updated."), code=302)

    return redirect(url_for("questions_bp.get_recent_questions",
                    user_id=current_user.user_id,
                    username=current_user.username,
                    message="Unable to update the question due to missing information."), code=302)


@questions_bp.route("/get_question_history", methods=["POST"])
@login_required
def get_question_history():
    """Return a JSON response of all the questions asked by a user.
    """

    # get query parameters
    user_id = request.args.get("user_id")

    if user_id:
        # get all history questions for that user
        all_questions = Question.query.filter_by(user_id=user_id).all()

        # construct response
        response = []

        if len(all_questions) == 0:
            response = [{
                "username": "",
                "user_id": user_id,
                "question_username": "",
                "comment_username": [],
                "id": 0,
                "question_user_id": int(user_id),
                "question_title": "",
                "question_date_updated": "",
                "question_source": "",
                "question_content": "",
                "question_num_comments": 0,
                "question_is_anon": bool(0),
                "comment_content": [],
                "comment_source": [],
                "comment_date_updated": [],
                "comment_is_anon": [],
                "comment_user_id": []
            }]

        for question in all_question:

            question_id = question.question_id

            # check if the question is from Facebook
            if question.user_id == 0:
                question_username = "Facebook"
            else:
                question_user = User.query.filter_by(user_id=question.user_id).first()
                question_username = question_user.username

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
                    comment_username = "Facebook"
                else:
                    # get the user for that comment
                    comment_user = User.query.filter_by(user_id=comment.user_id).first()
                    comment_username = comment_user.username

                comment_user_id.append(comment.user_id)
                comment_username.append(comment_username)
                comment_content.append(comment.content)
                comment_source.append(comment.source)
                comment_is_anon.append(comment.is_anonymous)
                comment_date_updated.append(comment.date_updated)

            # add question data into response
            response.append({
                "username": "",
                "user_id": user_id,
                "id": question.question_id,
                "question_user_id": question.user_id,
                "question_username": question_username,
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
    return redirect(url_for("questions_bp.get_recent_questions",
                            user_id=current_user.user_id,
                            username=current_user.username,
                            message="Invalid user id. Unable to get questions."), code=302)


@questions_bp.route("/search", methods=["POST"])
@login_required
def search():
    """Returns a JSON response containing the most relevant questions for a user's
    search query.
    """
    query = request.args.get("query")
    TOP_K = 5 # get top 5 most relevant questions

    # get file path of .pkl and .joblib files
    dirname = os.path.dirname(os.path.abspath(__file__))
    pkl_file = os.path.join(dirname, "vectors.pkl")
    joblib_file = os.path.join(dirname, "vectorizer.joblib")
    with open(pkl_file, "rb") as f:
        tfidf_matrix, ids = pickle.load(f)
    tfidf_vectorizer = joblib.load(joblib_file)

    # preprocess query
    query = preProcess(query)
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_vectorizer.transform([' '.join(query)])).reshape(-1)
    cosine_similarities = cosine_similarities[cosine_similarities > 0.0]
    if not cosine_similarities.tolist():
        # raise Exception('No similar questions found!!')
        return redirect(url_for("questions_bp.get_recent_questions",
                                message="No similar questions found."), code=302)
    top_k_max_indices = cosine_similarities.argsort()[-TOP_K:][::-1]
    top_k_question_ids = np.array(ids)[top_k_max_indices].tolist() # top_k_question_ids is a list of integers

    # generate response object containing the top k most relevant questions and their comments
    response = []
    for question_id in top_k_question_ids:

        question = Question.query.filter_by(question_id=question_id).first()

        question_user = User.query.filter_by(user_id=question.user_id).first()
        question_username = question_user.username

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
                comment_username.append("Facebook")
            else:
                # get the user for that comment
                comment_user = User.query.filter_by(user_id=comment.user_id).first()
                comment_username.append(comment_user.username)

            comment_user_id.append(comment.user_id)
            # comment_username.append(comment_username)
            comment_content.append(comment.content)
            comment_source.append(comment.source)
            comment_is_anon.append(comment.is_anonymous)
            comment_date_updated.append(comment.date_updated)

        # add question data into response
        response.append({
            "username": "",
            "user_id": "",
            "id": question.question_id,
            "question_user_id": question.user_id,
            "question_username": question_username,
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

    return jsonify(response), 200


@questions_bp.route("/train_model", methods=["GET"])
def train_model():
    """Trains the model that the 'search' function uses to find the most relevant
    questions for a user's search query.
    """

    return redirect(url_for("questions_bp.get_recent_questions",
                            user_id=current_user.user_id,
                            username=current_user.username,
                            message="Model training complete."), code=302)


# function to preprocess a string query for 'search'
def preProcess(query):
    """Preprocess a string query for the 'search' function.

    Args:
        query (string): the string query to preprocess
    
    Returns:
        the processed string query
    """

    # removing punctuation
    def removePunct(non_punctuation):
        non_punctuation = "".join([char for char in query if char not in string.punctuation]) # if character not part of the string.punctuation list store as prossedData
        return non_punctuation

    # tokenizing as separate words
    def tokenize(tokens):
        tokens = re.split('\W+',processedQuery) # tokenizing every word and separating the same using commas
        return tokens

    # removing stopwords
    def removeStopword(cleanData):
        stopwords = nltk.corpus.stopwords.words('english') # storing all the stopwords for the English language
        cleanData = [word for word in cleanData if word not in stopwords]
        return cleanData

    # stemming
    def stemmer(currentData):
        stemming = nltk.PorterStemmer()
        stemmedData = [stemming.stem(word) for word in currentData]
        return stemmedData

    # lemmatizing
    def lemmatizing(currentData):
        lemma = nltk.WordNetLemmatizer()
        lemData = [lemma.lemmatize(word) for word in currentData]
        return lemData

    # part-of-speech tagging
    def posTagging(processedQuery):
        tag = nltk.pos_tag([i for i in processedQuery if i])
        parsed = [word for word,pos in tag if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'JJ' or pos == 'VB')]
        return parsed

    processedQuery = removePunct(query)
    processedQuery = tokenize(processedQuery)
    processedQuery = removeStopword(processedQuery)
    processedQuery = stemmer(processedQuery)
    processedQuery = lemmatizing(processedQuery)
    processedQuery = posTagging(processedQuery)
    return processedQuery
