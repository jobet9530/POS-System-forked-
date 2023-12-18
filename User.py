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
