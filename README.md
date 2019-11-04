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

## AWS Setup Details 

Login Details : username : sankares@usc.edu and password : Cancerbase@2019

Project Name : Project_SideEffects

## Connecting to our MySQL DB instance on Amazon RDS
Instructions:
1. Open MySQL Workbench and navigate to the home page (MySQL Connections).
2. Open a new connection.
3. Set the "Hostname" field to inventory-1.cs45dfwrhl7w.us-west-1.rds.amazonaws.com
4. Set the "Port" field to 3306
5. Set the "Username" field to Administrator
6. In the "Password" field, click "Store in Vault ..." and enter Cancerbase2019 as the password.
7. Click OK to connect.

## Setting up Amazon RDS (MySQL)
- The basic building block of Amazon RDS is the DB instance. This environment is where you run your MySQL databases.
### Create a MySQL DB instance
1. [Sign into the AWS Management Console](https://us-east-1.signin.aws.amazon.com/oauth?SignatureVersion=4&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJMOATPLHVSJ563XQ&X-Amz-Date=2019-11-04T23%3A31%3A03.123Z&X-Amz-Signature=ea4b9504e0e7e75bb000928877803887676806a670ec9b37f2ac2f3319e57993&X-Amz-SignedHeaders=host&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&response_type=code&state=hashArgs%23) and open the Amazon RDS console at https://console.aws.amazon.com/rds/
    - IAM user name: Administrator
    - IAM password: Cancerbase2019
2. In the top right corner of the Amazon RDS console, choose the AWS Region in which you wnat to create the DB instance (in our case, this will be N. California).
3. Follow the remaining steps at https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html, step 3.
    - Note (important!): Before you can create or connect to a DB instance, you must complete the tasks in [Setting Up for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html)

### Troubleshooting connection problems 
If you are unable to connect to the MySQL DB instance, it is likely that the VPC (virtual private cloud) is restricting access to your IP address.
- Check out https://medium.com/@ryanzhou7/connecting-a-mysql-workbench-to-amazon-web-services-relational-database-service-36ae1f23d424 to troubleshoot.
    (1) Check that under "Network & Security", "Public accessibility" is set to "Yes" so that you can access from your IP address.
        - NOTE: We will need to remove public accessibility once we deploy to production (and do other VPC-related stuff).    