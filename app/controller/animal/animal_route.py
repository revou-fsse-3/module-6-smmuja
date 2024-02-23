from flask import Blueprint, jsonify, request
# from app import app
from app.utils.database import db
from app.models.animal import Animal
from app.utils.api_response import api_response
from app.service.animal_service import Animal_service
from app.controller.animal.schema.update_animal import Update_animal_request
from pydantic import ValidationError

animal_blueprint = Blueprint('animal_endpoint', __name__)



@animal_blueprint.route('/', methods=['GET'])
def get_list_animal():
    try:
        animal_service = Animal_service()
        # animals = Animal.query.all()
        animals = animal_service.get_animals()

        # return [animal.as_dict() for animal in animals], 200
        return api_response(
            status_code=200, 
            message='' ,
            data=animals
        )
    except Exception as e:
        return str(e), 500
    
    
@animal_blueprint.route('/search', methods=['GET'])
def search_animal():
    try:
        request_data = request.args
        animal_service = Animal_service()
        # animals = Animal.query.all()
        animals = animal_service.search_animal(request_data['name'])

        # return [animal.as_dict() for animal in animals], 200
        return api_response(
            status_code=200, 
            message='' ,
            data=animals
        )
    except Exception as e:
        return str(e), 500
    


@animal_blueprint.route('/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return 'Animal not found', 404

        return animal.as_dict(), 200
    except Exception as e:
        return str(e), 500

@animal_blueprint.route('/', methods=['POST'])
def create_animal():
    try:
        data = request.json
        print(data)

        animal = Animal()
        # animal.id = data['id']
        animal.name = data['name']
        animal.species = data['species']
        # animal.binomial_name = data['binomial name']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.food = data['food']
        animal.diet_category = data['diet category']
        # animal.animal_class = data['animal class']
        
        db.session.add(animal)
        db.session.commit()
        
        # return 'success', 201
        return animal.as_dict(), 201
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route('/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "Animal not found", 404
        
        data = request.json
        update_animal_request = Update_animal_request(**data)
        print(update_animal_request)
        # print(data)

        animal = Animal()
        # # # animal.id = data['id']
        # animal.name= update_animal_request.name
        # animal.species= update_animal_request.species
        # animal.age= update_animal_request.age
        # animal.gender= update_animal_request.gender
        # animal.food= update_animal_request.food
        # # animal.diet_category= update_animal_request.diet_category
        # animal.animal_class= update_animal_request.animal_class
        



        animal.name = data.get('name', animal.name)
        animal.species = data.get('species', animal.species)
        # animal.binomial_name = data['binomial name']
        animal.age = data.get('age', animal.age)
        animal.gender = data.get('gender', animal.gender)
        animal.food = data.get('food', animal.food)
        animal.diet_category = data.get('diet category', animal.diet_category)
        animal.animal_class = data.get('animal class', animal.animal_class)
        
        # # db.session.add(animal)
        # # db.session.commit()

        animal_service = Animal_service()

        animals = animal_service.update_animal(animal_id, animal)
        
        return api_response(
            status_code=200, 
            message='Updated' ,
            data=animals
        )
    except ValidationError as e:
        return api_response(
            status_code=400, 
            message=e.errors() ,
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500, 
            message=e.errors() ,
            data={}
        )
    
@animal_blueprint.route('/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    try:
        data = request.json
        print(data)

        animal = Animal.query.get(animal_id)

        animal.name = data.get('name', animal.name)
        animal.species = data.get('species', animal.species)
        # animal.binomial_name = data['binomial name']
        animal.age = data.get('age', animal.age)
        animal.gender = data.get('gender', animal.gender)
        animal.food = data.get('food', animal.food)
        animal.diet_category = data.get('diet category', animal.diet_category)
        animal.animal_class = data.get('animal class', animal.animal_class)



        # # animal.id = data['id']
        # animal.name = data['name']
        # animal.species = data['species']
        # # animal.binomial_name = data['binomial name']
        # animal.age = data['age']
        # animal.gender = data['gender']
        # animal.food = data['food']
        # animal.diet_category = data['diet category']
        # # animal.animal_class = data['animal class']
        
        db.session.delete(animal)
        db.session.commit()
        
        return 'success', 200
    except Exception as e:
        return str(e), 500
    
