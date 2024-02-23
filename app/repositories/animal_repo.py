from app.models.animal import Animal
from app.utils.database import db


class Animal_repo():
    def get_list_animal(self):
        animals = Animal.query.all()
        return animals
    
    def update_animal(self, id, animal):
        animal_obj = Animal.query.get(id)
        animal_obj.name = animal.name
        animal_obj.species = animal.species
        animal_obj.age = animal.age
        animal_obj.gender = animal.gender
        animal_obj.food = animal.food
        animal_obj.diet_category = animal.diet_category
        animal_obj.animal_class = animal.animal_class

        db.session.commit()
        # return animal_obj


    def search_animal(self, name):
        animals = Animal.query.filter(Animal.name.like(f'%{name}')).all()
        return animals
