from app.service.employee_service import Employee_service


def test_get_employee(test_app, mocker):

    mock_employee_data = [
        {
            "email": "Mia@email.com",
            "id": 2,
            "name": "Mia",
            "phone": 12345,
            "role": "Dolphin Trainer",
            "schedule": "Afternoon shift"
        }
    ]
    mocker.patch.object(Employee_service, 'get_employees', return_value=mock_employee_data)

    response = test_app.get("/employee/")

    assert response.status_code == 200
    assert response.json['data'] == mock_employee_data
    assert len(response.json['data']) == len(mock_employee_data)


# def test_post_employee(test_app, mocker):
    
#     data =  {
#             "email": "Mia@email.com",
#             # "id": 2,
#             "name": "Mia",
#             "phone": 12345,
#             "role": "Dolphin Trainer",
#             "schedule": "Afternoon shift"
#             }

#     mocker.patch.object(Employee_service, 'create_employee', return_value=data)

    
#     response = test_app.post("/employee/", json=data)

    
#     assert response.status_code == 201
#     assert response.json['data']["name"] == "Mia"

def test_put_employee(test_app, mocker):
    
    data ={
        "email": "Mia@email.com",
        # "id": 2,
        "name": "Mia",
        "phone": 12345,
        "role": "Dolphin Trainer",
        "schedule": "Afternoon shift"
        }

    mocker.patch.object(Employee_service, 'update_employee', return_value=data)

    
    response = test_app.put("/employee/2", json=data)

    
    assert response.status_code == 200

def test_put_employee_code_400(test_app, mocker):
    
    data ={}

    mocker.patch.object(Employee_service, 'update_employee', return_value=data)
    response = test_app.put("/employee/", json=data)
    assert response.status_code == 405


def test_delete_employee_not_found(test_app, mocker):
    
    expected_response = "Employee not found"
    
    mocker.patch.object(Employee_service, "delete_employee", return_value=expected_response)

    #Act
    response = test_app.delete("/employee/59")

    #Assert
    assert response.status_code == 404


def test_delete_employee (test_app, mocker):

    expected_response = {
        "data": None,
        "status": {
            "code": 200,
            "message": "Employee deleted"
        }
    }

    mocker.patch.object(Employee_service, "delete_employee", return_value=expected_response)

    response = test_app.delete("/employee/2")

    assert response.status_code == 200

def test_search_employee_by_id(test_app, mocker):

    expected_data =  [
            {
            "email": "Mia@email.com",
            # "id": 2,
            "name": "Mia",
            "phone": 12345,
            "role": "Dolphin Trainer",
            "schedule": "Afternoon shift"
            }
    ]
    
    expected_response = {
        'data': expected_data,
        'status': {
            "code": 200,
            "message": ""
        }
    }


    mocker.patch.object(Employee_service, 'search_employee', return_value=expected_response)

    response = test_app.get("/employee/search?name=Mia")

    assert response.status_code == 200
    assert response.json['data'] == expected_response