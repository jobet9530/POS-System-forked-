from flask import jsonify
from flask_restful import Resource, fields, marshal_with
from database import db, Customer

customer_fields = {
    'customer_id': fields.String,
    'customer_name': fields.String,
    'customer_address': fields.String,
    'customer_phone': fields.String,
    'customer_email': fields.String
}

class CustomerResource(Resource):
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
                'phone': c.customer_phone,
                'address': c.customer_address
            } for c in customers]
            return jsonify(customer_list)

    @marshal_with(customer_fields)
    def post(self, customer_data):
        customer = Customer(
            customer_name=customer_data['customer_name'],
            customer_address=customer_data['customer_address'],
            customer_phone=customer_data['customer_phone'],
            customer_email=customer_data['customer_email']
        )
        db.session.add(customer)
        db.session.commit()
        return customer, 201

    @marshal_with(customer_fields)
    def put(self, customer_id, customer_data):
        customer = Customer.query.get(customer_id)
        if customer:
            customer.customer_name = customer_data['customer_name']
            customer.customer_address = customer_data['customer_address']
            customer.customer_phone = customer_data['customer_phone']
            customer.customer_email = customer_data['customer_email']
            db.session.commit()
            return customer
        else:
            return jsonify({'message': 'Customer not found'}), 404
