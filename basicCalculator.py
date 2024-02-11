variable = True
while variable:

  #Take two numbers as input and add them together
  num1 = float(input("Enter a number to add: "))
  num2 = float(input("Enter another number to add: "))
  sum = num1 + num2
  print("The sum of the number is: ",sum)
  
  #Take two numbers ans subtract the second from the first
  num1 = float(input("Enter a number to subtract: "))
  num2 = float(input("Enter a number to subtract: "))
  sub = num2 - num1 
  print("The subtraction between the numbers is: ", sub)
  
  #Take two numbers and multiply them
  num1 = float(input("Enter a number to multiply: "))
  num2 = float(input("Enter a number to multiply: "))
  mul = num1 * num2 
  print("The multiplication is: ", mul)
  
  #Take two numbers and divide them
  num1 = float(input("Enter a number to divide: "))
  num2 = float(input("Enter another number to divide: "))
  div = num1 / num2
  print("The division between the first number and the second is: ", div)
  
  #Take two numbers and perform a modulus operation
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))
  mod = num1 % num2
  print("The result of the modulus operation is: ", mod)
  
  #Choose wich operation to perform on two numbers
  operation = input("Enter the operation you want to perform: (+, -, *, /, %) ")
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))
  if operation == "+": 
    print("The sum of the numbers is: ", num1 + num2)
  elif operation == "-":
    print("The subtraction between the numbers is: ", num2 - mun1)
  elif operation == "*":
    print("The multiplication is: ", num1 * num2)
  elif operation == "/":
    print("The division between the numbers is: ", num2 / num1)
  elif operation == "%":
    print("The result of the modulus operation is: ", num1 % num2)
  else:
    print("Invalid operation")
  
  #Take 3 numbers and add them together 
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))
  num3 = float(input("Enter another number: "))
  sum = num1 + num2 + num3
  print("The sum of the numbers is: ", sum)
  
  #mix op. with 3
  def multiply(): 
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a second number: "))
    num3 = float(input("Enter a third number: "))
    return num1 * num2 * num3
  print("The multiplication of the numbers is: ", multiply())
  
  #Mix op. with more than 3
  def add_numbers(num1, num2, num3):
    return num1 + num2 + num3
  print("We are going to make a mix operation")
  num1 = float(input("Enter a number: "))
  operation = input("Enter an operation: +, -, *, / ")
  num2 = float(input("Enter another number: "))
  operation2 = input("Enter another operation: +, -, *, / ")
  num3 = float(input("Enter another number: "))
  if operation in ("+", "-", "*", "/") and operation2 in ("+", "-", "*", "/"):
    result = eval(f"{num1} {operation} {num2} {operation2} {num3}")
    print("Result: ", result)
  else:
    print("It is not valid")
  
  continue_or_not = input("Do you want to make more operations? (y/n): ") 
  if continue_or_not == "n":
    print("Goodbye!")
    variable = False
