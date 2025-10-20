class Calculator:
    def add(self, a, b):
        return a + b

    # add subtract method
    def subtract(self, a, b):
        return a - b

    # add multiply method
    def multiply(self, a, b):
        return a * b
    
    # add divide method
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b