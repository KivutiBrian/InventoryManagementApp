from flask import Flask, render_template, request, redirect, url_for, flash
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


@app.context_processor
def utility_processor():
    def compute_quanity(inventoryID: int):
        # find an inventory that matches the id
        inv = Inventory.get_inventory_byID(id=inventoryID)
        if inv is not None:
            # get the the stock quanity
            total_stock = list(map(lambda obj: obj.quantity, inv.stock))
            total_sales = list(map(lambda obj: obj.quantity, inv.sales))
            return sum(total_stock) - sum(total_sales)
            
    return dict(compute_quanity=compute_quanity)



@app.route('/')
def index():
    return render_template('/landing/index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    total_inventories = len(Inventory.fetch_all())

    return render_template('/admin/dashboard.html', ti=total_inventories)

@app.route('/inventories', methods=['GET', 'POST'])
def inventories():
    return InventoryService.inventories()


@app.route("/inventories/<int:inv_id>/restock", methods=['POST'])
def restock(inv_id):
    if request.method == 'POST':
        qty = request.form['qty']
        
        r = Stock(quantity=qty,inventoryId=inv_id)
        r.create_record()
        flash("New stock successfully added", "success")

        return redirect(url_for('inventories'))

@app.route("/inventories/<int:inv_id>/make-sale", methods=['POST'])
def make_sale(inv_id):
    if request.method == "POST":
        qty = request.form['qty']

        s = Sales(quantity=qty, inventoryId=inv_id)
        s.create_record()
        flash("Sale successfully recorded", "success")
        return redirect(url_for('inventories'))


@app.route('/inventories/<int:inv_id>/edit', methods=['POST'])
def edit_inventory(inv_id):
    if request.method == 'POST':
        name:str = request.form['name']
        itype:str = request.form['category']
        bp = request.form['bp']
        sp = request.form['sp']

        u = Inventory.edit_inventory(
            inv_id=inv_id,
            name=name,
            itype=itype,
            bp=bp,
            sp=sp
        )
        flash("Inventory record successfully updated", "success")
        return redirect(url_for('inventories'))


#################################################################
"""Stock"""
@app.route('/stock')
def stock():
    all_stock = Stock.fetch_all()
    return render_template('admin/stock.html', all_stock=all_stock)

@app.route('/sales')
def sales():
    all_sales = Sales.fetch_all()
    return render_template('admin/sales.html', all_sales=all_sales)



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)