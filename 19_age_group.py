age = int(input("Enter your age: "))

if (age<13):
    print("Child")
elif(age<20 and age>=13 ):
    print("Teenager")
elif(age<60 and age>=20):
    print("Adult")
else:
    print("Senior")