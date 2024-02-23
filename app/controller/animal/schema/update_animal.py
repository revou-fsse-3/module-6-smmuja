from pydantic import BaseModel, Field
from typing import Optional

class Update_animal_request(BaseModel):
    # id = db.Column(db.Integer, primary_key=True)
    # id: int = Field(..., description='Animal Id')
    name: str = Field(..., description='Animal name', min_length=3, max_length=50)
    species: str = Field(..., description='Animal species')
    binomial_name: Optional[str] = Field(None, description='Binomial name')
    age : Optional[int]= Field (None, description='Animal Age')
    gender : str = Field(..., description='Animal gender')
    food : str = Field(..., description='Animal food')
    # diet_category : str = Field(..., description='diet category')
    animal_class : Optional[str] = Field(None, description='Animal class')

