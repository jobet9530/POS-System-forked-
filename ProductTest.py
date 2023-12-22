import unittest
from flask import Flask, jsonify
from flask_restful import Api
from ProductResource import ProductResource

app = Flask(__name__)
api = Api(app)
api.add_resource(ProductResource, '/product')


class ProductResourceTestCase(unittest.TestCase):
    def test_get_product(self):
        try:
            response = app.test_client().get('/product')
            self.assertEqual(response.status_code, 200)
            products = {
                'product_id': 1,
                'product_name': 'Product 1',
                'price': 10,
                'stock_quantity': 100,
                'barcode': '123456789012',
                'category': 'Category 1'
            }
            expected_response = {'products': [
                products], 'message': 'Products Retrieve successfully'}
            self.assertEqual(response.json, jsonify(expected_response).json)
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
