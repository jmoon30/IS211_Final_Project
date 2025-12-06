# IS211 Final Project – Book Catalogue Web Application

This project is a Flask-based web application that allows a user to keep track of the books they own. After logging in, the user can search for books using an ISBN number through the Google Books API. The application retrieves book information from the API and stores selected details in a local SQLite database. The user can then view their saved books in a table and delete any book from their collection.

The application follows a simple model-view-controller structure using Flask and SQLAlchemy. The database contains two tables: a User table for login credentials and a Book table for storing book information such as title, author, page count, average rating, and the user associated with each book. All data is stored locally using SQLite and SQLAlchemy ORM.

## Features
- User login system
- Search for books by ISBN using the Google Books API
- Store book title, author, page count, and average rating
- Display all saved books in a table
- Delete books from the collection
- Persistent data storage using SQLite

## Technology Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Google Books API
- HTML

## How to Run the Application

1. Open a terminal in the project root directory.
2. Install required packages:
   py -m pip install -r requirements.txt
3. Navigate into the application folder:
   cd book_catalogue
4. Run the application:
   py app.py
5. Open a web browser and go to:
   http://127.0.0.1:5000

## Default Login Credentials
Username: admin  
Password: admin  

## How the Application Works

After logging in, the user is directed to the dashboard where they can enter an ISBN number into the search box. When the user submits the ISBN, the application sends a request to the Google Books API and retrieves the book’s information. The title, author, page count, and average rating are then saved to the database and displayed in a table on the page. The user may delete any book from the list using the delete link provided in the table.

If the application is restarted, previously saved books will still be available because they are stored in the SQLite database.

## Project Structure

IS211_Final_Project  
│  
├── requirements.txt  
├── README.md  
├── .venv  
└── book_catalogue  
    ├── app.py  
    ├── models.py  
    ├── templates  
    │   ├── login.html  
    │   └── dashboard.html  
    └── static  


