from app.utils.database import db


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    species = db.Column(db.String(100), nullable=False)
    binomial_name = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    food = db.Column(db.String(100), nullable=False)
    diet_category = db.Column(db.String(100), nullable=False)
    animal_class = db.Column(db.String(100), nullable=True)
    

    def as_dict(self):
        return {'id' : self.id, 
                'name': self.name, 
                'species': self.species,
                'binomial name' : self.binomial_name,
                'age' : self.age,
                'gender': self.gender,
                'food': self.food,
                'diet category': self.diet_category,
                'animal class' : self.animal_class
                }
