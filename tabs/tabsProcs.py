import json
import os
from time import sleep
import pandas as pd
from flask import Blueprint, render_template, current_app

getTabs_blueprint = Blueprint('getTabs_blueprint',__name__,template_folder='templates',static_folder='static')

@getTabs_blueprint.route('/tabs_main', methods=['GET'])
def tabs_main():
    current_app.logger.info(f'tabs_main:started')
    return render_template('tabs_main.html')

