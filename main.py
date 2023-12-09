from flask import Flask, jsonify, render_template, url_for
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from database import db, Product, Customer, Sale

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///POS.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)


class ProductResource(Resource):
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get(product_id)
            if product:
                return jsonify({
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'price': product.price,
                    'stock_quantity': product.stock_quantity,
                    'barcode': product.barcode,
                    'category': product.category
                })
            else:
                return jsonify({'message': 'Product not found'}), 404
        else:
            products = Product.query.all()
            product_list = [{
                'product_id': p.product_id,
                'product_name': p.product_name,
                'price': p.price,
                'stock_quantity': p.stock_quantity,
                'barcode': p.barcode,
                'category': p.category
            } for p in products]
            return jsonify(product_list)

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str,
                            required=True, help='Product name is required')

        args = parser.parse_args()
        new_product_name = args['product_name']

        product = Product.query.get(product_id)
        if product:
            product.product_name = new_product_name
            db.session.commit()
            return jsonify({'message': 'Product updated successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404

    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404


api.add_resource(ProductResource, '/product', '/product/<int:product_id>')


class CustomerResource(Resource):
    def get(self, customer_id=None):
        if customer_id:
            customer = Customer.query.get(customer_id)
            if customer:
                return jsonify({
                    'customer_id': customer.customer_id,
                    'customer_name': customer.customer_name,
                    'customer_address': customer.customer_address,
                    'customer_phone': customer.customer_phone,
                    'customer_email': customer.customer_email
                })
            else:
                return jsonify({'message': 'Customer not found'}), 404
        else:
            customers = Customer.query.all()
            customer_list = [{
                'customer_id': c.customer_id,
                'customer_name': c.customer_name,
                'email': c.customer_email,
                'phone_address': c.customer_email,
                'address': c.customer_address
            }for c in customers]
            return jsonify(customer_list)


class SaleResource(Resource):
    def get(self, sale_id=None):
        if sale_id:
            sale = Sale.query.get(sale_id)
            if sale:
                return jsonify({
                    'sale_id': sale.sale_id,
                    'customer_id': sale.customer_id,
                    'product_id': sale.product_id,
                    'sale_date': sale.sale_date,
                    'quantity': sale.quantity,
                    'total_amount': sale.total_amount,
                    'payment_method': sale.payment_method,
                    'notes': sale.notes
                })
            else:
                return jsonify({'message': 'Sale not found'}), 404
        else:
            sales = Sale.query.all()
            sale_list = [{
                'sale_id': s.sale_id,
                'customer_id': s.customer_id,
                'product_id': s.product_id,
                'sale_date': s.sale_date,
                'quantity': s.quantity,
                'total_amount': s.total_amount,
                'payment_method': s.payment_method,
                'notes': s.notes
            }for s in sales]
            return jsonify(sale_list)


api.add_resource(SaleResource, '/sale', '/sale/<int:sale_id>')


@app.route('/api/data')
def get_data():
    data = {'status': 'success', 'message': 'Data fetched successfully'}
    return jsonify(data)


@app.route('/')
def render_frontend():
    api_response = {'status': 'success', 'message': 'API data endpoint'}
    return render_template('index.html', api_data=api_response, css_url=url_for('static', filename='style.css'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
