from flask import Blueprint, jsonify, request
# from app import app
from app.utils.database import db
from app.models.animal import Animal

animal_blueprint = Blueprint('animal_endpoint', __name__)



@animal_blueprint.route('/', methods=['GET'])
def get_list_animal():
    try:
        animals = Animal.query.all()

        return [animal.as_dict() for animal in animals], 200
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
        animal.id = data['id']
        animal.name = data['name']
        animal.species = data['name']
        animal.binomial_name = data['binomial name']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.food = data['diet']
        animal.diet_category = data['diet category']
        animal.animal_class = data['animal class']
        
        db.session.add(animal)
        db.session.commit()
        
        return 'success', 200
    except Exception as e:
        return e, 500
@animal_blueprint.route('/', methods=['PUT'])
def update_animal():
    try:
        data = request.json
        print(data)

        animal = Animal()
        animal.id = data['id']
        animal.name = data['name']
        animal.species = data['name']
        animal.binomial_name = data['binomial name']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.food = data['diet']
        animal.diet_category = data['diet category']
        animal.animal_class = data['animal class']
        
        db.session.add(animal)
        db.session.commit()
        
        return 'success', 200
    except Exception as e:
        return e, 500
    
@animal_blueprint.route('/', methods=['DELETE'])
def delete_animal():
    try:
        data = request.json
        print(data)

        animal = Animal()
        animal.id = data['id']
        animal.name = data['name']
        animal.species = data['name']
        animal.binomial_name = data['binomial name']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.food = data['diet']
        animal.diet_category = data['diet category']
        animal.animal_class = data['animal class']
        
        db.session.delete(animal)
        db.session.commit()
        
        return 'success', 200
    except Exception as e:
        return e, 500
    
