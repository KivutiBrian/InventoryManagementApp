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


# error handlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/errors/404.html'), 404


@app.before_first_request
def create():
    db.create_all()

@app.route('/')
def index():
    return render_template('/landing/index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('/admin/dashboard.html')

@app.route('/inventories', methods=['GET', 'POST'])
def inventories():
    return InventoryService.inventories()


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)