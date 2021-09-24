class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):

        return self.a+self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):

        if self.b == 0:
            raise ValueError("Division by zero not possible!!")
        return self.a/self.b

obj = Calculator(4,5)
print("Sum : ",obj.addition())
print("Differece : ",obj.subtraction())
print("Product : ",obj.multiplication())
print("Quotient : ",obj.division())