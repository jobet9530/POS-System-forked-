from flask import jsonify, request
from flask_restful import Resource
from database import db, Sale, Customer, Product


class SaleResource(Resource):

    def get(self):
        try:
            sales = Sale.query(Sale, Customer, Product).join(
                Customer, Sale.customer_id == Customer.customer_id).join(
                Product, Sale.product_id == Product.product_id).all()
            sales = [{
                'sale_id': sale[0].sale_id,
                'customer_id': sale[0].customer_id,
                'customer_name': sale[1].customer_name,
                'product_id': sale[0].product_id,
                'product_name': sale[2].product_name,
                'quantity': sale[0].quantity,
                'price': sale[0].price
            }for sale in sales]

            return jsonify(sales)
        except Exception as e:
            return str(e)

    def post(self):
        try:
            sales = Sale.query(Sale, Customer, Product).join(
                Customer, Sale.customer_id == Customer.customer_id).join(
                Product, Sale.product_id == Product.product_id).all()
            sales = [{
                'sale_id': sale[0].sale_id,
                'customer_id': sale[0].customer_id,
                'customer_name': sale[1].customer_name,
                'product_id': sale[0].product_id,
                'product_name': sale[2].product_name,
                'quantity': sale[0].quantity,
                'price': sale[0].price
            }for sale in sales]

            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )
            db.session.add(product)
            db.session.commit()
        except Exception as e:
            return str(e)

    def put(self):
        try:
            sales = Sale.query(Sale, Customer, Product).join(
                Customer, Sale.customer_id == Customer.customer_id).join(
                Product, Sale.product_id == Product.product_id).all()
            sales = [{
                'sale_id': sale[0].sale_id,
                'customer_id': sale[0].customer_id,
                'customer_name': sale[1].customer_name,
                'product_id': sale[0].product_id,
                'product_name': sale[2].product_name,
                'quantity': sale[0].quantity,
                'price': sale[0].price
            }for sale in sales]

            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )
            db.session.add(product)
            db.session.commit()
        except Exception as e:
            return str(e)
