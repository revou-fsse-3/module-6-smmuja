from flask import Blueprint, jsonify, request
# from app import app
from app.utils.database import db
from app.models.employee import Employee
from app.utils.api_response import api_response
from app.service.employee_service import Employee_service
from app.controller.employee.schema.update_employee import Update_employee_request

employee_blueprint = Blueprint('employee_endpoint', __name__)



@employee_blueprint.route('/', methods=['GET'])
def get_list_employee():
    try:
        employee_service = Employee_service()
        employees = employee_service.get_employees()

        return api_response(
            status_code=200, 
            message='' ,
            data=employees
        )
    except Exception as e:
        return str(e), 500

@employee_blueprint.route('/search', methods=['GET'])
def search_employee():
    try:
        request_data = request.args
        employee_service = Employee_service()

        employees = employee_service.search_employee(request_data['name'])

        # if not employee_service:
        #     return "Employee not found", 404

        return api_response(
            status_code=200, 
            message='' ,
            data=employees
        )
    
        
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
        update_employee_request = Update_employee_request(**data)
        print(update_employee_request)

        employee = Employee()
        # employee.id = data['id']
        employee.name = data.get('name', employee.name)
        employee.email = data.get('email', employee.email)
        employee.phone = data.get('phone', employee.phone)
        employee.role = data.get('role', employee.role)
        employee.schedule = data.get('schedule', employee.schedule)
        # db.session.add(employee)
        # db.session.commit()
    
        
        employee_service = Employee_service()

        employees = employee_service.update_employee(employee_id, employee)
        
        return api_response(
            status_code=200, 
            message='Updated' ,
            data=employees
        )
    except Exception as e:
        return api_response(
            status_code=500, 
            message=e.errors() ,
            data={}
        )

@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        employee_service = Employee_service()
        is_deleted = employee_service.delete_employee(employee_id)

        if not employee_service:
            return 'Not found', 404

        if is_deleted == 'Not found':
            return api_response(
                status_code=404,
                message=is_deleted,
                data='none'
            )
        
        return api_response(
            status_code=200,
            message='Employee deleted',
            data=is_deleted
        )

        
        # db.session.delete(employee)
        # db.session.commit()
        
    except Exception as e:
        return api_response(
            status_code=500,
            message = str(e),
            data={}
        )
    