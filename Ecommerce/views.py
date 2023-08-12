import os
from flask import render_template
from flask import Flask
import json



app = Flask(__name__)

import locale
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

listOfProducts = [
        {"title" : "24-Piece Black Silverware Set with Steak Knives, Black Flatware Set for 4, Food-Grade Stainless Steel Tableware Cutlery Set",
         "price":19.99,
         "image":"cutlery_set.png",
         "id":1},
        
        {"title" : "kelamayi Upgrade Stand Up Broom and Dustpan Set",
         "price":19.19,
         "image":"broom_and_dust_pan_set.png",
         "id":2},
        
        {"title" : "AaoLin USB Desk Fan, Small Fans with CVT Variable Speeds",
         "price":9.99,
         "image":"desk_fan.png",
         "id":3},
        
        {"title" : "DecoBros Kitchen Counter and Cabinet Pan Organizer Shelf Rack, Bronze",
         "price":16.87,
         "image":"pots.png",
         "id":4},
        
        {"title" : "Home Hero 11-Pcs Kitchen Knife Set with Sheath and 2-Stage Knife Sharpener - Ultra-Sharp High Carbon Stainless Steel Knives Set for Kitchen with Ergonomic Handle (11 Pc Set, Black)",
         "price":19.99,
         "image":"knife_set.png",
         "id":5}

    ]

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/products/')
@app.route('/products')
def products():
    """Render list of products."""
    
    return render_template('productsCatalog.html',productList = listOfProducts,locale = locale)


@app.route('/products/<int:id>')
def productPage(id):
    """renders a single product page"""
    for product in listOfProducts:
        if product.get("id") == id:
            return render_template('product.html',product = product,locale = locale)
    return render_template('404.html')


# @app.route('/images')
# def get_image(imageName):
#     return { url_for('static', filename='images/{{product[\'image\']}}')}}

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("IP",
'0.0.0.0'),port=int(os.getenv("PORT", 8080) ))


