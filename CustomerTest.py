import unittest
from Customer import CustomerResource


class TestCustomerResource(unittest.TestCase):
    def test_get_customer(self):
        customer_resource = CustomerResource()
        customer_data = {
            'customer_id': 1,
            'customer_name': 'Chicago vs Bulls',
            'customer_address': '123 Main St',
            'customer_phone': '555-1234',
            'customer_email': 'lTqFP@example.com'
        }

        response = customer_resource.post(customer_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json, {'message': 'Customer created successfully'})


if __name__ == '__main__':
    unittest.main()
