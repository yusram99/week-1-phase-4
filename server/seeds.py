from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

def seed_data():
    # Create the database tables and initialize the app context
    with app.app_context():
        db.create_all()

        # Create restaurant and pizza objects
        dominion_pizza = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
        pizza_hut = Restaurant(name='Pizza Hut', address='123 Main St')
        margherita = Pizza(name='Margherita', ingredients='Tomato sauce, mozzarella, basil')
        pepperoni = Pizza(name='Pepperoni', ingredients='Tomato sauce, mozzarella, pepperoni')
        veggie_lover = Pizza(name='Veggie Lover', ingredients='Tomato sauce, mozzarella, bell peppers, mushrooms, onions')

        # Add the restaurant and pizza objects to the session
        db.session.add_all([dominion_pizza, pizza_hut, margherita, pepperoni, veggie_lover])

        # Commit the changes to the database
        db.session.commit()

if __name__ == '__main__':
    # Call the seed_data function when the script is executed
    seed_data()
