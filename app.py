from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from patient import Patients, Patient
from doctor import Doctors, Doctor
from appointment import Appointments, Appointment
from common import Common
from staff import Staffs, Staff
import json

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:id>')
api.add_resource(Common, '/common')
api.add_resource(Staffs, '/staff')
api.add_resource(Staff, '/staff/<int:id>')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])