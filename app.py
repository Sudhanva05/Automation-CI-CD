import fastapi as Fastapi 

app = Fastapi.FastAPI()

@app.get("/")
def home():
    return{"message" : "Hello All CI/CD is working "}

@app.get("/health")
def health():
    return{"status": "server is running biath"}