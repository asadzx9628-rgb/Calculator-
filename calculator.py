
print("================================")
print("       ASAD CALCULATOR")
print("================================")

num1 = float(input("Enter first number: "))
operator = input("Enter (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operator!"

print("Result:", result)
print("Thank you for using Asad Calculator!")
