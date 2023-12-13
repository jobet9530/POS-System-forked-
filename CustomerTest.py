import unittest
# Import the existing SQLAlchemy instance
from Customer import CustomerResource, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Import the SQLAlchemy class
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'


class TestCustomerResource(unittest.TestCase):
    def setUp(self):
        app.app_context().push()
        db.init_app(app)
        db.create_all()  # Create the database tables

    def tearDown(self):
        db.session.remove()  # Close the database session
        db.drop_all()  # Drop the database tables

        if os.path.exists('test.sqlite'):
            os.remove('test.sqlite')

    def test_post_customer(self):
        with app.test_request_context():
            resource = CustomerResource()
            response = resource.post()
            self.assertEqual(response.status_code, 200)

    def test_get_customer(self):
        with app.test_request_context():
            resource = CustomerResource()
            response = resource.get()
            self.assertEqual(response.status_code, 200)

    def test_put_customer(self):
        with app.test_request_context():
            resource = CustomerResource()
            response = resource.put(
                customer_id=1, customer_data={"name": "test"})
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
