from flask import jsonify, request
from flask_restful import Resource
from database import db, Order, Customer


class OrderResource(Resource):

    def get(self):
        try:
            customer_id = request.args.get('customer_id')
            orders = db.session.query(Order).filter_by(
                customer_id=customer_id).all()
            result = []
            for order in orders:
                customer = Customer.query.get(order.customer_id)
                result.append({
                    'order_id': order.order_id,
                    'customer_id': order.customer_id,
                    'customer_name': customer.customer_name,
                    'order_date': order.order_date
                })
                return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': f'An error occurred: {e}'}), 500

    def post(self):
        try:
            customer_id = request.json['customer_id']
            orders = db.session.query(Order).filter_by(
                customer_id=customer_id).all()
            result = []
            for order in orders:
                customer = Customer.query.get(order.customer_id)
                result.append({
                    'order_id': order.order_id,
                    'customer_id': order.customer_id,
                    'customer_name': customer.customer_name,
                    'order_date': order.order_date
                })
                return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': f'An error occurred: {e}'}), 500

    def put(self):
        try:
            customer_id = request.json['customer_id']
            new_order_date = request.json['order_date']
            order = Order.query.filter_by(customer_id=customer_id).first()

            if order:
                order.order_date = new_order_date
                db.session.commit()
                return jsonify({'message': 'Order updated successfully'}), 200
            else:
                return jsonify({'message': 'Order not found'}), 404

        except Exception as e:
            return jsonify({'message': f'An error occurred: {e}'}), 500

    def delete(self):
        try:
            customer_id = request.json['customer_id']
            order = Order.query.filter_by(customer_id=customer_id).first()

            if order:
                db.session.delete(order)
                db.session.commit()
                return jsonify({'message': 'Order deleted successfully'}), 200
            else:
                return jsonify({'message': 'Order not found'}), 404
        except Exception as e:
            return jsonify({'message': f'An error occurred: {e}'}), 500
