# csv_to_mysql.py
# csv_to_mysql.py adds the raw data from a CSV file to a MySQL database.

import csv
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="justinho",
    passwd="GRIDS",
    database="inventory",
    port=3306
)

cursor = conn.cursor(buffered=True)

filename = "raw_data.csv"
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    print("Adding data to database...")
    for row in csv_reader:
        question_content = row[1]
        comment = row[2]
        date_created = row[3]
        source = row[4]
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if len(source) == 0:
                source = "unknown" # default value for source
            else:
                # check if question exists in database already                
                cursor.execute("SELECT COUNT(*) FROM question WHERE content=%s", (question_content,))                
                count = cursor.fetchone()[0]                

                # add question if it's not already in the database                
                if count == 0:
                    sql = "INSERT INTO question (content, date_created, date_updated, is_anonymous, source, num_comments) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (question_content, date_created, date_created, 1, source, 1)
                    cursor.execute(sql, val)
                    conn.commit()

                # get question_id                
                cursor.execute("SELECT question_id FROM question WHERE content=%s", (question_content,))
                question_id = cursor.fetchone()[0]

                # check if comment exists in database already
                cursor.execute("SELECT COUNT(*) FROM comment WHERE question_id=%s AND content=%s", (question_id, comment,))
                count = cursor.fetchone()[0]
                
                # add comment if it's not already in the database
                if count == 0:                    
                    sql = "INSERT INTO comment (question_id, content, date_created, date_updated, is_anonymous, source) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (question_id, comment, date_created, date_created, 1, source)
                    cursor.execute(sql, val)
                    conn.commit()          

                    # update num_comments of question
                    cursor.execute("SELECT num_comments FROM question WHERE question_id=%s", (question_id,))
                    num_comments = cursor.fetchone()[0]
                    cursor.execute("UPDATE question SET num_comments=%s WHERE question_id=%s", (num_comments+1, question_id,))
                    conn.commit()

    cursor.execute("SELECT COUNT(*) from question")
    count = cursor.fetchone()[0]
    print("number of questions: " + str(count))
    cursor.execute("SELECT COUNT(*) from comment")
    count = cursor.fetchone()[0]
    print("number of comments: " + str(count))
    conn.commit()
    cursor.close()
    print("Successfully added data to database.")
