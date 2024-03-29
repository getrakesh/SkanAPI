from flask import Flask, request
import json
from bson.json_util import dumps
# importing PyMongo client
from pymongo import MongoClient

# Understanding import
# from then name of installed package then the class/module name ( MongoClient is in pymongo package)

client = MongoClient('localhost:27017')
db = client.ContactDB

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World......API....."


# Simple Post API
@app.route("/add_contact", methods=['POST'])
def add_contact():
    try:
        data = request.get_json()
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = db.Contacts.insert_one({
                "name": user_name,
                "contact": user_contact
            })
            return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/get_all_contact", methods=['GET'])
def get_all_contact():
    try:
        contacts = db.Contacts.find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
