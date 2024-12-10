from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "Notification Service", "message": "Hello from Notification Service"}
