from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "Appointment Service", "message": "Hello from Appointment Service"}
