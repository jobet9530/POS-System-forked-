from flask import jsonify, request
from flask_restful import Resource, reqparse
from database import db, User
from werkzeug.security import generate_password_hash
import re


class UserResource(Resource):

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True)
            parser.add_argument('email', type=str, required=True)
            parser.add_argument('password', type=str, required=True)
            args = parser.parse_args()

            # Validate email
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, args['email']):
                return {'message': 'Invalid email address'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {e}'}, 500

    def get(self):
        try:
            users = User.query.all()
            users = [{
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            }for user in users]

            return jsonify(users)
        except Exception as e:
            return str(e)

    def put(self):
        try:
            users = User.query.all()
            users = [{
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            }for user in users]

            user = User(
                username=request.json['username'],
                email=request.json['email'],
                password=generate_password_hash(request.json['password'])
            )
            db.session.add(user)
            db.session.commit()
