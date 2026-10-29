x = 5  # Example starting value for x
y = 4  # Example starting value for y

# TODO: Add 3 to x using the += operator
x += 3 

# TODO: Multiply y by 2 using the *= operator
y *= 2 

# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y 

# TODO: Print the value of 'result'
print(result)


#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# Define sample values for the variables so the code can run
a = 10
b = 4
c = 5

# Create a condition that checks if a is greater than b
condition1 = a > b 

# Create a condition that checks if b is even (hint: use the modulus operator)
condition2 = b % 2 == 0

# Create a condition that checks if c is less than or equal to a
condition3 = c <= a

# Combine the above conditions using logical operators to create a 'final_condition'
# The 'final_condition' should be True if either:
# - a is greater than b, or
# - b is even and c is less than or equal to a
final_condition = condition1 or (condition2 and condition3)

# Print the value of 'final_condition'
print(final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("Enter your test score (0-100): "))

# Implement a grading system using if-elif-else statements
if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the grade for the given score
print(f"Your grade is: {grade}")

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")

# Use conditional statements to perform the chosen operation on num1 and num2
# Handle the case of division by zero
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation selected."

# Print the result of the operation
print(f"Result: {result}")
