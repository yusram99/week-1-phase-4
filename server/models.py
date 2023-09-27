from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Define the Restaurant class representing the 'restaurants' table
class Restaurant(db.Model):
    # Set the table name
    __tablename__ = 'restaurants'
    
    # Define columns for the 'restaurants' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the restaurant
    name = db.Column(db.String(50), nullable=False)  # Name of the restaurant, cannot be null
    address = db.Column(db.String(255), nullable=False)  # Address of the restaurant, cannot be null
    
    # Establish a relationship with the 'Pizza' class through the 'restaurant_pizzas' association table
    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas')

# Define the Pizza class representing the 'pizzas' table
class Pizza(db.Model):
    # Set the table name
    __tablename__ = 'pizzas'
    
    # Define columns for the 'pizzas' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the pizza
    name = db.Column(db.String(50), nullable=False)  # Name of the pizza, cannot be null
    ingredients = db.Column(db.String(255), nullable=False)  # Ingredients of the pizza, cannot be null

# Define the RestaurantPizza class representing the 'restaurant_pizzas' association table
class RestaurantPizza(db.Model):
    # Set the table name
    __tablename__ = 'restaurant_pizzas'
    
    # Define columns for the 'restaurant_pizzas' table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the association
    price = db.Column(db.Float, nullable=False)  # Price of the pizza at the restaurant, cannot be null
    
    # Define foreign keys to establish relationships with 'Pizza' and 'Restaurant' tables
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    # Create relationships with 'Pizza' and 'Restaurant' classes
    pizza = db.relationship('Pizza')  # Relationship with the 'Pizza' class
    restaurant = db.relationship('Restaurant')  # Relationship with the 'Restaurant' class
