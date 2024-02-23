from pydantic import BaseModel, Field
from typing import Optional

class Update_employee_request(BaseModel):
    # id = db.Column(db.Integer, primary_key=True)
    # id: int = Field(..., description='Animal Id')
    name: str = Field(..., description='Employee name', min_length=3, max_length=50)
    email: Optional [str] = Field(None, description='Employee email')
    phone: Optional[int] = Field(None, description='Employee phone')
    role : str= Field (..., description='Employee role ')
    schedule : str = Field(..., description='Employee schedule')

