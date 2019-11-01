# Side Effects Management
![](/images/backend_architecture_diagram_103019.png)

## Getting Started
1. Install the required packages.
```
pip3 install -r requirements.txt
```
2. Install MySQL and MySQL workbench from https://dev.mysql.com/downloads/installer/ and https://dev.mysql.com/downloads/workbench/
3. Create a username and password in MySQL workbench to access the database (https://dev.mysql.com/doc/workbench/en/wb-mysql-connections-navigator-management-users-and-privileges.html). 
4. Download Postman from https://www.getpostman.com/downloads/
5. Update your MySQL credentials in ~/app/.env
6. Navigate to the top-level of the project directory.
7. On the command line, type
```
python wsgi.py
```
8. Now you should be able to test API requests via Postman and see any associated changes in MySQL workbench.

## Backend NLP 

The backend NLP folder contains the code that parse the user string. 

1) Read the user string passed as parameter via the API call 
2) Pre-process the query string and find the feature vector 
3) Match similarity with that of the DB content, find the best match 
4) Respond back with the comments corresponding to the best match 
