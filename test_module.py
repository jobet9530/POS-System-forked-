import pytest
from Customer import CustomerResource
from Warehouse import WarehouseResource
import coverage
from coverage.exceptions import NoDataError

cov = coverage.Coverage()
cov.start()


@pytest.fixture
def customer():
    resource = CustomerResource()
    return resource


@pytest.fixture
def warehouse():
    resource = WarehouseResource()
    return resource


def test_get_warehouse(warehouse):
    response = warehouse.get(warehouse_id=1)
    assert response.status_code == 200
    assert response.data == {
        "id": 1,
        "name": "Warehouse 1",
        "address": "123 Main St",
        "phone": "555-1234",
        "email": "9yQpE@example.com",
    }
    print("test_get_warehouse passed successfully!")


def test_post_warehouse(warehouse):
    data = {
        "name": "Warehouse 2",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = warehouse.post(data=data)
    assert response.status_code == 201
    print("test_post_warehouse passed successfully!")


def test_put_warehouse(warehouse):
    data = {
        "name": "Warehouse 2",
        "address": "456 Main St",
        "phone": "555-5678",
        "email": "9yQpE@example.com",
    }
    response = warehouse.put(warehouse_id=1, data=data)
    assert response.status_code == 200
    print("test_put_warehouse passed successfully!")


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

try:
    cov.load()
    if not cov.get_data():
        raise NoDataError("No data to report.")
    cov.report()
    percentage_coverage = cov.report()
    print(f"Code coverage: {percentage_coverage}%")
except NoDataError as e:
    print(e)
