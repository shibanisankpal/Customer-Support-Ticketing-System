# ticket_system.py
import streamlit as st
import pandas as pd
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('tickets.db')
c = conn.cursor()

# Create a tickets table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        subject TEXT,
        description TEXT,
        status TEXT DEFAULT 'Open',
        agent_name TEXT,
        feedback TEXT DEFAULT ''
    )
''')
conn.commit()

def create_ticket(customer_name, subject, description):
    c.execute('''
        INSERT INTO tickets (customer_name, subject, description)
        VALUES (?, ?, ?)
    ''', (customer_name, subject, description))
    conn.commit()

def get_all_tickets():
    c.execute('SELECT * FROM tickets')
    return c.fetchall()

def update_ticket(ticket_id, status, agent_name, feedback):
    c.execute('''
        UPDATE tickets
        SET status = ?, agent_name = ?, feedback = ?
        WHERE ticket_id = ?
    ''', (status, agent_name, feedback, ticket_id))
    conn.commit()

def delete_ticket(ticket_id):
    c.execute('''
              DELETE FROM tickets
              WHERE ticket_id = ?
              ''', (ticket_id))
    conn.commit()

def main():
    st.title("Customer Support Ticketing System")

    # User inputs
    customer_name = st.text_input("Customer Name")
    subject = st.text_input("Subject")
    description = st.text_area("Description")

    # Submit ticket
    if st.button("Submit Ticket"):
        create_ticket(customer_name, subject, description)
        st.success("Ticket submitted successfully!")

    # Display all tickets
    st.subheader("All Tickets")
    tickets_df = pd.DataFrame(get_all_tickets(), columns=['Ticket ID', 'Customer Name', 'Subject', 'Description', 'Status', 'Agent Name', 'Feedback'])
    st.dataframe(tickets_df)

    # Update ticket status, agent name, and feedback
    ticket_id = st.number_input("Enter Ticket ID", min_value=1, value=1)
    status = st.selectbox("Select Status", ["Open", "In Progress", "Closed"])
    agent_name = st.text_input("Agent Name (if assigned)")
    feedback = st.text_area("Enter Feedback")

    if st.button("Update"):
        update_ticket(ticket_id, status, agent_name, feedback)
        st.success("Ticket updated successfully!")
        # Reload the ticket data after update
        tickets_df = pd.DataFrame(get_all_tickets(), columns=['Ticket ID', 'Customer Name', 'Subject', 'Description', 'Status', 'Agent Name', 'Feedback'])
        st.dataframe(tickets_df)
    # Delete ticket
    if st.button("Delete Ticket"):
        delete_ticket(ticket_id)
        st.success("Ticket deleted successfully!")
        # Reload the ticket data after deletion
        tickets_df = pd.DataFrame(get_all_tickets(), columns=['Ticket ID', 'Customer Name', 'Subject', 'Description', 'Status', 'Agent Name', 'Feedback'])
        st.dataframe(tickets_df)

if __name__ == "__main__":
    main()


