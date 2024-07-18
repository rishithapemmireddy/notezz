# LetsNote - Note Taking Web App

## Description
LetsNote is a modern note-taking web application built with FastAPI and MongoDB Atlas. FastAPI is a high-performance web framework for building APIs with Python, known for its speed and ease of use. MongoDB Atlas is a fully-managed cloud database service that provides scalable and flexible data storage.


## Features

- **CRUD Operations**: Create, Read, Update, and Delete notes.
- **User Authentication**: Registration and login functionalities.
- **Responsive Design**: Supports different screen sizes.
- **Data Storage**: Uses MongoDB to store notes and user data.

## Technologies Used

- **Backend**: FastAPI
- **Database**: MongoDB Atlas
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2 (for rendering HTML templates)

## Installation

### Prerequisites
- Python 3.8 or higher
- MongoDB Atlas account
- Git

### Setup
To get a local copy up and running, follow these steps:

```sh
# Clone the repository
git clone https://github.com/rishithapemmireddy/Notzz.git

# Navigate to the project directory
cd notzz

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn index:app --reload
or
fastapi dev index.py

# Usage
Copy code
# Example usage
python main.py
