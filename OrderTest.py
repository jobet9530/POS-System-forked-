import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from Order import OrderResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
api.add_resource(OrderResource, '/order')


class TestOrderResource(unittest.TestCase):
    def setUp(self):
        try:
            app.config['Test'] = True
            self.app = app.test_client()
            self.db = SQLAlchemy(app)
            self.db.create_all()
        except Exception as e:
            return str(e)

    def tearDown(self):
        try:
            self.db.session.remove()
            self.db.drop_all()
        except Exception as e:
            return str(e)

    def test_get(self):
        try:
            response = self.app.get('/order')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, [{
                'order_id': 1,
                'customer_id': 1,
                'customer_name': 'John',
                'order_date': '2020-01-01',
                'customer': {
                    'customer_id': 1,
                    'customer_name': 'John',
                    'customer_address': '123 Main St',
                    'customer_email': 'jDyKs@example.com',
                    'customer_phone': '123-456-7890'
                },
                'product': {
                    'product_id': 1,
                    'product_name': 'Product 1',
                    'price': 10.0,
                    'stock_quantity': 100,
                    'barcode': '123456789012',
                    'category': 'Category 1'
                },
                'quantity': 5,
                'price': 50.0,
                'payment_method': 'Credit Card',
                'payment_date': '2020-01-01',

            }])
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    unittest.main()
