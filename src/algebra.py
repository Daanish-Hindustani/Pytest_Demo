from equation import Equation

class Algebra(Equation):
    def __init__(self, val1: int, val2: int, operation: str, result: int):
        super().__init__(val1, val2, operation)
        self.result = result

    def algebra(self):
        val = self.calculate()  
        if val == 0:
            raise ValueError("Division by zero error in algebra calculation.")
        return self.result / val  