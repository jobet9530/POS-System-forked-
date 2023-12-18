import unittest
from datebase import db, Sale, Product, Customer
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class SaleTest(unittest.TestCase):

    def setUp(self):
        try:
            self.app = Flask(__name__)
            self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
            self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            self.db = SQLAlchemy(self.app)
            self.db.create_all()
            self.client = self.app.test_client()
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def tearDown(self):
        try:
            self.db.session.remove()
            self.db.drop_all()
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def calculate_total_price(quantity, price):
        return quantity * price

    def test_get_sale(self):
        try:
            customer = Customer(customer_name='Jobet')
            product = Product(product_name='T-Shirt', price=10)
            sale = Sale(
                customer_id=customer.id,
                product_id=product.id,
                quantity=10,
                total_price=self.calculate_total_price(10, 10)
            )

            db.session.add(customer)
            db.session.add(product)
            db.session.add(sale)
            db.session.commit()

            response = self.client.get('/sale')
            self.assertEqual(response.status_code, 200)

            calculated_total_price = self.calculate_total_price(10, 10)

        except Exception as e:
        return {'message': f'An error occurred: {e}'}, 500
