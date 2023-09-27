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
    # Create a welcome message as a response
    response = make_response('<h1>Welcome to the Pizza Restaurant API!</h1>', 200)
    return response

# Get all restaurants
@app.route('/restaurants', methods=['GET'])  
def get_restaurants():
    # Query all restaurants from the database
    restaurants = Restaurant.query.all()
    # Return a JSON response containing restaurant data
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

# Get a restaurant by id
@app.route('/restaurants/<int:id>', methods=['GET']) 
def get_restaurant(id):
    # Query a restaurant by its id
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # If the restaurant exists, also retrieve its pizzas and return as JSON
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    else:
        # If the restaurant is not found, return a 404 error
        return jsonify({'error': 'Restaurant not found'}), 404

# Delete a restaurant by id
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    # Query and delete a restaurant by its id
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        # Return a 204 No Content response on successful deletion
        return '', 204
    else:
        # If the restaurant is not found, return a 404 error
        return jsonify({'error': 'Restaurant not found'}), 404

# Get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    # Query all pizzas from the database
    pizzas = Pizza.query.all()
    # Return a JSON response containing pizza data
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

# Get a pizza by id
@app.route('/pizzas/<int:id>', methods=['GET']) 
def get_pizza(id):
    # Query a pizza by its id
    pizza = Pizza.query.get(id)
    if pizza:
        # Return a JSON response containing pizza data
        return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
    else:
        # If the pizza is not found, return a 404 error
        return jsonify({'error': 'Pizza not found'}), 404

# Create a restaurant_pizza relationship
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
