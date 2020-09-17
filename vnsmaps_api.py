from flask import Flask
from flask import jsonify

from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Vnsmaps"
mongo = PyMongo(app)

@app.route('/init', methods=['POST'])
def device_init():
    return jsonify({"status":"OK"})

@app.route('/sendgps', methods=['POST'])
def sendgps():
    return jsonify({"status":"OK"})

@app.route('/sendgrcode', methods=['POST'])
def sendqrcode():
    return jsonify({"status":"OK"})

@app.route('/sendweight', methods=['POST'])
def sendweight():
    return jsonify({"status":"OK"})


if __name__ == '__main__':
   app.run()


