from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from .classroom_schema import ClassResponse

class StudentCreate(BaseModel):
    full_name         : str = Field(..., min_length= 6)
    student_code      : str = Field(..., min_length= 6)
    email             : str = Field(...)
    class_id          : int

class StudentUpdate(BaseModel):
    full_name         : Optional[str] = Field(None, min_length= 6)
    student_code      : Optional[str] = Field(None, min_length= 6)
    email             : Optional[str] = None
    class_id          : Optional[int] = None

class StudentResponse(BaseModel):
    student_id        : int
    full_name         : str
    student_code      : str
    email             : str
    classroom         : ClassResponse

    model_config = ConfigDict(from_attributes= True)