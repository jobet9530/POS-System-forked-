from flask import jsonify
from flask_restful import Resource
from database import db, OrderItem


class OrderItemResource(Resource):

    def get(self, order_item_id):
        order_item = OrderItem.query.get(order_item_id)
        if order_item_id:
            if order_item:
                return jsonify({
                    'order_item_id': order_item.order_item_id,
                    'order_id': order_item.order_id,
                    'product_id': order_item.product_id,
                    'quantity': order_item.quantity,
                    'unit_price': order_item.unit_price,
                    'item_amount': order_item.item_amount
                })
            else:
                return jsonify({'message': 'Order item not found'}), 404
        else:
            order_items = OrderItem.query.all()
            order_item_list = [{
                'order_item_id': o.order_item_id,
                'order_id': o.order_id,
                'product_id': o.product_id,
                'quantity': o.quantity,
                'unit_price': o.unit_price,
                'item_amount': o.item_amount
            } for o in order_items]
            return jsonify(order_item_list)
