from flask import jsonify, request
from database import db, Customer
from flask_restful import Resource

class CustomerResource(Resource):

    def get(self):
        try:
            customer_id = request.args.get('customer_id')
            if customer_id:
                customer = Customer.query.get(customer_id)
                if customer is None:
                    return {'message': 'Customer not found'}, 404
                return jsonify(customer.to_dict())
            else:
                return {'message': 'Customer ID not provided'}, 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def post(self):
        try:
            data = request.get_json()
            customer = Customer(
                customer_name=data['customer_name'],
                customer_address=data['customer_address'],
                customer_phone_number=data['customer_phone_number'],
                customer_email=data['customer_email']
            )
            db.session.add(customer)
            db.session.commit()
            return jsonify(customer.to_dict()), 201

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def put(self):
        try:
            data = request.get_json()

            customer_id = data.get('customer_id')

            if not customer_id:
                return {'message': 'Customer ID not provided'}, 400

            customer = Customer.query.get(customer_id)

            if not customer:
                return {'message': 'Customer not found'}, 404

            customer.customer_name = data.get('customer_name')
            customer.customer_address = data.get('customer_address')
            customer.customer_phone_number = data.get('customer_phone_number')
            customer.customer_email = data.get('customer_email')

            db.session.commit()

            return jsonify(customer.to_dict()), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500