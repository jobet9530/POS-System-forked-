from flask import Flask, jsonify, render_template, url_for
from flask_restful import Api, Resource, reqparse
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from database import db, Product, Customer, Sale, SaleItem, User, Order, OrderItem
from product_resource import ProductResource
from customer_resource import CustomerResource
from sale_resource import SaleResource

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


class SaleItemResource(Resource):

    def get(self, sale_item_id):
        sale_item = SaleItem.query.get(sale_item_id)
        if sale_item_id:
            if sale_item:
                return jsonify({
                    'sale_item_id': sale_item.sale_item_id,
                    'sale_id': sale_item.sale_id,
                    'product_id': sale_item.product_id,
                    'quantity': sale_item.quantity,
                    'price': sale_item.price,
                    'amount': sale_item.amount
                })
            else:
                return jsonify({'message': 'Sale item not found'}), 404
        else:
            sale_items = SaleItem.query.all()
            sale_item_list = [{
                'sale_item_id': s.sale_item_id,
                'sale_id': s.sale_id,
                'product_id': s.product_id,
                'quantity': s.quantity,
                'price': s.price,
                'amount': s.amount
            } for s in sale_items]
            return jsonify(sale_item_list)


api.add_resource(SaleItemResource, '/sale_item',
                 '/sale_item/<int:sale_item_id>')


class UserResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username is required')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password is required')

        args = parser.parse_args()
        username = args['username']
        password = args['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'})


api.add_resource(UserResource, '/user', '/user/<int:user_id>')


class OrderResource(Resource):

    def get(self, order_id=None):
        if order_id:
            order = Order.query.get(order_id)
            if order:
                return jsonify({
                    'order_id': order.order_id,
                    'customer_id': order.customer_id,
                    'order_date': order.order_date,
                    'total_amount': order.total_amount,
                    'payment_method': order.payment_method,
                    'notes': order.notes
                })
            else:
                return jsonify({'message': 'Order not found'}), 404
        else:
            orders = Order.query.all()
            order_list = [{
                'order_id': o.order_id,
                'customer_id': o.customer_id,
                'order_date': o.order_date,
                'total_amount': o.total_amount,
                'payment_method': o.payment_method,
                'notes': o.notes
            } for o in orders]
            return jsonify(order_list)


api.add_resource(OrderResource, '/order', '/order/<int:order_id>')


class OrderItemResource(Resource):

    def get(self, order_item_id):
        order_item = OrderItem.query.get(order_item_id)
        if order_item_id:
            if order_item:
                return jsonify({
                    'order_item_id': order_item.order_item_id,
                    'order_id': order_item.order_id,
                    'product_id': order_item.product_id,
                    'quantity': order_item.quantity,
                    'unit_price': order_item.unit_price,
                    'item_amount': order_item.item_amount
                })
            else:
                return jsonify({'message': 'Order item not found'}), 404
        else:
            order_items = OrderItem.query.all()
            order_item_list = [{
                'order_item_id': o.order_item_id,
                'order_id': o.order_id,
                'product_id': o.product_id,
                'quantity': o.quantity,
                'unit_price': o.unit_price,
                'item_amount': o.item_amount
            } for o in order_items]
            return jsonify(order_item_list)


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
