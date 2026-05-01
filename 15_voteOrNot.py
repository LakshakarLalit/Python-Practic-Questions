age = int(input("Enter your age: "))

if age>0 and age<18:
    print("You cannot vote")
elif age>18:
    print("You can vote")
else:
    print("Not valid")