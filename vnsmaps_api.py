from flask import Flask
from flask import jsonify


app = Flask(__name__)
@app.route('/init')
def device_init():
    return jsonify({"status":"OK"})
if __name__ == '__main__':
   app.run()
