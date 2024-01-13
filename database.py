import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///POS.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.Text, unique=True)
    category = db.Column(db.Text)


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    address = db.Column(db.Text)


class Sale(db.Model):
    sale_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    sale_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.Text)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    customer = db.relationship('Customer', backref='sales')
    user = db.relationship('User', backref='sales')


class SaleItem(db.Model):
    sale_item_id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.sale_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    item_amount = db.Column(db.Float, nullable=False)
    sale = db.relationship('Sale', backref='items')
    product = db.relationship('Product', backref='sales')


class User(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    customer_name = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, default='user')
    customer = db.relationship('Customer', backref='users')


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    order_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.Text)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    customer = db.relationship('Customer', backref='orders')
    user = db.relationship('User', backref='orders')


class OrderItem(db.Model):
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    item_amount = db.Column(db.Float, nullable=False)
    order = db.relationship('Order', backref='items')
    product = db.relationship('Product', backref='orders')


class Warehouse(db.Model):
    warehouse_id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.Text, nullable=False)
    warehouse_address = db.Column(db.Text)
    warehouse_phone_number = db.Column(db.Text)
    warehouse_email = db.Column(db.Text)


class WarehouseItem(db.Model):
    warehouse_item_id = db.Column(db.Integer, primary_key=True)
    warehouse_id = db.Column(
        db.Integer, db.ForeignKey('warehouse.warehouse_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    warehouse = db.relationship('Warehouse', backref='items')
    product = db.relationship('Product', backref='warehouses')


class MonthlySales(db.Model):
    month = db.Column(db.Text, primary_key=True)
    sales = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    profit_margin = db.Column(db.Float, nullable=False)
    revenue_growth = db.Column(db.Float, nullable=False)
    profit_growth = db.Column(db.Float, nullable=False)
    revenue_per_sale = db.Column(db.Float, nullable=False)
    profit_per_sale = db.Column(db.Float, nullable=False)
    revenue_per_customer = db.Column(db.Float, nullable=False)
    profit_per_customer = db.Column(db.Float, nullable=False)
    revenue_per_product = db.Column(db.Float, nullable=False)
    profit_per_product = db.Column(db.Float, nullable=False)


class InactiveAccount(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, default='user')


class Delivery(db.Model):
    delivery_id = db.Column(db.Integer, primary_key=True)
    delivery_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
    delivery_status = db.Column(db.Text)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    order = db.relationship('Order', backref='deliveries')


if __name__ == '__main__':
    db_file_path = 'POS.sqlite'

    try:
        with app.app_context():
            inspector = inspect(db.engine)

            if not os.path.exists(db_file_path):
                # Create the tables
                db.create_all()
                print("Database file created, and tables created successfully.")
            else:
                # Check if each table exists, and create it if not
                for table_name in db.metadata.tables.keys():
                    if not inspector.get_table_names().__contains__(table_name):
                        db.create_all()
                        print(f"Table '{table_name}' created successfully.")
                    else:
                        print(
                            f"Table '{table_name}' already exists. Skipping table creation.")

    except Exception as e:
        print(f"An error occurred: {e}")
