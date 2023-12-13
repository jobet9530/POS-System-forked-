import unittest
from Customer import CustomerResource


class TestCustomerResource(unittest.TestCase):
    def test_post_customer(self):
        resource = CustomerResource()
        response = resource.post()
        self.assertEqual(response.status_code, 200)

    def test_get_customer(self):
        resource = CustomerResource()
        response = resource.get()
        self.assertEqual(response.status_code, 200)

    def test_put_customer(self):
        resource = CustomerResource()
        response = resource.put(customer_id=1, customer_data={"name": "test"})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
