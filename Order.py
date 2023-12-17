from flask import jsonify
from flask_restful import Resource
from database import db, Order, Customer


class OrderResource(Resource):

    def get(self):
        try:
            orders = Order.query.join(
                Customer, Order.customer_id == Customer.customer_id).all()
            return jsonify(orders)
        except Exception as e:
            return str(e)
