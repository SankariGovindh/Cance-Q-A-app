# Side Effects Management
![](/images/backend_architecture_diagram.png)

## Getting Started
1. Install the required packages.
```
pip3 install -r requirements.txt
```
2. Install MySQL workbench from https://dev.mysql.com/downloads/workbench/
3. Create a username and password in MySQL workbench to access the database (https://dev.mysql.com/doc/workbench/en/wb-mysql-connections-navigator-management-users-and-privileges.html). 
4. Navigate to the app/ directory on your local setup. Check that there is a file called 'app.py'
5. Inside 'app.py', update the username and password inside the 'config' object near the top of the file.
6. Fire up a flask server.
```
flask run
```
7. Download Postman from https://www.getpostman.com/downloads/
8. Now you should be able to test API requests via Postman and see any associated changes in MySQL workbench.

## Backend NLP 

The backend NLP folder contains the code that parse the user string. 

1) Read the user string passed as parameter via the API call 
2) Pre-process the query string and find the feature vector 
3) Match similarity with that of the DB content, find the best match 
4) Respond back with the comments corresponding to the best match 

