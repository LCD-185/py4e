largest = None
smallest = None

while True:
    number = input("Please enter a number ")
    if (number == "done"): break
    elif(True):
        try:
            number = int(number)
            if (largest is None or number > largest):  largest = number
            elif (smallest is None or number < smallest) : smallest = number
        except:
            print("Invalid input")



print("Maximum is", largest)
print("Minimum is", smallest)
