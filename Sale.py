from flask import jsonify, request
from flask_restful import Resource
from database import db, Sale, Product


class SaleResource(Resource):

    def get(self):
        try:
            sales = db.session.query(Sale, Product).join(
                Product, Sale.product_id == Product.product_id).all()
            sales_list = [{
                'sale_id': sale[0].sale_id,
                'customer_id': sale[0].customer_id,
                'product_id': sale[0].product_id,
                'sales_date': sale[0].sales_date,
                'total_amount': sale[0].total_amount,
                'payment_method': sale[0].payment_method,
                'notes': sale[0].notes,
                'product': {
                    'product_id': sale[1].product_id,
                    'product_name': sale[1].product_name,
                    'price': sale[1].price,
                    'quantity': sale[1].quantity
                }
            }for sale in sales]
            return jsonify(sales_list)
        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            sales = []
            customer_id = request.json['customer_id']
            product_id = request.json['product_id']
            sales_date = request.json['sales_date']
            total_amount = request.json['total_amount']
            payment_method = request.json['payment_method']
            notes = request.json['notes']

            product = db.session.query(Product).filter_by(
                product_id=product_id).first()

            sale = Sale(
                customer_id=customer_id,
                product_id=product_id,
                sales_date=sales_date,
                total_amount=total_amount,
                payment_method=payment_method,
                notes=notes
            )

            db.session.add(sale)
            db.session.commit()

            return jsonify({
                'sale_id': sale.sale_id,
                'customer_id': sale.customer_id,
                'product_id': sale.product_id,
                'sales_date': sale.sales_date,
                'total_amount': sale.total_amount,
                'payment_method': sale.payment_method,
                'notes': sales.notes,
                'product': {
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'price': product.price,
                    'quantity': product.quantity
                }
            })
        except Exception as e:
            return {'error': str(e)}

    def put(self):
        try:
            sale_id = request.json['sale_id']
            customer_id = request.json['customer_id']
            product_id = request.json['product_id']
            sales_date = request.json['sales_date']
            total_amount = request.json['total_amount']
            payment_method = request.json['payment_method']
            notes = request.json['notes']

            sale = db.session.query(Sale).filter_by(
                sale_id=sale_id).first()

            sale.customer_id = customer_id
            sale.product_id = product_id
            sale.sales_date = sales_date
            sale.total_amount = total_amount
            sale.payment_method = payment_method
            sale.notes = notes

            db.session.commit()

            return jsonify({
                'sale_id': sale.sale_id,
                'customer_id': sale.customer_id,
                'product_id': sale.product_id,
                'sales_date': sale.sales_date,
                'total_amount': sale.total_amount,
                'payment_method': sale.payment_method,
                'notes': sale.notes
            })
        except Exception as e:
            return {'error': str(e)}
