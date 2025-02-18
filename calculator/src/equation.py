class Equation:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return a**b

    def square_root(self, a):
        return a**0.5

    def choose_operation(self, operation, a, b=None):
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)
        elif operation == "power":
            return self.power(a, b)
        elif operation == "square_root":
            return self.square_root(a)
