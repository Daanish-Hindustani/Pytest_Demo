
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from equation import Equation
from algebra import Algebra
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/calc/{val1}/{val2}/{operation}")
async def calculate(val1: int, val2: int, operation: str):
    equation = Equation(val1, val2, operation)
    return {"result": equation.calculate()}
@app.get("/algebra/{val1}/{var1}/{val2}/{var2}/{operation}/{result}")
async def algebra(val1: int, var1: str, val2: int, var2: str, operation: str, result: int):
    algebra = Algebra(val1, var1, val2, var2, operation, result)
    obj = {"result": algebra.calculate()}
    return obj
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)