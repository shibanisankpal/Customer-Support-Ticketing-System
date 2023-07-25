# Customer-Support-Ticketing-System

This project implements a simple Customer Support Ticketing System, allowing users to submit support tickets, and support agents to manage and respond to them. The application is built using Python and Streamlit and utilizes an SQLite database to store ticket data.

## Link to application

## Getting Started
-Clone the repository to your local machine:

git clone https://github.com/shibanisankpal/Customer-Support-Ticketing-System.git
cd Customer-Support-Ticketing-System

-Install the required dependencies:

pip install streamlit pandas sqlite3

-Run the Streamlit app:

streamlit run app.py

The Customer Support Ticketing System application should now be accessible at http://localhost:8501 in your web browser.

Database
The application uses an SQLite database (tickets.db) to store ticket information. The database contains a "tickets" table with columns for Ticket ID, Customer Name, Subject, Description, Status, Agent Name, and Feedback.

Dependencies
Streamlit: A Python library for building web applications with simple Python scripts.
Pandas: A data manipulation library used for displaying ticket data in a tabular format.
SQLite3: A built-in Python library for working with SQLite databases.
