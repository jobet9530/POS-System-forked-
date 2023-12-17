from flask import jsonify, request
from flask_restful import Resource
from database import db, OrderItem, Product

class OrderItemResource(Resource):

    def get(self):
        try:
            order_items = OrderItem.query(OrderItem, Product).join(
                Product, OrderItem.product_id == Product.product_id).all()
            order_items = [{
                'order_item_id': order_item[0].order_item_id,
                'order_id': order_item[0].order_id,
                'product_id': order_item[0].product_id,
                'product_name': order_item[1].product_name,
                'quantity': order_item[0].quantity,
                'price': order_item[0].price
            }for order_item in order_items]

            return jsonify(order_items)
        except Exception as e:
            return str(e)

    def post(self):
        try:
            order_items = OrderItem.query(OrderItem, Product).join(
                Product, OrderItem.product_id == Product.product_id).all()
            order_items = [{
                'order_item_id': order_item[0].order_item_id,
                'order_id': order_item[0].order_id,
                'product_id': order_item[0].product_id,
                'product_name': order_item[1].product_name,
                'quantity': order_item[0].quantity,
                'price': order_item[0].price
            }for order_item in order_items]

            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )

            db.session.add(product)
            db.session.commit()

            return jsonify(order_items)
        except Exception as e:
            return str(e)
