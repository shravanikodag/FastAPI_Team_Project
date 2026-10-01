from fastapi import FastAPI
from app.api import users

app = FastAPI(
    title="Team Task Management API",
    version="1.0.0"
)



# Connect users.py router to the FastAPI application
app.include_router(users.router)


@app.get("/")
def root():
    return {
        "message": "Team Task Management API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
