from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "Patient Service", "message": "Hello from Patient Service"}
