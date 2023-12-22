from flask import Flask, render_template
from flask_restful import Api
from ProductResource import ProductResource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    render_template("index.html")

product = ProductResource()

if __name__ == "__main__":
    app.run()
