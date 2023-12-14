from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from database import db, Warehouse

app = Flask(__name__)
Api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///POS.sqlite'


class WarehouseResource(Resource):

    def get(self, warehouse_id=None):
        try:
            if warehouse_id is None:
                warehouses = Warehouse.query.all()
                return jsonify([warehouse.to_dict() for warehouse in warehouses])
            else:
                warehouse = Warehouse.query.get(warehouse_id)
                return jsonify(warehouse.to_dict())
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def post(self, warehouse_id=None):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('warehouse_name', type=str, required=True)
            parser.add_argument('warehouse_address', type=str)
            parser.add_argument('warehouse_phone_number', type=str)
            parser.add_argument('warehouse_email', type=str)
            args = parser.parse_args()

            if warehouse_id is None:
                warehouse = Warehouse(
                    warehouse_name=args['warehouse_name'],
                    warehouse_address=args['warehouse_address'],
                    warehouse_phone_number=args['warehouse_phone_number'],
                    warehouse_email=args['warehouse_email']
                )
                db.session.add(warehouse)
                db.session.commit()
                return jsonify(warehouse.to_dict()), 201
            else:
                warehouse = Warehouse.query.get(warehouse_id)
                if warehouse is None:
                    return {'message': 'Warehouse not found'}, 404

                warehouse.warehouse_name = args['warehouse_name']
                warehouse.warehouse_address = args['warehouse_address']
                warehouse.warehouse_phone_number = args['warehouse_phone_number']
                warehouse.warehouse_email = args['warehouse_email']
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def put(self, warehouse_id=None):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('warehouse_name', type=str)
            parser.add_argument('warehouse_address', type=str)
            parser.add_argument('warehouse_phone_number', type=str)
            parser.add_argument('warehouse_email', type=str)
            args = parser.parse_args()

            warehouse = Warehouse.query.get(warehouse_id)
            if warehouse is None:
                return {'message': 'Warehouse not found'}, 404

            if args['warehouse_name'] is not None:
                warehouse.warehouse_name = args['warehouse_name']
            if args['warehouse_address'] is not None:
                warehouse.warehouse_address = args['warehouse_address']
            if args['warehouse_phone_number'] is not None:
                warehouse.warehouse_phone_number = args['warehouse_phone_number']
            if args['warehouse_email'] is not None:
                warehouse.warehouse_email = args['warehouse_email']

            db.session.commit()
            return jsonify(warehouse.to_dict())
        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500
