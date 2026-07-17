from sqlalchemy.orm import Session
from exception.exception import AppException
from schemas.students_schema import StudentCreate, StudentUpdate
from models.students_model import StudentModel

async def get_all_student(db: Session):
    student = db.query(StudentModel).all()
    return student

async def get_student_by_id(db: Session, id: int) -> StudentModel:
    is_existing = db.query(StudentModel).filter(StudentModel.student_id == id).first()
    if not is_existing:
        raise AppException(404, f"Không tìm thấy sinh viên có id {id}", "STUDENT NOT FOUND")
    return is_existing

async def create_new_student(db: Session, student_data: StudentCreate) -> StudentModel:
    new_student = StudentModel(
        full_name= student_data.full_name,
        student_code= student_data.student_code,
        email= student_data.email,
        class_id= student_data.class_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

