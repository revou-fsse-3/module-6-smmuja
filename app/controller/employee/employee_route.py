from flask import Blueprint, jsonify, request
# from app import app
from app.utils.database import db
from app.models.employee import Employee

employee_blueprint = Blueprint('employee_endpoint', __name__)



@employee_blueprint.route('/', methods=['GET'])
def get_list_employee():
    try:
        employees = Employee.query.all()

        return [employee.as_dict() for employee in employees], 200
    except Exception as e:
        return str(e), 500

@employee_blueprint.route('/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return 'Employee not found', 404

        return employee.as_dict(), 200
    except Exception as e:
        return str(e), 500

@employee_blueprint.route('/', methods=['POST'])
def create_employee():
    try:
        data = request.json
        print(data)

        employee = Employee()
        # employee.id = data['id']
        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']
        employee.role = data['role']
        employee.schedule = data['schedule']
        db.session.add(employee)
        db.session.commit()
        
        # return 'Employee created', 201
        return employee.as_dict(), 201
    except Exception as e:
        return e, 500

@employee_blueprint.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:

        employee = Employee.query.get(employee_id)

        if not employee:
            return 'Employee not found', 404
        data = request.json

        employee = Employee()
        # employee.id = data['id']
        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']
        employee.role = data['role']
        employee.schedule = data['schedule']
        # db.session.add(employee)
        db.session.commit()
    
        
        # return 'Update successful', 200
        return employee.as_dict(), 200
    except Exception as e:
        return e, 500

@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:

        employee = Employee.query.get(employee_id)

        if not employee:
            return 'Employee not found', 404
        data = request.json

        employee = Employee()
        # employee.id = data['id']
        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']
        employee.role = data['role']
        employee.schedule = data['schedule']
        db.session.delete(employee)
        db.session.commit()
    
        
        # return 'Update successful', 200
        return employee, 200
    except Exception as e:
        return e, 500
