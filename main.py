"""

How to run fastapi application?


uvicorn main:app --reload



#### Steps to open swagger UI

- http://127.0.0.1:8000/openapi.json
- copy & paste into https://editor.swagger.io/


#### another option

- http://127.0.0.1:8000/docs



"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}