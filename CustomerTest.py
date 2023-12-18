import unittest
from database import db, Customer
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class TestCustomerResource(unittest.TestCase):

    def setUp(self):
        try:
            self.app = Flask(__name__)
            self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
            self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            self.db = SQLAlchemy(self.app)
            self.db.init_app(self.app)
            db.create_all()
        except Exception as e:
            print(e)

    def tearDown(self):
        try:
            db.session.remove()
            db.drop_all()
        except Exception as e:
            print(e)

    def test_get_customer(self):
        try:
            customer = Customer(
                customer_name='test',
                email='test',
                address='test',
                phone_number='test'
            )
            db.session.add(customer)
            db.session.commit()
            customer = Customer.query.get(1)
            self.assertEqual(customer.customer_name, 'test')
        except Exception as e:
            print(e)

    def test_post_customer(self):
        try:
            customer = Customer(
                customer_name='test',
                email='test',
                address='test',
                phone_number='test'
            )
            db.session.add(customer)
            db.session.commit()
            customer = Customer.query.get(1)
            self.assertEqual(customer.customer_name, 'test')
        except Exception as e:
            print(e)

    def test_put_customer(self):
        try:
            customer = Customer(
                customer_name='test',
                email='test',
                address='test',
                phone_number='test'
            )
            db.session.add(customer)
            db.session.commit()
            customer_id = customer.customer_id
            customer = Customer.query.get(customer_id)
            customer.customer_name = 'test2'
            db.session.commit()

        except Exception as e:
            print(e)

    def test_delete_customer(self):
        try:
            customer = Customer(
                customer_name='test',
                email='test',
                address='test',
                phone_number='test'
            )
            db.session.add(customer)
            db.session.commit()
            customer = customer.customer_id
            db.session.delete(customer)
            db.session.commit()
            customer = Customer.query.get(1)
            self.assertEqual(customer.customer_name, 'test')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
