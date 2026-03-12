import fastapi as Fastapi 

app = Fastapi.FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD pipeline updated successfully!"}

@app.get("/health")
def health():
    return {"status": "server is running normally"}