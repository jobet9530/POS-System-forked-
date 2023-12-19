from flask import jsonify, request
from flask_restful import Resource
from database import db, Product
import barcode
from barcode.writer import ImageWriter
from datetime import datetime


class ProductResource(Resource):
    def generate_unique_barcode(product_id):
        try:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            barcode_value = f"{product_id}-{timestamp}"

            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(barcode_value, writer=ImageWriter())
            ean.save(f"static/barcodes/{barcode_value}.png")

            return barcode_value
        except Exception as e:
            print(f"Error generating barcode: {e}")
            return None

    def post(self):
        try:
            product_name = request.json['product_name']
            price = request.json['price']
            stock_quantity = request.json['stock_quantity']
            category = request.json['category']

            new_product = Product(
                product_name=product_name,
                price=price,
                stock_quantity=stock_quantity,
                category=category
            )
            new_product.barcode = self.generate_unique_barcode(
                new_product.product_id)
            db.session.add(new_product)
            db.session.commit()
            return jsonify({'message': 'Product created successfully'})
        except Exception as e:
            return jsonify({'message': str(e)})

    def put(self):
        try:
            product_id = request.args.get('product_id')
            product = Product.query.get(product_id)

            if product:
                product.product_name = request.json['product_name']
                product.price = request.json['price']
                product.stock_quantity = request.json['stock_quantity']
                product.category = request.json['category']

                product.barcode = self.generate_unique_barcode(
                    product.product_id)
                db.session.commit()

                return jsonify({'message': 'Product updated successfully'})
            else:
                return jsonify({'message': 'Product not found'})

        except Exception as e:
            return jsonify({'message': str(e)})

    def delete(self):
        try:
            product_id = request.args.get('product_id')
            product = Product.query.get(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return jsonify({'message': 'Product deleted successfully'})
            else:
                return jsonify({'message': 'Product not found'})
        except Exception as e:
            return jsonify({'message': str(e)})

    def get(self):
        try:
            products = Product.query.all()
            product_list = []
            for product in products:
                product_data = {
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'price': product.price,
                    'stock_quantity': product.stock_quantity,
                    'barcode': product.barcode,
                    'category': product.category
                }
                product_list.append(product_data)
            return jsonify({'products': product_list})
        except Exception as e:
            return jsonify({'message': str(e)})
