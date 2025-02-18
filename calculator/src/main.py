from fastapi import FastAPI, HTTPException
from src.equation import Equation

app = FastAPI()
equation = Equation()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Equation API!"}


@app.get("/equation/{operation}/{val1}/{val2}")
def equation_two_values(operation: str, val1: float, val2: float):
    try:
        return {"result": equation.choose_operation(operation, val1, val2)}
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400, detail="Division by zero is not allowed."
        )  # noqa: E501
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
