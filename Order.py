from flask import jsonify, request
from flask_restful import Resource
from database import db, Order, Customer


class OrderResource(Resource):

    def get(self):
        try:
            orders = Order.query(Order, Customer).join(
                Customer, Order.customer_id == Customer.customer_id).all()
            orders = [{
                'order_id': order[0].order_id,
                'customer_id': order[0].customer_id,
                'customer_name': order[1].customer_name,
                'order_date': order[0].order_date,
                'total_amount': order[0].total_amount
            }for order in orders]

            return jsonify(orders)

        except Exception as e:
            return str(e)

    def post(self):
        try:
            customer = []
            orders = Order.query(Order, Customer).join(
                Customer, Order.customer_id == Customer.customer_id).all()
            orders = [{
                'order_id': order[0].order_id,
                'customer_id': order[0].customer_id,
                'customer_name': order[1].customer_name,
                'order_date': order[0].order_date,
                'total_amount': order[0].total_amount
            }for order in orders]

            customer = Customer(
                customer_name=request.json['customer_name'],
                customer_address=request.json['customer_address'],
                customer_email=request.json['customer_email'],
                customer_phone=request.json['customer_phone']
            )

            db.session.add(customer)
            db.session.commit()

            return jsonify(orders)
        except Exception as e:
            return str(e)

    def put(self):
        try:
            orders = Order.query(Order, Customer).join(
                Customer, Order.customer_id == Customer.customer_id).all()
            orders = [{
                'order_id': order[0].order_id,
                'customer_id': order[0].customer_id,
                'customer_name': order[1].customer_name,
                'order_date': order[0].order_date,
                'total_amount': order[0].total_amount
            }for order in orders]
            return jsonify(orders)
        except Exception as e:
            return str(e)

    def delete(self):
        try:
            orders = Order.query(Order, Customer).join(
                Customer, Order.customer_id == Customer.customer_id).all()
            orders = [{
                'order_id': order[0].order_id,
                'customer_id': order[0].customer_id,
                'customer_name': order[1].customer_name,
                'order_date': order[0].order_date,
                'total_amount': order[0].total_amount
            }for order in orders]
            return jsonify(orders)
        except Exception as e:
            return str(e)
