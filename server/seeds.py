# from models import db, Restaurant, Pizza, RestaurantPizza
# from app import app

# def seed_data():
#     with app.app_context():
#         db.create_all()

#         dominion_pizza = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
#         pizza_hut = Restaurant(name='Pizza Hut', address='123 Main St')
#         margherita = Pizza(name='Margherita', ingredients='Tomato sauce, mozzarella, basil')
#         pepperoni = Pizza(name='Pepperoni', ingredients='Tomato sauce, mozzarella, pepperoni')
#         veggie_lover = Pizza(name='Veggie Lover', ingredients='Tomato sauce, mozzarella, bell peppers, mushrooms, onions')

#         db.session.add_all([dominion_pizza, pizza_hut, margherita, pepperoni, veggie_lover])
#         db.session.commit()

# if __name__ == '__main__':
#     seed_data()


from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

def seed_data():
    with app.app_context():
        db.create_all()

        dominion_pizza = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
        pizza_hut = Restaurant(name='Pizza Hut', address='123 Main St')
        margherita = Pizza(name='Margherita', ingredients='Tomato sauce, mozzarella, basil')
        pepperoni = Pizza(name='Pepperoni', ingredients='Tomato sauce, mozzarella, pepperoni')
        veggie_lover = Pizza(name='Veggie Lover', ingredients='Tomato sauce, mozzarella, bell peppers, mushrooms, onions')

        # Add more restaurants and pizzas here
        another_restaurant = Restaurant(name='Another Restaurant', address='456 Elm St')
        hawaiian = Pizza(name='Hawaiian', ingredients='Tomato sauce, mozzarella, ham, pineapple')
        meat_lover = Pizza(name='Meat Lover', ingredients='Tomato sauce, mozzarella, sausage, bacon, pepperoni')

        db.session.add_all([dominion_pizza, pizza_hut, margherita, pepperoni, veggie_lover, another_restaurant, hawaiian, meat_lover])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
