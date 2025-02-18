
from fastapi import FastAPI
from equation import Equation
from algebra import Algebra
import uvicorn

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/calc/{val1}/{val2}/{operation}")
async def calculate(val1: int, val2: int, operation: str):
    equation = Equation(val1, val2, operation)
    return {"result": equation.calculate()}
@app.get("/algebra/{val1}/{val2}/{operation}/{result}")
async def algebra(val1: str, val2: str, operation: str, result: int):
    varible = val1[1]
    val1 = int(val1[0])
    val2 = int(val2[0])
    algebra = Algebra(val1, val2, operation, result)
    return {f'result: {varible} = ': algebra.algebra()}
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)