from flask import jsonify
from flask_restful import Resource
from database import db, Customer

class Customer(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get(customer_id)
            if customer:
                return jsonify({
                    'customer_id': customer.customer_id,
                    'customer_name': customer.customer_name,
                    'customer_address': customer.customer_address,
                    'customer_phone': customer.customer_phone,
                    'customer_email': customer.customer_email
                })
            else:
                return jsonify({'message': 'Customer not found'}), 404
        else:
            customers = Customer.query.all()
            customer_list = [{
                'customer_id': c.customer_id,
                'customer_name': c.customer_name,
                'email': c.customer_email,
                'phone_address': c.customer_email,
                'address': c.customer_address
            } for c in customers]
            return jsonify(customer_list)