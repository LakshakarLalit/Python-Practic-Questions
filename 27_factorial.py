number = int(input("Enter a number to find factorial:"))
num = number
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1
print(f'Factorial of {num} is: {factorial}')