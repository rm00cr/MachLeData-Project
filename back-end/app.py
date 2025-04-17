
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
import datetime
import time
import requests
import json
import public_ip as ipf

from Model import Salaries, db



host = "localhost"#ipf.get() 
database = 'mydatabase'
user = 'myuser'
password = 'mypassword'
port = '5434'

# Create a connection string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)


@app.route('/')
def index():
    return 'Hallo'
    
@app.route('/save/', methods=['POST'])
def insert_salary():
    data = request.get_json()
    # Extract the data from the request
    work_year = data.get('work_year')
    experience_level = data.get('experience_level')
    employment_type = data.get('employment_type')
    job_title = data.get('job_title')
    salary = data.get('salary')
    salary_currency = data.get('salary_currency')
    salary_in_usd = data.get('salary_in_usd')
    employee_residence = data.get('employee_residence')
    remote_ratio = data.get('remote_ratio')
    company_location = data.get('company_location')
    company_size = data.get('company_size')
    # Create a new record
    new_salary = {
        'work_year': work_year,
        'experience_level': experience_level,
        'employment_type': employment_type,
        'job_title': job_title,
        'salary': salary,
        'salary_currency': salary_currency,
        'salary_in_usd': salary_in_usd,
        'employee_residence': employee_residence,
        'remote_ratio': remote_ratio,
        'company_location': company_location,
        'company_size': company_size,
    }
    # Send the data to the database
    db.session.add(new_salary)
    db.session.commit()
    return "success"

@app.route('/data/<id>', methods=['GET'])
def get_data(id):
    # Assuming you have a function to retrieve the data from the database
    # For example, using SQLAlchemy:
    records = Salaries.query.filter_by(id=id).all()
    # Convert the records to a list of dictionaries
    records = [{'id': record.id, 'work_year': record.work_year, 'experience_level': record.experience_level,
                'employment_type': record.employment_type, 'job_title': record.job_title,
                'salary': record.salary, 'salary_currency': record.salary_currency,
                'salary_in_usd': record.salary_in_usd, 'employee_residence': record.employee_residence,
                'remote_ratio': record.remote_ratio, 'company_location': record.company_location,
                'company_size': record.company_size} for record in records]
    return jsonify(records)


if __name__ == '__main__':
        app.run(
        host="0.0.0.0",
        debug=True,
        passthrough_errors=True,
        use_debugger=False,
        use_reloader=True,
    )
