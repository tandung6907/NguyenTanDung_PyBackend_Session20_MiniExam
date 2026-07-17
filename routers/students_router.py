from fastapi import APIRouter
from services.student_service import get_all_student, get_student_by_id, create_new_student

router = APIRouter()

@router.get("/students")
def display_student():
    students = get_all_student()
    return students

@router.post("/student/update")
def add_student():
    find_student = get_student_by_id()
    if find_student:
        create_new_student()
    return find_student