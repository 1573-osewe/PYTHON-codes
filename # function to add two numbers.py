# function to add two numbers
def add_numbers(a,b):
    return a+b

# input from the user

num1 = float(input("Enter the fisrt number:"))
num2 = float(input("Enter the second number:"))
 
 # call the defined function and display the result

result = add_numbers(num1, num2)
print(f"the sum of {num1} and {num2} is {result}")
