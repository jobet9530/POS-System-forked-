from flask import Flask, request, jsonify
from database import db, Product
from flask_restful import Resource
import barcode
from barcode.writer import ImageWriter

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class ProductResource(Resource):
    @app.route('/product', methods=['GET'])
    def get(self):
        try:
            category = request.args.get('category')
            if category:
                products = Product.query.filter_by(category=category).all()
                if not products:
                    return jsonify({'message': 'Products not found'}), 404
                elif category is None:
                    return jsonify({'message': 'Category is required'}), 400
                else:
                    result = []
                    for product in products:
                        result.append({
                            'product_id': product.product_id,
                            'product_name': product.product_name,
                            'price': product.price,
                            'stock_quantity': product.stock_quantity,
                            'barcode': product.barcode,
                            'category': product.category
                        })
                    return jsonify({'products': result, 'message': 'Products Retrieve successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @app.route('/product', methods=['POST'])
    def post(self):
        try:
            data = request.get_json()
            if not all(key in data for key in ['product_name', 'price', 'stock_quantity', 'barcode', 'category']):
                return jsonify({'error': 'Missing required fields'}), 400
            existing_product = Product.query.filter_by(
                barcode=data['barcode']).first()
            if existing_product:
                return jsonify({'error': 'Product already exists with same barcode'}), 400

            new_product = Product(
                product_name=data['product_name'],
                price=data['price'],
                stock_quantity=data['stock_quantity'],
                generated_barcode=barcode(
                    writer=ImageWriter(),
                    data=data['barcode']
                ),
                category=data['category']
            )
            if new_product:
                if not all(key in data for key in ['product_name', 'price', 'stock_quantity', 'barcode', 'category']):
                    return jsonify({'error': 'Missing required fields'}), 400
                else:
                    generated_barcode = barcode(
                        data['barcode'], writer=barcode.writer.ImageWriter())
                    generated_barcode.save('barcode.png')
                    db.session.add(new_product)
                    db.session.commit()
                    return jsonify({'message': 'Product created successfully'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500
        finally:
            db.session.close()

    @app.route('/product/<int:product_id>', methods=['PUT'])
    def put(self, product_id):
        try:
            data = request.get_json()
            product = Product.query.filter_by(product_id=product_id)

            if not Product:
                return jsonify({'message': 'Product not found'}), 404

            if not all(key in data for key in ['product_name', 'price', 'stock_quantity', 'barcode', 'category']):
                return jsonify({'error': 'Missing required fields'}), 400

            if 'product_name' in data:
                product.product_name = data['product_name']
            if 'price' in data:
                product.price = data['price']
            if 'stock_quantity' in data:
                product.stock_quantity = data['stock_quantity']
            if 'barcode' in data:
                product.barcode = data['barcode']
            if 'category' in data:
                product.category = data['category']

            db.session.commit()
            return jsonify({'message': 'Product updated successfully'}), 200

        except Exception as e:
            return jsonify({'message': str(e)}), 500
        finally:
            db.session.close()

    @app.route('/product/<int:product_id>', methods=['DELETE'])
    def delete(self, product_id):
        try:
            product = Product.query.filter_by(product_id=product_id)

            if not product:
                return jsonify({'message': 'Product not found'}), 404
            elif product:
                db.session.delete(product)
                db.session.commit()
                return jsonify({'message': 'Product deleted successfully'}), 200

        except Exception as e:
            return jsonify({'message': str(e)}), 500
        finally:
            db.session.close()
