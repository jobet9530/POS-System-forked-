import unittest
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from main import ProductResource, Product, db


class TestProductResource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        cls.db = SQLAlchemy(cls.app)

        with cls.app.app_context():
            cls.db.create_all()

        cls.api = Api(cls.app)
        cls.api.add_resource(ProductResource, '/product',
                             '/product/<int:product_id>')
        cls.client = cls.app.test_client()
        pass

    @classmethod
    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()
        pass

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

    def test_get_product_not_found(self, product_id):
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

    def test_put_product_not_found(self, product_id):
        response = self.client.put(
            f'/product/{product_id}', json={'product_name': 'Updated Product'})
        print(response.data.decode('utf-8'))

        if response.status_code == 500:
            print(response.get_json())

        self.assertEqual(response.status_code, 404)
        expected_data = {'message': 'Product not found'}
        self.assertEqual(response.get_json(), expected_data)

        # if response == 404:
        # expected_data = {'message': 'Product not found'}
        # actual_data = response.get_json()
        # self.assertEqual(actual_data, expected_data)
        # else:
        # self.fail(
        # "Expected JSON response but received content type: {}".format(response.content_type))

    def test_post_product_not_found(self, product_id):
        # product = Product.query.get(product_id)
        self.test_post_product_not_found(product_id=123)

        response = self.client.put(
            '/product/2', json={'product_name': 'Updated Product No'})
        self.assertEqual(response.status_code, 404)

        if response == 404:
            expected_data = {'message': 'Product not found'}
            actual_data = response.get_json()
            self.assertEqual(actual_data, expected_data)
        else:
            self.fail(
                "Expected JSON response but received content type: {}".format(response.content_type))

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

    def test_delete_product_not_found(self, product_id):
        product = Product.query.get(product_id)

        if not product:
            return ({'message': 'Product not found'}, 404)

        db.session.delete(product)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()

    test_client.test_post_product_not_found(product_id=123)
