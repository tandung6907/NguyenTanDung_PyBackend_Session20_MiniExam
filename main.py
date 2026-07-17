from routers.students_router import students_router
from fastapi import FastAPI
from database.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind= engine)

app.include_router(students_router)

@app.get("/")
async def home():
    return {"message" : "Tạo API thành công"}