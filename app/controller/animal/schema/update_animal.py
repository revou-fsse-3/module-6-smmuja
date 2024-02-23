from pydantic import BaseModel, Field
from typing import Optional

class Update_animal_request(BaseModel):
    # id = db.Column(db.Integer, primary_key=True)
    id: int = Field(..., description='Animal Id')
    # name = db.Column(db.String(100), nullable=True)
    name: str = Field(..., description='Animal name', min_length=3, max_length=50)
    # species = db.Column(db.String(100), nullable=False)
    species: str = Field(..., description='Animal species')
    # binomial_name = db.Column(db.String(100), nullable=True)
    binomial_name: Optional[str] = Field(None, description='Binomial name')
    # age = db.Column(db.Integer, nullable=True)
    age : Optional[int]= Field (None, description='Animal Age')
    # gender = db.Column(db.String(100), nullable=False)
    gender : str = Field(..., description='Animal gender')
    # food = db.Column(db.String(100), nullable=False)
    food : str = Field(..., description='Animal food')
    # diet_category = db.Column(db.String(100), nullable=False)
    # diet_category : str = Field(..., description='diet category')
    # animal_class = db.Column(db.String(100), nullable=True)
    animal_class : Optional[str] = Field(None, description='Animal class')

