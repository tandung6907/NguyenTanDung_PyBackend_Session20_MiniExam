from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class ClassCreate(BaseModel):
    class_name      : str = Field(..., min_length= 6)
    class_code      : str = Field(..., min_length= 6)

class ClassUpdate(BaseModel):
    class_name      : Optional[str] = Field(None, min_length= 6)
    class_code      : Optional[str] = Field(None, min_length= 6)

class ClassResponse(BaseModel):
    class_id        : int
    class_name      : str
    class_code      : str

    model_config = ConfigDict(from_attributes= True)