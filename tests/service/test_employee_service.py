
from app.models.employee import Employee
from app.service.employee_service import Employee_service
from app.repositories.employee_repo import Employee_repo

def test_get_list_employee_success(mocker):

    #Arrange
    mock_employee_data = [
        Employee(
            email= "Mia@email.com",
            id= 2,
            name= "Mia",
            phone= 12345,
            role= "Dolphin Trainer",
            schedule= "Afternoon shift"
        ),
        Employee(
            email= "Abi@email.com",
            id= 5,
            name= "Abi",
            phone= 12345,
            role= "Zoo Keeper",
            schedule= "Night shift"
        ),
    ]
    mocker.patch.object(Employee_repo, 'get_list_employee', return_value=mock_employee_data)

    #Act
    employee_service = Employee_service().get_employees()

    #Assert
    assert len(employee_service) == 2
    assert employee_service[0]['name'] == 'Mia'
    assert employee_service[1]['role'] == 'Zoo Keeper'


def test_update_employee_success(test_app, mocker):

    mock_employee_data = Employee(
            email= "Mia@email.com",
            id= 2,
            name= "Mia",
            phone= 12345,
            role= "Dolphin Trainer",
            schedule= "Afternoon shift"
        ),
    mocker.patch.object(Employee_repo, 'update_employee', return_value=mock_employee_data)



    employee_service_update = test_app.post("/employee/1", json=Employee_service().update_employee(id))
    
    assert employee_service_update.json['data']['name'] == "Mia"
    assert employee_service_update.status_code == 201