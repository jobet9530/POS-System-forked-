import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


class ProductResource(Resource):
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get(product_id)
            if product:
                return jsonify({
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'price': product.price,
                    'stock_quantity': product.stock_quantity,
                    'barcode': product.barcode,
                    'category': product.category
                })
            else:
                return jsonify({'message': 'Product not found'}), 404
        else:
            products = Product.query.all()
            product_list = [{
                'product_id': p.product_id,
                'product_name': p.product_name,
                'price': p.price,
                'stock_quantity': p.stock_quantity,
                'barcode': p.barcode,
                'category': p.category
            } for p in products]
            return jsonify(product_list)

  def get(self, product_id):
    if product_id:
      product = Product.query.get(product_id)
      if product:
        return jsonify({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'price': product.price,
            'stock_quantity': product.stock_quantity,
            'barcode': product.barcode,
            'category': product.category
        })
      else:
        return jsonify({'message': 'Product not found'}), 404
    else:
      products = Product.query.all()
      product_list = [{
          'product_id': p.product_id,
          'product_name': p.product_name,
          'price': p.price,
          'stock_quantity': p.stock_quantity,
          'barcode': p.barcode,
          'category': p.category
      } for p in products]
      return jsonify(product_list)

  def put(self, product_id):
    parser = reqparse.RequestParser()
    parser.add_argument('product_name',
                        type=str,
                        required=True,
                        help='Product name is required')

    args = parser.parse_args()
    new_product_name = args['product_name']

    product = Product.query.get(product_id)
    if product:
      product.product_name = new_product_name
      db.session.commit()
      return jsonify({'message': 'Product updated successfully'})
    else:
      return jsonify({'message': 'Product not found'}), 404

  def delete(self, product_id):
    product = Product.query.get(product_id)
    if product:
      db.session.delete(product)
      db.session.commit()
      return jsonify({'message': 'Product deleted successfully'})
    else:
      return jsonify({'message': 'Product not found'}), 404