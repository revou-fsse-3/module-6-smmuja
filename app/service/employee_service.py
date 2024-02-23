from app.models.employee import Employee
from app.repositories.employee_repo import Employee_repo

class Employee_service:
    def __init__(self) :
        self.employee_repo= Employee_repo()
        
    def get_employees(self):
        employees = self.employee_repo.get_list_employee()
        return [employee.as_dict() for employee in employees]
    
    def search_employee(self, name):
        employees = self.employee_repo.search_employee(name)
        return [employee.as_dict() for employee in employees]

    
    def update_employee(self, id, employee_data):
        updated_employee = self.employee_repo.update_employee(id, employee_data)
        return updated_employee

    def delete_employee(self, id):
        employee= Employee.query.get(id)

        if not employee:
            return 'Employee not found'

        is_deleted = self.employee_repo.delete_employee(id)
        return is_deleted.as_dict()



