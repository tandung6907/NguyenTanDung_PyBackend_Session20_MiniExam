from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__   = "students"

    student_id      = Column(Integer, primary_key= True, index= True)
    student_code    = Column(String(15), nullable= False, unique= True)
    full_name       = Column(String(255), nullable= False)
    email           = Column(String(50), nullable= False, unique= True)
    class_id        = Column(Integer, ForeignKey("classrooms.class_id"), unique= True)

    classroom       = relationship("ClassroomModel", back_populates= "students")
