class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == '__main__':
    # Example usage
    calc = Calculator()
    num1 = 5
    num2 = 7
    print("The sum is:", calc.add(num1, num2))
    print("The product is:", calc.multiply(num1, num2))
    print("The difference is:", calc.subtract(num1, num2))
    print("The quotient is:", calc.divide(num1, num2))
