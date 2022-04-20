from flask import Flask, json, request
from flask_cors import CORS
import db

app = Flask(__name__)
cors = CORS(app)

my_client = db.connect_to_db()


# GET all data
@app.route("/home", methods=["GET"])
def get_all_data():
    data = db.get_all_data(my_client)
    response = app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    return response


# POST a new type
@app.route("/type/new", methods=["POST"])
def add_new_terms():
    terms = request.json
    print("---received terms--")
    print(terms)
    db.add_new_terms(terms, my_client)
    response = app.response_class(response="Terms added to the database", status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run()
