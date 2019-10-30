# views.py
from flask import request, make_response
from datetime import datetime
from flask import current_app as app
from .models import db, User, Question, Comment

@app.route("/create_user", methods=["POST"])
def create_user():
    """Create a user."""
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")    
    username = request.args.get("username")
    password = request.args.get("password")
    email = request.args.get("email")    
    if first_name and last_name and username and email and password:

        # make sure a user with this username or email exist already
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f"{username} ({email}) already exists!")

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        username=username,
                        password=password,
                        email=email,
                        date_created=datetime.now()) # create an instance of the User class
        db.session.add(new_user) # adds a new user to the database
        db.session.commit() # commit all changes to the database
    
    headers = {"Content-Type": "application/json"}
    return make_response(f"{new_user} successfully created!", 200)
                        #  200,
                        #  headers=headers)


@app.route('/delete_user', methods=['POST'])
def delete_user():
    """Delete user from database."""

    print("TODO")


@app.route('/update_user', methods=['PUT'])
def update_user():
    """Update details of a user."""

    print("TODO")


@app.route("/get_faqs", methods=["GET"])
def get_faqs():
    """Return a JSON response of the top 10 most frequently asked questions (FAQs)."""

    # connect to database
    print("Retrieving FAQs...")
    conn, cursor = connect(config)

    # get question from database
    query_for_questions = ("SELECT question_id, user_id, title, date_updated, source, num_comments FROM questions LIMIT 10")
    cursor.execute(query_for_questions)

    results_questions = cursor.fetchall()

    # construct response
    response = [] 
    for result in results_questions:

        question_id = result[0]        

        # get comments associated with the question_id
        query_for_comments = ("SELECT comment_id, user_id, comment_text, is_anonymous, source FROM comments WHERE question_id=%s")                
        cursor.execute(query_for_comments, (question_id, ))
        comments_results = cursor.fetchall()        
        comments_text = []
        comments_source = []
        comments_is_anon = []
        comments_user_id = []
        for comment in comments_results:
            comment_id, user_id, comment_text, is_anon, source = \
                comment[0], comment[1], comment[2], comment[3], comment[4]
            comments_text.append(comment_text)
            comments_source.append(source)
            comments_is_anon.append(is_anon)
            comments_user_id.append(user_id)
        
        # add question data into response
        question_id, question_user_id, question_title, date_updated, source, num_comments = \
            result[0], result[1], result[2], result[3], result[4], result[5]
        response.append({
            "question_id": question_id,    
            "question_user_id": user_id,
            "question_title": question_title,
            "question_date_updated": date_updated,
            "question_source": source,            
            "comments_text": comments_text,
            "comments_source": comments_source,
            "comments_is_anon": comments_is_anon,
            "comments_user_id": comments_user_id,
            "num_comments": num_comments
        })

    # close connection to database
    cursor.close()
    conn.close()

    print("Successfully fetched FAQs.")

    return jsonify(response)


@app.route('/add_comment', methods=['POST'])
def add_comment():
    """Add comment to the question thread with id 'question_id'."""

    # get query parameters
    question_id = request.args.get('question_id')
    comment_text = request.args.get('comment_text')
    print("TODO")


@app.route('/get_comments', methods=['GET'])
def get_comments():
    """Return the comments associated with a specified question_id in JSON format.
    
    Precondition(s):
    - question_id is not None
    """
    
    # get query parameters
    question_id = request.args.get('question_id')
    print("TODO")


@app.route('/update_comment', methods=['PUT'])
def update_comment():
    """Update the comment with id 'comment_id' that is associated with the 
    question with id 'question_id'.
    """

    # get query parameters
    question_id = request.args.get('question_id')
    comment_id = request.args.get('comment_id')

    print("TODO")


@app.route('/add_question', methods=['POST'])
def add_question():
    """Add a question to the database.
    
    Precondition(s): 
    - user_id is not None
    - question_text is not None
    - is_anon is not None    
    """

    # get query parameters
    user_id = request.args.get('user_id')
    question_text = request.args.get('question_text')
    is_anon = request.args.get('is_anonymous')
    source = request.args.get('source')

    # connect to database
    conn, cursor = connect(config)

    add_question = ("INSERT INTO questions "
                    "(user_id, title, date_created, date_updated, is_anonymous, source) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
    
    # prepare 'insert' query
    if source is None:
        question_data = (user_id, question_text, get_datetime(), get_datetime(), is_anon, 'Side Effects App')
    else:
        question_data = (user_id, question_text, get_datetime(), get_datetime(), is_anon, source)

    # add question to database
    cursor.execute(add_question, question_data)

    # commit changes to database and close connection
    conn.commit()
    cursor.close()
    conn.close()

    # return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    return jsonify(success=True)


@app.route('/get_question', methods=['GET'])
def get_question():
    """Return a question from the database with id 'question_id' in JSON format.

    Returns a JSON response containing the question text of the given question_id.
    """

    # get query parameters
    question_id = request.args.get('question_id')

    # connect to database
    print("Connecting to db...")
    conn, cursor = connect(config)

    # get question from database
    query = ("SELECT title FROM questions "
             "WHERE question_id=%s")
    cursor.execute(query, (question_id, ))

    # do something with retrieved question
    # for question_text in cursor:
    #     print("{}: {}".format(question_id, question_text))
    result = cursor.fetchone()

    # close connection to database
    cursor.close()
    conn.close()    
    
    return jsonify(result)