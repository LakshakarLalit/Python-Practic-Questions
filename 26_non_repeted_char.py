string = "teeter"

for char in string:
    print(char)
    if string.count(char) == 1:
        print("Charactor is:",char)
        break