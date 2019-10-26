from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import errorcode

from helpers import connect, create_database, get_datetime
from tables import tables

app = Flask(__name__)

DB_NAME = 'inventory'

# MOVE CONFIGURATION VARIABLES OUT OF THIS FILE
# config = {
#     'user': '<INSERT YOUR USERNAME HERE>',
#     'password': '<INSERT YOUR PASSWORD HERE>',
#     'host': '127.0.0.1',
#     'database': DB_NAME
# }
config = {
    'user': 'justinho',
    'password': 'GRIDS',
    'host': '127.0.0.1',
    'database': DB_NAME
}

@app.route('/get_faqs', methods=['GET'])
def get_faqs():
    """Return a JSON response of the top 10 most frequently asked questions (FAQs)."""

    # connect to database
    print("Retrieving FAQs...")
    conn, cursor = connect(config)

    # get question from database
    query_for_questions = ("SELECT question_id, user_id, title, date_updated, source, num_comments FROM questions LIMIT 10")
    cursor.execute(query_for_questions)

    results_questions = cursor.fetchall()

    # parse result into JSON
    response = {}    
    for result in results_questions:

        question_id = result[1]

        # get comments associated with the question_id
        query_for_comments = ("SELECT comment_id, user_id, comment_text, is_anonymous, source FROM comments WHERE question_id=%s")                
        cursor.execute(query_for_comments, (question_id, ))
        comments_results = cursor.fetchall()
        comments = {}
        for comment in comments_results:
            comment_id, user_id, comment_text, is_anonymous, source = \
                comment[0], comment[1], comment[2], comment[3], comment[4]
            comments[comment_id] = {
                'user_id': user_id,
                'comment_text': comment_text,
                'is_anonymous': is_anonymous,
                'source': source
            }
        
        # add question data into response
        question_id, user_id, title, date_updated, source, num_comments = \
            result[0], result[1], result[2], result[3], result[4], result[5]
        response[question_id] = {
            'question_id': question_id,
            'user_id': user_id,
            'title': title,
            'date_updated': date_updated,
            'source': source,
            'comments': comments,
            'num_comments': num_comments
        }

    # close connection to database
    cursor.close()
    conn.close()

    print("Successfully fetched FAQs.")

    return jsonify(response)


@app.route('/create_user', methods=['POST'])
def create_user():
    """Create a user."""

    print("TODO")


@app.route('/delete_user', methods=['POST'])
def delete_user():
    """Delete user from database."""

    print("TODO")


@app.route('/update_user', methods=['PUT'])
def update_user():
    """Update details of a user."""

    print("TODO")


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


if __name__ == '__main__':

    # create database if database does not already exist
    DB_NAME = 'inventory'
    conn, cursor = connect(config)    
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            print("Database {} created successfully.".format(DB_NAME))
            conn.database = DB_NAME
        else:
            print(err)
            exit(1)
    
    # create tables if they don't already exist in the database
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Creating table {}".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(" already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    
    cursor.close()
    conn.close()
