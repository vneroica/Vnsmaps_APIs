from flask import Flask
from flask import jsonify
from flask import request
import datetime

from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Vnsmaps"
mongo = PyMongo(app)

@app.route('/init', methods=['POST'])
def device_init():
    devices_db = mongo.db.Devices
    logs = mongo.db.logs
    if not "device_id" in request.form:
        logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
        return jsonify({"status":"fail", "detail":"bad_data"}), 419
    else:
        
        device_id = int(request.form['device_id'])
        print (device_id)
        device = devices_db.find_one({'device_id': device_id})

        print (device)

        if device:
            if device['status'] == 0:
                device['status'] = 1
                devices_db.save(device)
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"ok"})
                return jsonify ({"status":"ok"}) , 200
            else:
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
                return jsonify ({"status":"fail","details":"device_already_activated"})
        else:
            logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
            return jsonify ({"status":"fail","details":"device_id_incorrect"}), 422

@app.route('/sendgps', methods=['POST'])
def sendgps():
    devices_db = mongo.db.Gpsdata
    logs = mongo.db.logs
    if not all(key in request.form for key in ('device_id', 'long', 'lat', 'speed', 'odbII', 'time')):
        logs.insert_one({"time": datetime.datetime.now(), "api":"sendgps", "status":"fail"})
        return jsonify({"status":"fail", "detail":"bad_data"}), 419
    else:
        
        devices_db.insert_one({"device_id": request.form['device_id'], "long": request.form['long'], "lat"
                               : request.form['lat'], "speed": request.form['speed'], "odbII": request.form['odbII']})
        logs.insert_one({"time": datetime.datetime.now(), "api":"sendgps", "status":"ok"})
        return jsonify ({"status":"ok"}) , 200

@app.route('/sendgrcode', methods=['POST'])
def sendqrcode():
    devices_db = mongo.db.Devices
    logs = mongo.db.logs
    if not "device_id" in request.form:
        logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
        return jsonify({"status":"fail", "detail":"data_incorrect"}), 419
    else:
        
        device_id = int(request.form['device_id'])
        print (device_id)
        device = devices_db.find_one({'device_id': device_id})

        print (device)

        if device:
            if device['status'] == 0:
                device['status'] = 1
                devices_db.save(device)
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"ok"})
                return jsonify ({"status":"ok"}) , 200
            else:
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
                return jsonify ({"status":"fail","details":"device_already_activated"})
        else:
            logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
            return jsonify ({"status":"fail","details":"device_id_incorrect"}), 422

@app.route('/sendweight', methods=['POST'])
def sendweight():
    devices_db = mongo.db.Devices
    logs = mongo.db.logs
    if not "device_id" in request.form:
        logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
        return jsonify({"status":"fail", "detail":"data_incorrect"}), 419
    else:
        
        device_id = int(request.form['device_id'])
        print (device_id)
        device = devices_db.find_one({'device_id': device_id})

        print (device)

        if device:
            if device['status'] == 0:
                device['status'] = 1
                devices_db.save(device)
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"ok"})
                return jsonify ({"status":"ok"}) , 200
            else:
                logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
                return jsonify ({"status":"fail","details":"device_already_activated"})
        else:
            logs.insert_one({"time": datetime.datetime.now(), "api":"init", "status":"fail"})
            return jsonify ({"status":"fail","details":"device_id_incorrect"}), 422


if __name__ == '__main__':
   app.run(debug=True)


