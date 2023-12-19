from flask import jsonify, request
from flask_restful import Resource, reqparse
from database import db, Warehouse, WarehouseItem, Product


class WarehouseItemResource(Resource):

    def get(self):
        try:
            warehouse_item = WarehouseItem.query(Warehouse, WarehouseItem, Product).join(
                Product, WarehouseItem.product_id == Product.id).join(Warehouse, WarehouseItem.warehouse_id == Warehouse.id).all()
            warehouse_item = [{
                'warehouse_item_id': warehouse_item[0].id,
                'product_name': warehouse_item[1].name,
                'warehouse_name': warehouse_item[2].name,
                'quantity': warehouse_item[0].quantity
            }for item in warehouse_item]
            return jsonify(warehouse_item)
        except Exception as e:
            return jsonify({'error': str(e)})

    def post(self):
        try:
            warehouse_item = WarehouseItem.query(Warehouse, WarehouseItem, Product).join(
                Product, WarehouseItem.product_id == Product.id).join(Warehouse, WarehouseItem.warehouse_id == Warehouse.id).join(Warehouse, WarehouseItem.warehouse_id == Warehouse.id).all()
            warehouse_item = [{
                'warehouse_item_id': warehouse_item[0].id,
                'product_name': warehouse_item[1].name,
                'warehouse_name': warehouse_item[2].name,
                'quantity': warehouse_item[0].quantity
            }for item in warehouse_item]
            warehouse = Warehouse(
                warehouse_name=request.json['warehouse_name'],
                warehouse_address=request.json['warehouse_address'],
                warehouse_phone_number=request.json['warehouse_phone_number'],
                warehouse_email=request.json['warehouse_email']
            )
            db.session.add(warehouse)
            db.session.commit()

            product = Product(
                product_name=request.json['product_name'],
                price=request.json['price'],
                stock_quantity=request.json['stock_quantity'],
                barcode=request.json['barcode'],
                category=request.json['category']
            )
            db.session.add(product)
            db.session.commit()
            return jsonify(warehouse_item)
        except Exception as e:
            return jsonify({'error': str(e)})

    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('warehouse_name', type=str, required=True,
                                location='json', help='Missing warehouse name')
            warehouse_item = WarehouseItem.query(Warehouse, WarehouseItem, Product).join(
                Product, WarehouseItem.product_id == Product.id).join(Warehouse, WarehouseItem.warehouse_id == Warehouse.id).join(Warehouse, WarehouseItem.warehouse_id == Warehouse.id).all()
            warehouse_item = [{
                'warehouse_item_id': warehouse_item[0].id,
                'product_name': warehouse_item[1].name,
                'warehouse_name': warehouse_item[2].name,
                'quantity': warehouse_item[0].quantity
            }for item in warehouse_item]
            return jsonify(warehouse_item)
        except Exception as e:
            return jsonify({'error': str(e)})
