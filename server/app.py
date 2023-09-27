# app.py
from flask import Flask, jsonify, request, make_response
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
db.init_app(app)
migrate = Migrate(app, db)

# Home Page Route
@app.route('/', methods=['GET'])  
def home():
    response = make_response('<h1>Welcome to the Pizza Restaurant API!</h1>', 200)
    return response

# get all restaurants
@app.route('/restaurants', methods=['GET'])  
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

# get restaurants by id
@app.route('/restaurants/<int:id>', methods=['GET']) 
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    
# delete restaurant by id
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    
# get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

# get pizzas by id
@app.route('/pizzas/<int:id>', methods=['GET']) 
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if pizza:
        return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
    else:
        return jsonify({'error': 'Pizza not found'}), 404


# @app.route('/restaurant_pizzas', methods=['POST'])
# def create_restaurant_pizza():
#     data = request.get_json()
#     print(data) 
#     data = request.get_json()
#     price = data.get('price')
#     pizza_id = data.get('pizza_id')
#     restaurant_id = data.get('restaurant_id')


#     if not (price and pizza_id and restaurant_id):
#         return jsonify({'errors': ['validation errors']}), 400

#     pizza = Pizza.query.get(pizza_id)
#     restaurant = Restaurant.query.get(restaurant_id)

#     if not (pizza and restaurant):
#         return jsonify({'errors': ['Pizza or Restaurant not found']}), 400

#     restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)

#     try:
#         db.session.add(restaurant_pizza)
#         db.session.commit()
#         return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'errors': ['validation errors']}), 400


# ...

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    if request.method == 'POST':
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not (price and pizza_id and restaurant_id):
            return jsonify({'errors': ['validation errors']}), 400

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not (pizza and restaurant):
            return jsonify({'errors': ['Pizza or Restaurant not found']}), 400

        restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)

        try:
            db.session.add(restaurant_pizza)
            db.session.commit()
            response_body = {'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}
            response = make_response(
                jsonify(response_body),
                201
            )
            return response
        except Exception as e:
            db.session.rollback()
            return jsonify({'errors': ['validation errors']}), 400



if __name__ == '__main__':
    app.run(debug=True)
