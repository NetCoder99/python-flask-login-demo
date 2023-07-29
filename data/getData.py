import json
import os
from time import sleep
import pandas as pd
from flask import Blueprint, render_template
from flask import current_app

getData_blueprint = Blueprint('getData_blueprint',__name__,template_folder='templates',static_folder='static')

@getData_blueprint.route('/products_api', methods=['GET'])
def products_api():
    print('products_api - started')
    ## http://127.0.0.1:5000/data/products
    absolute_path = os.path.dirname(__file__)
    full_path     = os.path.join(absolute_path, "products.json")
    sleep(1)
    with open(full_path) as products_file:
        json_data = json.load(products_file)
        print('products_api - returned')
        return json_data['products']

@getData_blueprint.route('/products', methods=['GET'])
def products():
    return render_template('products.html')

@getData_blueprint.route('/products_ajax', methods=['GET'])
def products_ajax():
    return render_template('github_gui.html')

@getData_blueprint.route('/pandas_demo1', methods=['GET'])
def pandas_demo1():
    current_app.logger.info(f'pandas_demo1 was called')

    products_json = getProductsAsJson()
    df_products = pd.DataFrame(products_json)
    products_html = df_products.to_html(columns=['id', 'title', 'brand'],  classes=['table', 'table-striped'])
    return render_template('pandas_demo1.html',
                           tables=[products_html],
                           titles=["Pandas Demo"])

    # data_demo1 = {
    #     "fruit": ["apple", "banana", "grapes", "orange"],
    #     "colour": ["red", "yellow", "green", "orange"],
    #     "quantity": [2, 1, 1, 3],
    #     "price": [80, 40, 100, 75]
    # }
    # df_demo1 = pd.DataFrame(data_demo1)
    # tmp_html = df_demo1.to_html(classes='data', table_id='pandas_demo1')
    # return render_template('pandas_demo1.html', tables=[df_demo1.to_html(classes=['data', 'table', 'table-striped'])], titles=["Table Title"])

def getProductsAsJson():
    absolute_path = os.path.dirname(__file__)
    full_path     = os.path.join(absolute_path, "products.json")
    with open(full_path) as products_file:
        json_data = json.load(products_file)
        print('products_api - returned')
        return json_data['products']
