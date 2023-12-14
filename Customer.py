from flask import jsonify, Flask
from datetime import datetime, timedelta
from database import db, Customer

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'


class CustomerResource(Resource):
    def get(self, customer_id=None):
        try:
            if customer_id is None:
                customers = Customer.query.all()
                return jsonify([customer.to_dict() for customer in customers])
            else:
                customer = Customer.query.get(customer_id)
                return jsonify(customer.to_dict())
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def post(self, customer_id=None):
        try:
            data = request.get_json()
            customer = Customer(**data)
            db.session.add(customer)
            db.session.commit()
            return jsonify(customer.to_dict())
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def put(self, customer_id):
        try:
            data = request.get_json()
            customer = Customer.query.get(customer_id)
            customer.update(data)
            db.session.commit()
            return jsonify(customer.to_dict())
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def delete(self, customer_id):
        try:
            customer = Customer.query.get(customer_id)

            five_months_ago = datetime.now() - timedelta(days=150)

            if customer.last_activity < five_months_ago:
                customer.active = False
                db.session.commit()
                return jsonify({'message': 'Customer temporarily deleted successfully'})
            else:
                return jsonify({'message': 'Customer cannot be deleted'})

        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500
