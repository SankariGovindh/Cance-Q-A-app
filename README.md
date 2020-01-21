# Side Effects Management
## Table of Contents
1. [Points of Contact](#poc)
2. [Getting Started](#getting-started)
  - [EC2 Instance](#ec2)
  - [Running Locally](#running-locally)
  - [NLP](#nlp)
  - [Testing Routes](#testing-routes)
  - [Connecting to the MySQL DB instance on Amazon RDS ](#connect-rds)
  - [Migrating Raw Data into MySQL](#migrate-data)
  - [Tech Stack](#tech-stack)
3. [Deep Dive](#deep-dive)
  - [Frontend](#frontend)
  - [Backend](#backend)        

<a name="poc"></a>
### Points of Contact
- Frontend: Kevin Tran (ktran774@usc.edu)
- Backend: Justin Ho (hojustin@usc.edu), Amy Chung (chungy@usc.edu)
- NLP/Search: Sankari Govindarajan (sankares@usc.edu), Sangeeth Koratten (koratten@usc.edu)

<a name="getting-started"></a>
## Getting Started
### Required Software
1. MySQL and MySQL Workbench (https://dev.mysql.com/downloads/installer/ and https://dev.mysql.com/downloads/workbench/)
2. Postman (https://www.getpostman.com/downloads/)
3. Install the required packages.
```
pip3 install -r requirements.txt
```

<a name="ec2"></a>
### EC2 Instance
- ubuntu@18.237.156.136
- Ask Kien Nguyen (kien.nguyen@usc.edu) for the .pem file
- To SSH into the EC2 instance where the server-side code is located at:
```
ssh -i /path/my-key-pair.pem ubuntu@18.237.156.136
```
- For more information, visit https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

<a name="running-locally"></a>
### Running Locally
1. Navigate to the top-level of the project directory.
2. On the command line, type
```
python wsgi.py
```
3. Now you should see something like the following in your terminal.
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 258-984-237
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
4. Now you should be able to test API requests via Postman and see any associated changes in MySQL workbench.

<a name="nlp"></a>
### NLP - /search endpoint
1. Read the user string passed as parameter via the API call 
2. Pre-process the query string and find the tfidf vector 
3. TFIDF values for the questions that are in the database is already pre-calculated and dumped to a .pkl file.
4. Cosine Similarity is found between the user input's TFIDF vector against all the TFIDF vectors present in the JSON file. 
5. Question ID with the highest match is returned back to an internal function, which then pulls the corresponding links and comments from the database and sends back to the frontend app. 

TrainingCode.py - To be executed every time there is a modification in the database. The code generates a pkl file containing the TFIDF matrix, which is then read in the NLPCode and similarity is performed. 

Libraries required : nltk, numpy, cosine_similarity 

<a name="testing-routes"></a>
### Testing Routes using Postman
1. Open PostMan.
2. File -> Import -> "SideEffectsApp(AWS).postman_collection"

<a name="connect-rds"></a>
### Connecting to the MySQL DB instance on Amazon RDS
Instructions:
1. Open MySQL Workbench and navigate to the home page (MySQL Connections).
2. Open a new connection.
3. Set the "Hostname" field to "[Ask Kien Nguyen (kien.nguyen@usc.edu) for URL of Amazon RDS MySQL DB instance]" (excluding quotes)
4. Set the "Port" field to 3306
5. Set the "Username" field to "administrator" (don't include quotes)
6. In the "Password" field, click "Store in Vault ..." and enter "[Ask Kien Nguyen (kien.nguyen@usc.edu) for password]" (don't include quotes) as the password.
7. Click OK to connect.
  
<a name="migrate-data"></a>
### Migrating Raw Data into MySQL
1. Download 1st sheet of the "Raw Data" Google Sheets file in Google Drive as a CSV file and save the file in the /datadump/ directory.
2. In the /datadump/ directory, run 
```
python csv_to_mysql.py
```
3. The database should be updated. In the terminal, you should see the total number of questions and comments that now exist in the database.

<a name="tech-stack"></a>
### Tech Stack
- Frontend:
    - Swift
- Backend:
    - Python3
    - Flask
    - SQLAlchemy
    - Nginx (to route traffic to port 80 of our EC2 instance)

<a name="deep-dive"></a>
## Deep Dive
![](/images/backend_architecture_diagram_103019.png)
<a name="frontend"></a>
### Frontend

#### Description of Files / File Structure
- app
  - SideEffects
  - SideEffects.xcodeproj

<a name="backend"></a>
### Backend
The backend uses a Client-Server architecture model. The Python Flask web framework was used to create an ReST API. SQLAlchemy was used for its ORM (object relational mapper) to make it simple to perform CRUD (create, read, update, delete) operations with our MySQL database. The server-side code is hosted on an AWS EC2 instance, and the MySQL database is hosted on Amazon RDS. 

#### Description of Files / File Structure
- [**app**](app/) (Contains all files regarding backend development)
  - [**auth**](app/auth/) (Contains routes related to authentication)
    - [**routes.py**](app/auth/routes.py)
  - [**comments**](app/comments/) (Contains routes related to the Comment class)
    - [**routes.py**](app/comments/routes.py)
  - [**questions**](app/questions/) (Contains routes related to the Question class)
    - [**routes.py**](app/questions/routes.py)
  - [**users**](app/users/) (Contains routes related to the User class)
    - [**routes.py**](app/users/routes.py)
  - [**__init__.py**](app/__init__.py) (Initialization script that connects all the components of the Flask app, including the SQLAlchemy and LoginManager plug-ins. Also registers all Flask blueprints to link all routes to the application.)
  - [**.env**](app/.env) (Contains our environment variables. Make sure to update the SECRET_KEY!!!)
  - [**config.py**](app/config.py)
  - [**models.py**](app/models.py) (Contains the model classes for User, Question, and Comment.)
  - [**vectorizer.joblib**](app/vectorizer.joblib) (Importing the file as joblib to access large arrays efficiently.)
  - [**vectors.pkl**](app/vectors.pkl) (Pickle file containing the feature vectors for the questions in the database)
- [**datadump**](datadump/) (Contains files regarding data migration)
  - [**csv_to_mysql.py**](datadump/csv_to_mysql.py) (Script that takes raw_data.csv generated from the Google Spreadsheet containing all our data and populates the database with all the data. Don't worry about adding duplicate data upon successive runs of this script. It checks for duplicate data.)
  - [**data_dump_11152019.sql**](datadump/data_dump_11152019.sql) (SQL script to create database tables, along with all data collected so far.)
  - [**raw_data.csv**](datadump/raw_data.csv) (CSV file generated from our Google Spreadsheet. Keep column structure, or else csv_to_mysql.py script won't be able to migrate the latest data to the database.)
- [**images**](images/) (Directory to hold architecture diagrams and other images)  
- [**model**](model/) (Contains files related to the NLP functions used to perform the 'search' function.)
  - [**NLPCode.py**](model/NLPCode.py) (The code gets executed when there is a new query from the user.)
  - [**TrainingCode.py**](model/TrainingCode.py) (Run the code to generate the feature vectors for the question sets that are already available.)
- [**tests**](tests/) (Contains all tests that we've conducted so far.)
  - [**SideEffectsApp(AWS).postman_collection.json**](test/SideEffectsApp(AWS).postman_collection.json) (Contains PostMan tests that the Fall 2019 team conducted. Import this file in Postman to execute tests.)
- [**.gitignore**](.gitignore) (Add sensitive files to .gitignore file to prevent accidental commital of sensitive files to online repository)
- [**README.md**](README.md) (Contains technical documentation. Project motivation and background are contained in a separate Google Doc.)
- [**requirements.txt**](requirements.txt) (Perform 'pip3 install requirements.txt' to install all dependencies in your virtual environment to get started)
- **side-effects-key-pair.pem** (File containing SSH key for AWS EC2 instance. Ask Kien Nguyen (kien.nguyen@usc.edu) for this file (keep this information safe!))
- [**wsgi.py**](wsgi.py) (Entry point to start up the backend server/application. To start the backend application, go to your terminal and type in "python3 wsgi.py")
