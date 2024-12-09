from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Data
menu_items = [
    {"id": 1, "name": "Pizza Margherita", "price": 8.99},
    {"id": 2, "name": "Cheeseburger", "price": 6.99},
    {"id": 3, "name": "Caesar Salad", "price": 5.99},
]

orders = []

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", menu=menu_items)

@app.route("/order", methods=["POST"])
def order():
    data = request.json
    orders.append(data)
    return jsonify({"message": "Order placed successfully!"}), 201

@app.route("/orders")
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True)
