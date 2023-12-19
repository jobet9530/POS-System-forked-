from flask import jsonify, request
from flask_restful import Resource
from database import db, Product
import barcode
from barcode.writer import ImageWriter
from datetime import datetime


class ProductResource(Resource):

    def post(self):
        try:
            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )
            db.session.add(product)
            db.session.commit()

        except Exception as e:
            return str(e)

    def get(self):
        try:
            products = Product.query.all()
            products = [{
                'product_id': product.product_id,
                'product_name': product.product_name,
                'price': product.price,
                'stock_quantity': product.stock_quantity,
                'barcode': product.barcode,
                'category': product.category
            }for product in products]

            return jsonify(products)
        except Exception as e:
            return str(e)
