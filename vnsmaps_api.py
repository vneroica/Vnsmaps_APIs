from flask import Flask
from flask import jsonify
from flask import request

from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Vnsmaps"
mongo = PyMongo(app)

@app.route('/init', methods=['POST'])
def device_init():
    devices_db = mongo.db.devices
    device_id = int(request.json['device_id'])
    device = devices_db.findone({'device_id': device_id})

    if device:
        if device['status'] == 0:
            device['status'] = 1
            devices_db.save(device)
            return jsonify ({"status":"ok"})

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


