from flask import jsonify, request
from flask_restful import Resource
from database import db, SaleItem, Product


class SaleItemResource(Resource):

    def get(self):
        try:
            sale_items = SaleItem.query(SaleItem, Product).join(
                Product, SaleItem.product_id == Product.product_id).all()
            sale_items = [{
                'sale_item_id': sale_item[0].sale_item_id,
                'sale_id': sale_item[0].sale_id,
                'product_id': sale_item[0].product_id,
                'product_name': sale_item[1].product_name,
                'quantity': sale_item[0].quantity,
                'price': sale_item[0].price
            }for sale_item in sale_items]

            return jsonify(sale_items)
        except Exception as e:
            return str(e)

    def post(self):
        try:
            sale_items = SaleItem.query(SaleItem, Product).join(
                Product, SaleItem.product_id == Product.product_id).all()
            sale_items = [{
                'sale_item_id': sale_item[0].sale_item_id,
                'sale_id': sale_item[0].sale_id,
                'product_id': sale_item[0].product_id,
                'product_name': sale_item[1].product_name,
                'quantity': sale_item[0].quantity,
                'price': sale_item[0].price
            }for sale_item in sale_items]

            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )

            db.session.add(product)
            db.session.commit()

            return jsonify(sale_items)
        except Exception as e:
            return str(e)
