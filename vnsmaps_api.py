from flask import Flask
from flask import jsonify

from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Vnsmaps"
mongo = PyMongo(app)

@app.route('/init')
def device_init():
    return jsonify({"status":"OK"})

@app.route('/sendgps')
def sendgps():
    return jsonify({"status":"OK"})

@app.route('/sendgrcode')
def sendqrcode():
    return jsonify({"status":"OK"})

@app.route('/sendweight')
def sendweight():
    return jsonify({"status":"OK"})


if __name__ == '__main__':
   app.run()


