from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<pre>Hello, This is a webpage developed in Python Flask!\nCheck for /aboutme and /time</pre>'

@app.route('/aboutme')
def get_data():
    data = {
        "name": "Vamshi Krishna",
        "age": 33,
        "city": "Hyderabad"
    }
    return jsonify(data)

@app.route('/time')
def time():
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time_ist = datetime.now(ist_timezone)
    formatted_time = current_time_ist.strftime('%d-%m-%Y %H:%M:%S %Z%z')
 #   current_time = datetime.now()
    return str(formatted_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
