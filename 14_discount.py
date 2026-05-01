purchase = float(input("Enter your purchase amount:"))
discount = 0

if purchase>=5000:
    discount = (purchase*10)/100

total = purchase - discount

print("Your discount is:",discount)
print("Total amount after discount: ",total)