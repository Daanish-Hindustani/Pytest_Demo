class Equation:
    def __init__(self, val1, val2, operation):
        self.val1 = val1
        self.val2 = val2
        self.operation = operation

    def calculate(self):
        if self.operation == 'add':
            return self.val1 + self.val2
        elif self.operation == 'subtract':
            return self.val1 - self.val2
        elif self.operation == 'multiply':
            return self.val1 * self.val2
        elif self.operation == 'divide':
            if self.val2 != 0:
                return self.val1 / self.val2
            else:
                raise ValueError("Cannot divide by zero")
        else:
            raise ValueError("Invalid operation")