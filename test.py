import pytest
from Customer import CustomerResource
import coverage

cov = coverage.Coverage()
cov.start()

@pytest.fixture
def customer():
    resource = CustomerResource()
    return resource


def test_get_customer(customer):
    response = customer.get(customer_id=1)
    assert response.status_code == 200
    assert response.data == {
        "id": 1,
        "name": "John",
        "address": "123 Main St",
        "phone": "555-1234",
        "email": "9yQpE@example.com",
    }
    print("test_get_customer passed successfully!")


def test_post_customer(customer):
    data = {
        "name": "Jane",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = customer.post(data=data)
    assert response.status_code == 201
    print("test_post_customer passed successfully!")


def test_put_customer(customer):
    data = {
        "name": "Jane",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = customer.put(customer_id=1, data=data)
    assert response.status_code == 200
    print("test_put_customer passed successfully!")

cov.stop()
cov.save()
cov.combine()
cov.report()

percentage_coverage = cov.report()

print(f"Code coverage: {percentage_coverage}%")
