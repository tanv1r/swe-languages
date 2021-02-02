print("Enter 'q' to quit.")
while True:
    bill_string = input("What is the bill (in $)? ")
    if bill_string == 'q':
        break
    try:
        bill = float(bill_string)
    except ValueError:
        print("Please enter only the dollar amount of the bill.")
    else:
        percentage_string = input("What is the tip percentage? ")
        if percentage_string == 'q':
            break
        try:
            percentage = float(percentage_string)
        except ValueError:
            print("Please enter the percentage amount as a number.")
        else:
            tip = bill*percentage/100.0
            total = bill + tip
            print("The tip is $" + str(tip) + ".")
            print("The total is $" + str(total) + ".")