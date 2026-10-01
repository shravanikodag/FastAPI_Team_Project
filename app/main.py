from fastapi import FastAPI

app = FastAPI(
    title="Team Task Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Team Task Management API is running!!"
    }