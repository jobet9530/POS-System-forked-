from flask import jsonify, request
from database import db, Customer, InactiveAccount
from flask_restful import Resource
from datetime import datetime


class CustomerResource(Resource):

    def get(self):
        try:
            customers = Customer.query(Customer).all()
            customers = [{
                'customer_id': customer[0].customer_id,
                'customer_name': customer[0].customer_name,
                'customer_address': customer[0].customer_address,
                'customer_email': customer[0].customer_email,
                'customer_phone': customer[0].customer_phone
            }for customer in customers]

            return jsonify(customers)
        except Exception as e:
            return str(e)

    def post(self):
        try:
            customers = Customer.query(Customer).all()
            customers = [{
                'customer_id': customer[0].customer_id,
                'customer_name': customer[0].customer_name,
                'customer_address': customer[0].customer_address,
                'customer_email': customer[0].customer_email,
                'customer_phone': customer[0].customer_phone
            }for customer in customers]

            customer = Customer(
                customer_name=request.json['customer_name'],
                customer_address=request.json['customer_address'],
                customer_email=request.json['customer_email'],
                customer_phone=request.json['customer_phone']
            )

            db.session.add(customer)
            db.session.commit()

            return jsonify(customers)
        except Exception as e:
            return str(e)

    def put(self):
        try:
            customers = Customer.query(Customer).all()
            customers = [{
                'customer_id': customer[0].customer_id,
                'customer_name': customer[0].customer_name,
                'customer_address': customer[0].customer_address,
                'customer_email': customer[0].customer_email,
                'customer_phone': customer[0].customer_phone
            }for customer in customers]

            return jsonify(customers)
        except Exception as e:
            return str(e)

    def __init__(self, customer_name, customer_address, customer_email, customer_phone):
        try:
            self.customer_name = customer_name
            self.customer_address = customer_address
            self.customer_email = customer_email
            self.customer_phone = customer_phone
        except Exception as e:
            return str(e)

    def update_activitiy(self):
        try:
            last_active_date = self.last_active_date()
            current_date = datetime.now().date()
            inactive_duration = current_date - last_active_date

            if inactive_duration.days >= 5 * 30:
                self.is_active = False
            else:
                self.is_active = True
            inactive_account = InactiveAccount(
                customer_id=self.customer_id,
                inactive_duration=inactive_duration
            )

            db.session.add(inactive_account)
            db.session.commit()
        except Exception as e:
            return str(e)
