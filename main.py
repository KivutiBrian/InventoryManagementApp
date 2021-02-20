from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# configs
from configs.configurations import Development, Testing, Production


app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)

# models
from models.inventory import Inventory
from models.stock import Stock
from models.sales import Sales

# services
from services.inventory import InventoryService

@app.before_first_request
def create():
    db.create_all()

@app.route('/')
def index():
    return render_template('/landing/index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        InventoryService.add_inventory()
        
    return InventoryService.inventories()


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)