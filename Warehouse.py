from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from database import db, Warehouse


class WarehouseResource(Resource):
    def post(self, warehouse_id=None):
        try:
            if warehouse_id:
                parser = reqparse.RequestParser()
                parser.add_argument('warehouse_name', required=True)
                parser.add_argument('warehouse_address', required=True)
                parser.add_argument('warehouse_phone', required=True)
                parser.add_argument('warehouse_email', required=True)
                args = parser.parse_args()
                warehouse = Warehouse.query.get(warehouse_id)
                if not warehouse:
                    return jsonify({'message': 'Warehouse not found'}), 404
                warehouse.warehouse_name = args['warehouse_name']
                warehouse.warehouse_address = args['warehouse_address']
                warehouse.warehouse_phone = args['warehouse_phone']
                warehouse.warehouse_email = args['warehouse_email']
                db.session.commit()
                return warehouse
            else:
                parser = reqparse.RequestParser()
                parser.add_argument('warehouse_name', required=True)
                parser.add_argument('warehouse_address', required=True)
                parser.add_argument('warehouse_phone', required=True)
                parser.add_argument('warehouse_email', required=True)
                args = parser.parse_args()
                new_warehouse = Warehouse(
                    warehouse_name=args['warehouse_name'],
                    warehouse_address=args['warehouse_address'],
                    warehouse_phone=args['warehouse_phone'],
                    warehouse_email=args['warehouse_email'],
                    warehouse_id=warehouse_id
                )
                db.session.add(new_warehouse)
                db.session.commit()
                return new_warehouse
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def get(self, warehouse_id=None):
        try:
            if warehouse_id:
                warehouse = Warehouse.query.get(warehouse_id)
                if not warehouse:
                    return jsonify({'message': 'Warehouse not found'}), 404
                return warehouse
            else:
                warehouses = Warehouse.query.all()
                return warehouses
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def put(self, warehouse_id=None):
        try:
            if warehouse_id:
                parser = reqparse.RequestParser()
                parser.add_argument('warehouse_name', required=True)
                parser.add_argument('warehouse_address', required=True)
                parser.add_argument('warehouse_phone', required=True)
                parser.add_argument('warehouse_email', required=True)
                args = parser.parse_args()
                warehouse = Warehouse.query.get(warehouse_id)
                if not warehouse:
                    return jsonify({'message': 'Warehouse not found'}), 404
                warehouse.warehouse_name = args['warehouse_name']
                warehouse.warehouse_address = args['warehouse_address']
                warehouse.warehouse_phone = args['warehouse_phone']
                warehouse.warehouse_email = args['warehouse_email']
                db.session.commit()
                return warehouse
            else:
                return jsonify({'message': 'Warehouse id is required'}), 400
        except Exception as e:
            return jsonify({'message': str(e)}), 500
