import pytest
from Customer import CustomerResource


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


def test_post_customer(customer):
    data = {
        "name": "Jane",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = customer.post(data=data)
    assert response.status_code == 201


def test_put_customer(customer):
    data = {
        "name": "Jane",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = customer.put(customer_id=1, data=data)
    assert response.status_code == 200
