# Python Program

# Multiple Inheritance

class Add:

    # Method 
    def addition(self, num1, num2):
        return (num1 + num2)

class Mul:
    # Method
    def multiplication(self, num1, num2):
        return (num1 * num2)

# Multiple Inheritance
class Div(Add, Mul):

    # Method
    def divide(self, num1, num2):
        return (num1 / num2)

# Create object
obj = Div()

# Call Method

print("Addition is: ", obj.addition(10, 20))
print("Multiplication is: ", obj.multiplication(10, 20))
print("Division is: ", obj.divide(10, 20))

# Thanks for Watching