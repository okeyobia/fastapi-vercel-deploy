from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Live from FastAPI! in Production"}
