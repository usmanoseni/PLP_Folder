# code that accept two value of the users and help to find the mathematical operation (addition, subtraction, multiplication, or division).
print("Welcome to the Calculator Program, dear user!")

# code to accept two numbers from the user and the operation to be performed
num1 = int(input("Enter Your first number:"))
num2 = int(input("Enter Your second number:"))
sign = str(input("Enter the operation you want to perform (+, -, *, /):"))
result = 0
# control flow code that determine how the output should look like
if sign == "+":
    result = num1 + num2
    print(f" The result of {num1}  {sign} {num2} = {result} ")
elif sign == "-":
    result = num1 - num2
    print(f" The result of {num1}  {sign} {num2} = {result} ")
elif sign == '*':
    result = num1 * num2
    print(f"The result of {num1}  {sign} {num2} = {result} ")
elif sign == '/':
    if num2 != 0:
        result = num1 * num2
        print(f"The result of {num1}  {sign} {num2} = {result} ")
    else:
        print("There is an error due to the zero input")
