from flask import jsonify
from flask_restful import Resource, reqparse
from database import db, User
from werkzeug.security import generate_password_hash
import re


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

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        if not (3 <= len(username) <= 20):
            return jsonify({'message': 'Username must be between 3 and 20 characters'}), 400

        if not re.match('^[a-zA-Z0-9_]+$', username):
            return jsonify({'message': 'Username can only contain letters, numbers, and underscores'}), 400

        if len(password) < 12:
            return jsonify({'message': 'Password must be at least 12 characters'}), 400

        if not (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)):
            return jsonify({'message': 'Weak password. It must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'}), 400

        common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]

        if password.lower() in common_passwords or re.match(r"\b\w+123\b", password.lower()):
            return jsonify({'message': 'Weak password. Please choose a different password.'}), 400

        if not (len(set(password) - set(username)) > 5 and len(set(password) - set(username[::-1])) > 5):
            return jsonify({'message': 'Password is too similar to the username. It should differ by at least 6 characters.'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'})
