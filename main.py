from flask import Flask, jsonify, render_template, url_for
from flask_restful import Api
from database import db
from Product import ProductResource
from Customer import CustomerResource
from Sale import SaleResource
from SaleItem import SaleItemResource
from User import UserResource
from Order import OrderResource
from OrderItem import OrderItemResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///POS.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)

product_resource_instance = ProductResource()
api.add_resource(ProductResource, '/product', '/product/<int:product_id>')

customer_resource_instance = CustomerResource()
api.add_resource(CustomerResource, '/customer', '/customer/<int:customer_id>')

sale_resource_instance = SaleResource()
api.add_resource(SaleResource, '/sale', '/sale/<int:sale_id>')

sale_item_resource_instance = SaleItemResource()
api.add_resource(SaleItemResource, '/sale_item',
                 '/sale_item/<int:sale_item_id>')

user_resource_instance = UserResource()
api.add_resource(UserResource, '/user', '/user/<int:user_id>')


order_resource_instance = OrderResource()
api.add_resource(OrderResource, '/order', '/order/<int:order_id>')


order_item_resource_instance = OrderItemResource()
api.add_resource(OrderItemResource, '/order_item',
                 '/order_item/<int:order_item_id>')


@app.route('/api/data')
def get_data():
    data = {'status': 'success', 'message': 'Data fetched successfully'}
    return jsonify(data)


@app.route('/')
def render_frontend():
    api_response = {'status': 'success', 'message': 'API data endpoint'}
    return render_template('index.html',
                           api_data=api_response,
                           css_url=url_for('static', filename='style.css'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
