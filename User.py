from flask import jsonify, request
from flask_restful import Resource, reqparse
from database import db, User
from werkzeug.security import generate_password_hash
import re


class UserResource(Resource):

    def post(self):
        try:
            