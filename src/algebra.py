from equation import Equation
import sympy

class Algebra(Equation):
    def __init__(self, val1: int, var1: str, val2: int, var2: str, operation: str, result: int):
        super().__init__(val1=val1, val2=val2, operation=operation)
        self.result = result
        self.var1 = var1
        self.var2 = var2

    def calculate(self):
        if self.operation == "add":
            self.operation = "+"
        elif self.operation == "subtract":
            self.operation = "-"
        elif self.operation == "multiply":
            self.operation = "*"
        elif self.operation == "divide":
            self.operation = "/"
        if self.var1 == self.var2:
            var1_sym = sympy.symbols(f'{self.var1}')
            solution = sympy.solve(f'{self.val1}*{self.var1} {self.operation} {self.val2}*{self.var2} - {self.result}', var1_sym)
            return str(solution[0])
        else:
            var1_sym, var2_sym = sympy.symbols(f'{self.var1} {self.var2}')
            solution = sympy.solve(f'{self.val1}*{self.var1} {self.operation} {self.val2}*{self.var2} - {self.result}', (var1_sym, var2_sym))
            return str(solution[0][0])
        
            
                