from database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ClassroomModel(Base):
    __tablename__   = "classrooms"

    class_id        = Column(Integer, primary_key= True, index= True)
    class_code      = Column(String(15), nullable= False, unique= True)
    class_name      = Column(String(255), nullable= False)

    students        = relationship("StudentModel", back_populates= "classroom")