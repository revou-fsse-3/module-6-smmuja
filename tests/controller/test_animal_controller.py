# from app.services.animal_services import Animal_service
# from app.controller.animal.animal_route import Animal_service
from app.service.animal_service import Animal_service
from app import db


def test_get_animal(test_app, mocker):

    mock_animal_data = [
            {
            "age": 1,
            "animal class": "Mammal",
            "diet category": "Carnivore",
            "food": "Meat",
            "gender": "Male",
            "id": 1,
            "name": "Catty",
            "species": "Cat"
            }
    ]
    mocker.patch.object(Animal_service, 'get_animals', return_value=mock_animal_data)


    response = test_app.get("/animal/")

    assert response.status_code == 200
    assert response.json['data'] == mock_animal_data
    assert len(response.json['data']) == len(mock_animal_data)

#  POST

# def test_post_animal(test_app, mocker):
#     #Arrange
#     data = {
#             "age": 1,
#             "animal class": "Mammal",
#             "diet category": "Carnivore",
#             "food": "Meat",
#             "gender": "Male",
#             "id": 1,
#             "name": "Catty",
#             "species": "Cat"
#             }
#     mocker.patch.object(Animal_service, 'create_animal', return_value=data)

    
#     response = test_app.post("/animal/", json=data)

    
#     assert response.status_code == 201
#     assert response.json['data']["name"] == "Catty"

# UPDATE
def test_put_animal(test_app, mocker):
    
    data ={
            "age": 1,
            "animal class": "Mammal",
            "diet category": "Carnivore",
            "food": "Meat",
            "gender": "Male",
            "id": 1,
            "name": "Catty",
            "species": "Cat"
            }
    mocker.patch.object(Animal_service, 'update_animal', return_value=data)

    
    response = test_app.put("/animal/3", json=data)

    
    assert response.status_code == 200

def test_put_animal_code_400(test_app, mocker):
    
    data ={}

    mocker.patch.object(Animal_service, 'update_animal', return_value=data)
    response = test_app.put("/animal/", json=data)
    assert response.status_code == 405


def test_delete_animal_not_found(test_app, mocker):
    
    expected_response = "Not found"
    
    mocker.patch.object(Animal_service, "delete_animal", return_value=expected_response)

    
    response = test_app.delete("/animal/56")

    
    assert response.status_code == 404


def test_delete_animal (test_app, mocker):

    expected_response = {
        "data": None,
        "status": {
            "code": 200,
            "message": "Animal deleted"
        }
    }

    mocker.patch.object(Animal_service, "delete_animal", return_value=expected_response)

    response = test_app.delete("/animal/3")

    assert response.status_code == 200

def test_search_animal_by_id(test_app, mocker):

    expected_data =  [
        {
            "age": 1,
            "animal class": "Mammal",
            "diet category": "Carnivore",
            "food": "Meat",
            "gender": "Male",
            "id": 1,
            "name": "Catty",
            "species": "Cat"
            }
    ]
    
    expected_response = {
        'data': expected_data,
        'status': {
            "code": 200,
            "message": ""
        }
    }


    mocker.patch.object(Animal_service, 'search_animal', return_value=expected_response)

    
    response = test_app.get("/animal/search?name=Catty")

    
    assert response.status_code == 200
    assert response.json['data'] == expected_response