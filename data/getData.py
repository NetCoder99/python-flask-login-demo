import json
import os

from flask import Blueprint, render_template

getData_blueprint = Blueprint('getData_blueprint',__name__,template_folder='templates',static_folder='static')

@getData_blueprint.route('/products_api', methods=['GET'])
def products_api():
    ## http://127.0.0.1:5000/data/products
    absolute_path = os.path.dirname(__file__)
    full_path     = os.path.join(absolute_path, "products.json")
    with open(full_path) as products_file:
        return json.load(products_file)

@getData_blueprint.route('/products', methods=['GET'])
def products():
    return render_template('products.html')
