# Adam Dobson – T2A2 – Food Recipe API Webserver Project

## [GitHub Repository](https://github.com/dobbbo/FlaskAPI)

## 1. Identification of the problem you are trying to solve by building this particular app.
This app will function as a food recipe sharing service where users can share their favourite food recipes with each other. The client (end user) will have the ability to create, read, update or delete posts related to their recipes. Additionally, users can register and login to their own user profile using their email address and a password, allowing for a more personalised and secure user experience.
The problem that this application looks to solve is to make food recipes easier to find and share. Food preparation is often something that people struggle with, whether it’s due to a lack of time, knowledge or willingness – often leading to ordering unhealthy or expensive food from restaurants. This app will concisely provide the end user with all the ingredients, apparatus and preparation techniques that they will need to prepare their own food at home, leading to less food expenses, a healthier diet and improved cooking skills.

## 2. Why is it a problem that needs solving?
This app is intended to be used like a forum, where users are able to include a relatively open-ended description under their recipe title – as such, users are able to add as much or as little detail about their recipes as they please. This ability to share recipes can immensely fast-track the end-users learning curve when it comes to cooking/preparing their own food at home – helping to make food preparation an easier, more fun and social experience.
The aim of this app is to encourage and enable the preparation of home-cooked/home-prepared meals. There are many reasons why this is a problem that needs solving, namely:
-	A healthier, more mindful diet – by preparing your own food, you are subconsciously more aware of exactly what food and ingredients you are consuming. This places a higher emphasis on users being mindful of what they are putting into their bodies, encouraging a healthier diet.
-	Developing a useful skill – food preparation is a timeless skill that users can benefit from throughout the entirety of their lives, allowing you to prepare food for loved ones, socialise about your recipes, stimulate your brain, or even just prepare yourself a delicious meal.
-	Saving money – instead of paying a premium for constantly ordering food from restaurants, users can find recipes from which the ingredients are sourced from grocery stores, which is far cheaper and therefore helping the user save money.

## 3. Why have you chosen this database system. What are the drawbacks compared to others?
PostgreSQL is a very powerful object-relational database management system, and the system I have chosen to use for this app. I’ve chosen PostgreSQL as it is well known for its good reliability, performance, extensiveness of features and it’s open-sourced nature. PostgreSQL primarily differentiates itself from others due to its emphasis on integrations and extensibility. As PostgreSQL is a relational database, this means it stores its data points in rows, and data attributes in columns. This creates a table that will be used to store multiple related rows, which is perfect for the development of this application.
Here is a list of reasons why I believe PostgreSQL is a good choice for the development of my application:
-	It is an open-source project, therefore allowing the freedom to modify and implement it as needed. You can create your own functions, data types, triggers etc.
-	It is free to use. 
-	Can handle very large amounts of data securely, reliably and with good performance. Good scalability.
-	Large community online, making it easier to find answers to any questions you may have.
-	Relatively easy to install, learn and maintain.
-	Good support from most cloud platforms.
-	Supports JSON.
-	Cross-platform compatibility, runs on many popular operating systems.
-	Can process complex data types. For example, it supports geographic objects and therefore can be used with location-based services.
-	Wide language support (e.g. Python, Perl, Java, C, C++, Perl and more).]
-	Compliant with SQL standard.
-	A wide array of extensions are available, making it highly expandable.
However, when comparing to other database systems, PostgreSQL definitely does have some drawbacks, these being:
-	By default, it is not available on all hosts.
-	Relatively low speed and performance metrics when comparing to other DBMS’, such as MySQL.
-	Some open-source applications may not support PostgreSQL, whereas other DBMS’ such as MySQL has strong support.
-	Had some difficulties installing, configuring and updating.
-	Online documentation is difficult to navigate and understand.
-	Difficulties when running locally.

## 4. Identify and discuss the key functionalities and benefits of an ORM.
Object Relational Mapping (ORM) is a technique used by developers to assist with managing the data stored in a relational database. Through ORM, developers can work with objects which represent their data in a database using an object-oriented approach. ORM enables us to create instances of object, which are mapped directly to the rows in our database table. As a result, we can then execute any CRUD (Create, Read, Update, Delete) operations on our data without needing to use or write any SQL. As the name suggests, ORM provides the developer with a library that enables us to map data to objects. It is this layer of abstraction between the database and the code that makes data a lot easier to work with. ORM therefore means that our application can run independent of the actual database management system being utilised in the backend. Some examples of well known ORM softwares for Python consist of SQLAlchemy (my choice of ORM), SQLObject, Storm, Django and Tryton. Some key benefits of using an Object Relational Mapper includes:
-	Makes working with data easier as we do not need to use any raw SQL commands, we can instead take an object-oriented approach
-	Developers can shift their focus on optimising their code, rather than worrying about SQL issues
-	ORM allows our app to run independently of the actual database, meaning that migrating to another database is far less of a hassle
-	Can improve performance as libraries are typically optimised for this
-	Built-in functionalities allow for higher security and data validity (for example, protection against SQL injection attacks

## 5. Document all endpoints for your API.
Here is a link to all endpoints in my application: https://documenter.getpostman.com/view/23745120/2s8YeuJVzK#f4dc5f2c-1241-4c9e-a1b0-47ee516b92c0

Endpoint 1 – Register New User:

Endpoint 2 – Duplicated Email in Registration:

Endpoint 3 – User Login:

Endpoint 4 – Create a Recipe:

Endpoint 5 – Get a List of All Recipes:

Endpoint 6 – Retrieve Single Recipe by ID:

Endpoint 7 – Update a Recipe:

Endpoint 8 – Delete a Recipe:

## 6. An ERD for your app.
![ERD for Application](docs/ERD.png)

## 7. Detail any third-party services that your app will use.
- Postman
- pgAdmin 4
- GitHub

## 8. Describe your projects models in terms of the relationships they have with each other.

## 9. Discuss the database relations to be implemented in your application.

## 10. Describe the way tasks are allocated and tracked in your project.
Screenshot of Trello board at beginning of project:
![Screenshot of Trello board at beginning of project](docs/Trello_start.png)
Screenshot of Trello board halfway through project:
![Screenshot of Trello board halfway through project](docs/Trello_during.png)
Screenshot of Trello board at end of project:
![Screenshot of Trello board at end of project](docs/Trello_end.png)