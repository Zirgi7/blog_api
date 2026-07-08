from fastapi import FastAPI
from routers import blogs
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="Управление блогами - создание, публикация, обновление и удаление",
    version="1.0.0"
)

app.include_router(blogs.router)


@app.get("/")
def root():
    return {"message": "Blog API is running. Visit /docs for Swagger documentation."}
