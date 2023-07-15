
def addition(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiplication(a, b):
  return a * b
def division(a, b):
  return a / b
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
operation = input("Enter the operation to be performed (+, -, *, /): ")
if operation == "+":
  result = addition(num1, num2)
elif operation == "-":
  result = subtract(num1, num2)
elif operation == "*":
  result = multiplication(num1, num2)
elif operation == "/":
  result = division(num1, num2)
print("The result is:", result)
