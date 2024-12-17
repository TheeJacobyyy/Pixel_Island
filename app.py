from flask import Flask, render_template, redirect, request, url_for, session
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'kjasdlslkaslaksdjllkasldj'

BOOKING_FILE = "bookings.json"

products = [
    {'id': 1, 'name': 'Tropical Island', 'description': 'Serene tropical retreat.', 'price': 500, 'image': '8BitRetreatOne.jpg'},
    {'id': 2, 'name': 'Winter Island', 'description': 'A winter wonderland island.', 'price': 750, 'image': 'WinterIsland.jpg'},
    {'id': 3, 'name': 'Lava Island', 'description': 'A warm exotic island with a marvelous volcano.', 'price': 1000, 'image': 'LavaIsland.jpg'},
]
water_sports_section = [
    {'id': 1, 'name': 'Jet Ski', 'description': '1500cc Jet Ski', 'price': 50, 'image': 'JetSki.jpg'},
    {'id': 2, 'name': 'Yacht', 'description': 'Super Sport sails yacht for all your luxury sailing needs', 'price': 150, 'image': 'Yacht.jpg'}
]

def load_bookings():
    try:
        with open(BOOKING_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_bookings(bookings):
    with open(BOOKING_FILE, "w") as file:
        json.dump(bookings, file, indent=4)

@app.route('/')
def index():
    featured_products = [
        {'id': 1, 'name': 'Tropical Island', 'description': 'Serene tropical retreat.', 'price': 500, 'image': '8BitRetreatOne.jpg'},
        {'id': 3, 'name': 'Lava Island', 'description': 'A warm exotic island with a marvelous volcano.', 'price': 1000, 'image': 'LavaIsland.jpg'},
    ]
    return render_template('index.html', products=products, featured_products=featured_products, water_sports_section=water_sports_section)

@app.route("/book/<int:product_id>", methods=["GET", "POST"])
def book(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']

        print(f"Booking for {product['name']} on {date} by {name} ({email})")
        
        return redirect(url_for("index"))

    return render_template("booking.html", product=product)

@app.route('/bookings')
def view_bookings():
    bookings = load_bookings()
    return render_template('bookings.html', bookings=bookings)

@app.route("/product/<int:id>")
def product(id):
    product = next((p for p in products if p['id'] == id), None)
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = [{'product': next(p for p in products if p['id'] == item), 'quantity': quantity} for item, quantity in cart.items()]
    total = sum(product['price'] * quantity for product, quantity in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    if 'cart' not in session:
        session['cart'] = {}
    session['cart'][id] = session['cart'].get(id, 0) + 1
    return redirect('/cart')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)