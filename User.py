from flask import jsonify
from flask_restful import Resource, reqparse
from database import db, User
from werkzeug.security import generate_password_hash


class UserResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username is required')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password is required')

        args = parser.parse_args()
        username = args['username']
        password = args['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'})
