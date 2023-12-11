import unittest
from flask import Flask
from flask_restful import Api
from flask_testing import TestCase
from main import ProductResource, db


class ProductTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        api = Api(app)
        api.add_resource(ProductResource, '/product',
                         '/product/<int:product_id>')

        with app.app_context():
            db.create_all()
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_product(self):

        client = self.app.test_client()

        product_data = {
            'product_name': 'Test Product',
            'price': 10.99,
            'stock_quantity': 100,
            'barcode': '123456789012',
            'category': 'Test Category'
        }

        response = client.get('/product', json=product_data)
        self.assertEqual(response.status_code, 200)  # Fix the typo here

        product_id = response.json['product_id']

        response = client.get(f'/product/{product_id}')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.json['product_name'], product_data['product_name'])
        self.assertEqual(response.json['price'], product_data['price'])
        self.assertEqual(
            response.json['stock_quantity'], product_data['stock_quantity'])
        self.assertEqual(response.json['barcode'], product_data['barcode'])
        self.assertEqual(response.json['category'], product_data['category'])


if __name__ == '__main__':
    unittest.main()
