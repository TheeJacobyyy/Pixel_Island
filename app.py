from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.secret_key = 'kjasdlslkaslaksdjllkasldj'

products = [
    {'id': 1, 'name': 'Tropical Island', 'price': 500, 'image': '8BitRetreatOne.jpg'},
    {'id': 2, 'name': 'Winter Island', 'price': 750, 'image': 'WinterIsland.jpg'},
    {'id': 3, 'name': 'Lava Island', 'price': 1000, 'image': 'LavaIsland.jpg'},
]
water_sports_section = [
    {'id': 1, 'name': 'Jet Ski', 'description': '1500cc Jet Ski', 'price': 50, 'image': 'JetSki.jpg'},
    {'id': 2, 'name': 'Yacht', 'description': 'Super Sport sails yacht for all your luxury sailing needs', 'price': 150, 'image': 'Yacht.jpg'}
]

@app.route("/")
def index():
    return render_template("index.html", products=products, water_sports_section=water_sports_section)

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

if __name__ == "__main__":
    app.run(debug=True)