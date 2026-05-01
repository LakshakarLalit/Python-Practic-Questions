number = int(input("Enter a number to check prime or not: "))

if number <= 1:
    print("Number is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Number is not prime")
            break

    else:
        print("Number is prime")  