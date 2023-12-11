from flask import jsonify
from flask_restful import Resource
from database import db, Sale


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
                'total_amount': s.total_amount,
                'payment_method': s.payment_method,
                'notes': s.notes
            } for s in sales]
            return jsonify(sale_list)