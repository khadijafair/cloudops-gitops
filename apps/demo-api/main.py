from fastapi import FastAPI

app = FastAPI(title="DevPlatform Demo API")

@app.get("/")
def home():
    return {
        "application": "demo-api",
        "version": "1.0.0",
        "message": "Deployed with DevPlatform"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
