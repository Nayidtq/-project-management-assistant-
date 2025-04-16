import streamlit as st
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Project Management Assistant",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'projects' not in st.session_state:
    st.session_state.projects = []
if 'events' not in st.session_state:
    st.session_state.events = []

# Function to add a new project
def add_project(name, description, start_date, end_date):
    new_project = {
        'name': name,
        'description': description,
        'start_date': start_date,
        'end_date': end_date,
        'status': 'In Progress'
    }
    st.session_state.projects.append(new_project)

# Function to add a new event
def add_event(title, description, date, time):
    new_event = {
        'title': title,
        'description': description,
        'date': date,
        'time': time
    }
    st.session_state.events.append(new_event)

# Sidebar
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Select a page:",
    ["Projects", "Calendar", "Virtual Assistant"]
)

# Projects Page
if page == "Projects":
    st.title("Project Management")
    
    # Form to add new project
    with st.expander("Add New Project"):
        with st.form("new_project"):
            name = st.text_input("Project Name")
            description = st.text_area("Description")
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("Start Date")
            with col2:
                end_date = st.date_input("End Date")
            
            if st.form_submit_button("Add Project"):
                if name and description:
                    add_project(name, description, start_date, end_date)
                    st.success("Project added successfully!")
                else:
                    st.error("Please complete all fields")
    
    # Projects list
    st.subheader("Active Projects")
    for project in st.session_state.projects:
        with st.expander(f"{project['name']} - {project['status']}"):
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Start Date:** {project['start_date']}")
            st.write(f"**End Date:** {project['end_date']}")

# Calendar Page
elif page == "Calendar":
    st.title("Event Calendar")
    
    # Form to add new event
    with st.expander("Add New Event"):
        with st.form("new_event"):
            title = st.text_input("Event Title")
            description = st.text_area("Description")
            date = st.date_input("Date")
            time = st.time_input("Time")
            
            if st.form_submit_button("Add Event"):
                if title and description:
                    add_event(title, description, date, time)
                    st.success("Event added successfully!")
                else:
                    st.error("Please complete all fields")
    
    # Events list
    st.subheader("Upcoming Events")
    for event in st.session_state.events:
        st.write(f"**{event['title']}**")
        st.write(f"Date: {event['date']} - Time: {event['time']}")
        st.write(f"Description: {event['description']}")
        st.write("---")

# Virtual Assistant Page
else:
    st.title("Virtual Assistant")
    st.write("""
    Welcome to the Project Management Virtual Assistant.
    Please enter your query in the text field below.
    """)
    
    query = st.text_input("How can I help you?")
    if query:
        st.write("Sorry, this functionality is under development. For now, you can use the Projects and Calendar tabs to manage your activities.")
