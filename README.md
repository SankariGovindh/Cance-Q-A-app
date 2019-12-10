# Side Effects Management
![](/images/backend_architecture_diagram_103019.png)

### Points of Contact
- Frontend: Kevin Tran (ktran774@usc.edu)
- Backend: Justin Ho (hojustin@usc.edu), Amy Chung (chungy@usc.edu)
- NLP/Search: Sankari Govindarajan (sankares@usc.edu), Sangeeth Koratten (koratten@usc.edu)


## Getting Started
### Required Software
1. MySQL and MySQL Workbench (https://dev.mysql.com/downloads/installer/ and https://dev.mysql.com/downloads/workbench/)
2. Postman (https://www.getpostman.com/downloads/)
3. Install the required packages.
```
pip3 install -r requirements.txt
```

### EC2 Instance
- ubuntu@18.237.156.136
- Ask Kien Nguyen (kien.nguyen@usc.edu) for the .pem file
- To SSH into the EC2 instance where the server-side code is located at:
```
ssh -i /path/my-key-pair.pem ubuntu@18.237.156.136
```
- For more information, visit https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html


### Running locally
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


### NLP - /search endpoint
1. Read the user string passed as parameter via the API call 
2. Pre-process the query string and find the tfidf vector 
3. TFIDF values for the questions that are in the database is already pre-calculated and dumped to a .pkl file.
4. Cosine Similarity is found between the user input's TFIDF vector against all the TFIDF vectors present in the JSON file. 
5. Question ID with the highest match is returned back to an internal function, which then pulls the corresponding links and comments from the database and sends back to the frontend app. 

TrainingCode.py - To be executed every time there is a modification in the database. The code generates a pkl file containing the TFIDF matrix, which is then read in the NLPCode and similarity is performed. 


### Testing Routes using Postman
1. Open PostMan.
2. File -> Import -> "SideEffectsApp(AWS).postman_collection"


### Connecting to the MySQL DB instance on Amazon RDS
Instructions:
1. Open MySQL Workbench and navigate to the home page (MySQL Connections).
2. Open a new connection.
3. Set the "Hostname" field to "[Ask Kien Nguyen (kien.nguyen@usc.edu) for URL of Amazon RDS MySQL DB instance]" (excluding quotes)
4. Set the "Port" field to 3306
5. Set the "Username" field to "administrator" (don't include quotes)
6. In the "Password" field, click "Store in Vault ..." and enter "[Ask Kien Nguyen (kien.nguyen@usc.edu) for password]" (don't include quotes) as the password.
7. Click OK to connect.
  

### Migrating Raw Data into MySQL
1. Download 1st sheet of the "Raw Data" Google Sheets file in Google Drive as a CSV file and save the file in the /datadump/ directory.
2. In the /datadump/ directory, run 
```
python csv_to_mysql.py
```
3. The database should be updated. In the terminal, you should see the total number of questions and comments that now exist in the database.


### Tech Stack
- Frontend:
    - Swift
- Backend:
    - Python3
    - Flask
    - SQLAlchemy
    - Nginx (to route traffic to port 80 of our EC2 instance)