## Deploy Machine Learning Model into AWS Cloud Servers
----------------------------------------------------

+ In this project, we will build a spam detector using machine learning & launch it as a serverless API using **AWS Elastic Beanstalk** technology.

+ `Amazon Elastic Compute Cloud (Amazon EC2)`, which provides secure, resizable compute capacity in the cloud whereas `AWS Elastic Beanstalk` is an easy-to-use service for deploying and scaling web applications into AWS cloud servers.

+ AWS Elastic Beanstalk Management Console provides a service to set up a Database under the **additional configuration**.

+ "Postman" is an API (application programming interface) development tool which helps to build, test and modify APIs. Almost any functionality that could be needed by any developer is encapsulated in this tool. It has the ability to make various types of HTTP requests(GET, POST, PUT, PATCH), saving environments for later use, converting the API to code for various languages(like JavaScript, Python).

**Task 1: Create a Flask application** -- We first activate the virtual environment inside the application folder by creating 'virtualenv venv' and then activating 'source venv/bin/activate'. In case you want to deactivate this environment, you run 'deactivate'

**Task 2: Create a RESTful API - GET/POST Method **-- We will convert our "Hello world" flask application into RESTful API which handles GET and POST method.

**Task 3: Build a spam detector ML model** -- In this task, we will be building a spam detector model using basic ML techniques.

**Task 4: Build a spam detector API** -- We will convert our "spam detector model" as an API using the flask web app so that we can deploy the API into AWS.

**Task 5: Launch an AWS EC2 instance (Virtual Server) using AWS Elastic Beanstalk** --  We launched an EC2 instance as a virtual cloud server using AWS elastic beanstalk.

**Task 6: Deploy your ML model(API) into AWS virtual servers** -- In this task, we will deploy spam detection API flask application into AWS EC2 instance.  For this, we need to make sure that AWS server correctly resolves project based dependencies such as "Flask", "scikit-learn" etc. into into cloud servers. This is achieved by writing a "requirements.txt" file. This file lists all project based dependencies so that AWS Elastic Beanstalk will install project based dependencies or libraries by looking into this file.

Within exiting the virtual environment created in task 1 write in terminal : `pip3 freeze > requirements.txt`. **Freeze** is a command that allows you to see what modules along with the versions you have installed with the pip command. When you deploy "requirements.txt" along with your codebase into the AWS, it informs the server all those dependencies on to its cloud servers. Technically, AWS will install all dependencies automatically rather than you deploying it manually.

Note :: Flask object name and application name has to match before deploying to AWS.

**Task 7: Perform additional AWS Elastic Beanstalk actions: Application versioning, Server logs, Server performance monitoring & Terminate the server** -- In this task, we will explore other AWS elastic beanstalk options such as App versioning, restarting servers, monitor server performance and how to terminate the server.
