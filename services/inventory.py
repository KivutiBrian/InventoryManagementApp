from flask import render_template,request, redirect, url_for
# models
from models.inventory import Inventory
from models.stock import Stock
from models.sales import Sales

class InventoryService:

    @classmethod
    def inventories(cls):
        # get all inventories
        all_inventories = Inventory.fetch_all()
        print("Heree:", all_inventories)
        return render_template('/admin/admin.html')

    @classmethod
    def add_inventory(cls):
        if request.method == 'POST':
            name:str = request.form['name']
            itype:str = request.form['category']
            bp = request.form['bp']
            sp = request.form['bp']

            # check if the inventory name exists
            if Inventory.check_inventorty_exists(inventory_name=name):
                print("The inventory already exists")
                return redirect(url_for('admin'))
            else:
                record = Inventory(name=name.title(),itype= itype.title(),bp = bp,sp=sp)
                record.create_record()
                print("Success!")
                return redirect(url_for('admin'))
