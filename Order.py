from flask import jsonify
from flask_restful import Resource
from database import db, Order


class OrderResource(Resource):

    def get(self, order_id):
        try:
            orders = Order.query.all()
            return jsonify([order.serialize() for order in orders])
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    def put(self):
        try:
            order = Order()
            db.session.add(order)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Order created successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    def delete(self):
        try:
            order = Order.query.first()
            db.session.delete(order)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Order deleted successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    def post(self):
        try:
            order = Order()
            db.session.add(order)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Order created successfully'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
