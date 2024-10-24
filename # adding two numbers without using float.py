# adding two numbers without using float
def add_numbers(a,b):
    return a+b

num1 = int(input("enter the first number:"))
num2 = int(input("Enter the second number"))

result = add_numbers(num1,num2)
print(f"the sum of {num1} and {num2} is {result}")
