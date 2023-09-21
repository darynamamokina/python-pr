#task 1

print("Task 1")

integer_variable = 98
print("Integer variable:", integer_variable)
print("Type of integer variable:", type(integer_variable))

float_variable = 9.667808
print("Float variable:", float_variable)
print("Type of float variable:", type(float_variable))

boolean_variable = True
print("Boolean variable:", boolean_variable)
print("Type of boolean variable:", type(boolean_variable))

string_variable = "I want pizza"
print("String variable:", string_variable)
print("Type of string variable:", type(string_variable))


#task 2

print("Task 2")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

sum_result = number1 + number2
print("Sum:", sum_result)

difference = number1 - number2
print("Difference:", difference)

product = number1 * number2
print("Product:", product)

if number2 != 0:
    quotient = number1 / number2
    print("Quotient:", quotient)
else:
    print("Division by zero is not allowed.")


#task 3

print("Task 3")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

greater_than = num1 > num2
less_than = num1 < num2
equal_to = num1 == num2

print("Is the first number greater than the second number?", greater_than)
print("Is the first number less than the second number?", less_than)
print("Are the two numbers equal?", equal_to)

int_num1 = int(num1)
int_num2 = int(num2)

print("Integer value of the first number:", int_num1)
print("Integer value of the second number:", int_num2)
