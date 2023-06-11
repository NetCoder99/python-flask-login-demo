import json
import os
from time import sleep

from flask import Blueprint, render_template

getData_blueprint = Blueprint('getData_blueprint',__name__,template_folder='templates',static_folder='static')

@getData_blueprint.route('/products_api', methods=['GET'])
def products_api():
    ## http://127.0.0.1:5000/data/products
    absolute_path = os.path.dirname(__file__)
    full_path     = os.path.join(absolute_path, "products.json")

    sleep(2)

    with open(full_path) as products_file:
        json_data = json.load(products_file)
        return json_data['products']

@getData_blueprint.route('/products', methods=['GET'])
def products():
    return render_template('products.html')

@getData_blueprint.route('/products_ajax', methods=['GET'])
def products_ajax():
    return render_template('products_ajax.html')
