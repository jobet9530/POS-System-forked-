from flask import jsonify
from flask_restful import Resource
from database import db, SaleItem

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
