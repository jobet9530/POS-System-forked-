import unittest
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from main import ProductResource, Product


class TestProductResource(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        if not hasattr(self.app, 'db'):
            self.db = SQLAlchemy(self.app)
            self.db.init_app(self.app)

        with self.app.app_context():
            self.db.create_all()

        self.api = Api(self.app)
        self.api.add_resource(ProductResource, '/product',
                              '/product/<int:product_id>')
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_get_product(self):
        with self.app.app_context():
            product = Product(
                product_name='Test Product',
                price=10.99,
                stock_quantity=100,
                barcode='123456789012',
                category='Test Category'
            )
            self.db.session.add(product)
            self.db.session.commit()

        response = self.client.get('/product/1')

        self.assertEqual(response.status_code, 200)

        expected_data = {
            'product_id': 1,
            'product_name': 'Test Product',
            'price': 10.99,
            'stock_quantity': 100,
            'barcode': '123456789012',
            'category': 'Test Category'
        }

        self.assertEqual(response.json, expected_data)

    def test_get_product_not_found(self):
        response = self.client.get('/product/1')

        self.assertEqual(response.status_code, 404)
        expected_data = {'message': 'Product not found'}
        self.assertEqual(response.get_json(), expected_data)

    def test_put_product(self):
        with self.app.app_context():
            product = Product(
                product_name='Test Product',
                price=10.99,
                stock_quantity=100,
                barcode='123456789012',
                category='Test Category'
            )
            self.db.session.add(product)
            self.db.session.commit()

        response = self.client.put('/product/1', json={
            'product_name': 'Updated Product',
            'price': 20.99,
            'stock_quantity': 200,
            'barcode': '987654321098',
            'category': 'Updated Category'
        })

        self.assertEqual(response.status_code, 200)

        with self.app.app_context():
            updated_product = Product.query.get(1)
            self.assertEqual(updated_product.product_name, 'Updated Product')

    def test_put_product_not_found(self):
        response = self.client.put(
            '/product/1', json={'product_name': 'Updated Product'})
        self.assertEqual(response.status_code, 404)
        expected_data = {'message': 'Product not found'}
        self.assertEqual(response.get_json(), expected_data)

    def test_delete_product(self):
        with self.app.app_context():
            product = Product(
                product_name='Test Product',
                price=10.99,
                stock_quantity=100,
                barcode='123456789012',
                category='Test Category'
            )
            self.db.session.add(product)
            self.db.session.commit()

        response = self.client.delete('/product/1')

        self.assertEqual(response.status_code, 200)

        with self.app.app_context():
            deleted_product = Product.query.get(1)
            self.assertIsNone(deleted_product)
            self.assertEqual(response.get_json(), {
                             'message': 'Product deleted successfully'})

    def test_delete_product_not_found(self):
        response = self.client.delete('/product/1')
        self.assertEqual(response.status_code, 404)
        expected_data = {'message': 'Product not found'}
        self.assertEqual(response.get_json(), expected_data)


if __name__ == '__main__':
    unittest.main()
