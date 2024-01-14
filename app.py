from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from database import db, Product

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products/", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        product = Product()