from flask import jsonify
from flask_restful import Resource
from database import db, Order


class OrderResource(Resource):

    def get(self, order_id=None):
        if order_id:
            order = Order.query.get(order_id)
            if order:
                return jsonify({
                    'order_id': order.order_id,
                    'customer_id': order.customer_id,
                    'order_date': order.order_date,
                    'total_amount': order.total_amount,
                    'payment_method': order.payment_method,
                    'notes': order.notes
                })
            else:
                return jsonify({'message': 'Order not found'}), 404
        else:
            orders = Order.query.all()
            order_list = [{
                'order_id': o.order_id,
                'customer_id': o.customer_id,
                'order_date': o.order_date,
                'total_amount': o.total_amount,
                'payment_method': o.payment_method,
                'notes': o.notes
            } for o in orders]
            return jsonify(order_list)
