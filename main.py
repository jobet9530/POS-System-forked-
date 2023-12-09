from flask import Flask, jsonify, render_template, url_for
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from database import db, Product  # Import Product from the database module

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


api.add_resource(ProductResource, '/product', '/product/<int:product_id>')


@app.route('/api/data')
def get_data():
    data = {'status': 'success', 'message': 'Data fetched successfully'}
    return jsonify(data)


@app.route('/')
def render_frontend():
    api_response = {'status': 'success', 'message': 'API data endpoint'}
    return render_template('index.html', api_data=api_response, css_url=url_for('static', filename='/style.css'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
