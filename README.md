## Pizza Restaurant API

The Pizza Restaurant API is a Flask-based web application that allows you to manage pizza restaurants and their menus. You can create, retrieve, update, and delete restaurants and pizzas using this API.

# Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

# Getting Started

These instructions will help you set up and run the Pizza Restaurant API on your local machine for development and testing purposes.

# Prerequisites
To run this project, you need the following:

- Python 3.8 or higher installed on your system.
- [Pip](https://pip.pypa.io/en/stable/) (Python package manager) installed.

# Installation
1. Clone this repository to your local machine:
  `` bash
   git clone https://github.com/yusram99/pizza-restaurant-api.git
2. Change to the project directory:
cd pizza-restaurant-api
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment:
source venv/bin/activate
5. Install the project dependencies:
pip install -r requirements.txt
6. Run the Flask application:
flask run
- The API should now be running locally at http://localhost:5000.

# API Endpoints
The following are the available API endpoints:

GET /restaurants: Retrieve a list of all restaurants.
GET /restaurants/<int:id>: Retrieve details for a specific restaurant by ID.
DELETE /restaurants/<int:id>: Delete a restaurant by ID.
GET /pizzas: Retrieve a list of all pizzas.
POST /restaurant_pizzas: Create a new restaurant pizza entry.

# Testing
You can test the API endpoints using tools like Postman.

# Contributing
If you would like to contribute to this project, please contact me on github.

# License
This project is licensed under the MIT License
