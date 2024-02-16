from app.utils.database import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    role = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)
    

    def as_dict(self):
        return {'id' : self.id, 
                'name': self.name, 
                'email': self.email,
                'phone': self.phone,
                'role': self.role,
                'schedule': self.schedule
                }
