from fastapi import FastAPI
import uvicorn
from src.dataloader import load_data

app = FastAPI()

testdaten = load_data()

@app.get("/")
def read_root():
    return testdaten.to_dict()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

