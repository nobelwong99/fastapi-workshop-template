from fastapi import FastAPI

app = FastAPI(title="Task Manager API", description="102 Workshop - Web API Development using Python")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}


# Add your endpoints below as you progress through the workshop tasks.
