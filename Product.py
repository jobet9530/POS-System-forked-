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
             product = Product.query(Product).all()
             product_response = [{
                'product_id': p.product_id,
                'product_name': p.product_name,
                'price': p.price,
                'stock_quantity': p.stock_quantity,
                'barcode': p.barcode,
                'category': p.category
            } for p in product]
            return jsonify(product_response)
        except Exception as e:
            return str(e)

