
from app.models.animal import Animal
from app.service.animal_service import Animal_service
from app.repositories.animal_repo import Animal_repo

def test_get_list_animal_success(mocker):

    #Arrange
    mock_animal_data = [
        Animal(
            age= 1,
            animal_class= "Mammal",
            diet_category= "Carnivore",
            food= "Meat",
            gender= "Male",
            id= 1,
            name= "Catty",
            species= "Cat",
        ),
        Animal(
            age= 1,
            animal_class= "Bird",
            diet_category= "Carnivore",
            food= "Meat",
            gender= "Male",
            id= 2,
            name= "Eagly",
            species= "Eagle"
        ),
    ]
    mocker.patch.object(Animal_repo, 'get_list_animal', return_value=mock_animal_data)

    #Act
    animal_service = Animal_service().get_animals()

    #Assert
    assert len(animal_service) == 2
    assert animal_service[0]['name'] == 'Catty'
    assert animal_service[1]['species'] == 'Eagle'


# def test_create_animal_success(test_app, mocker):

#     mock_animal_data = Animal(
#             age= 1,
#             anima_class= "Mammal",
#             diet_category= "Carnivore",
#             food= "Meat",
#             gender= "Male",
#             id= 1,
#             name= "Catty",
#             species= "Cat"
#         ),
#     mocker.patch.object(Animal_repo, 'create_animal', return_value=mock_animal_data)

    

    # animal_service_create = test_app.post("/animal/", json=Animal_service().create_animal())
    
    # assert animal_service_create.json['data']['name'] == "Catty"
    # assert animal_service_create.status_code == 201

    
def test_update_animal_success(test_app, mocker):

    mock_animal_data = Animal(
            age= 1,
            animal_class= "Mammal",
            diet_category= "Carnivore",
            food= "Meat",
            gender= "Male",
            id= 1,
            name= "Catty",
            species= "Cat"
        ),
    mocker.patch.object(Animal_repo, 'update_animal', return_value=mock_animal_data)

    

    animal_service_update = test_app.post("/animal/1", json=Animal_service().update_animal(id, mock_animal_data))
    
    assert animal_service_update.json['data']['name'] == "Catty"
    assert animal_service_update.status_code == 201

