from calculate_tip import calculate_bill_and_tip

print("Enter 'q' to quit.")
while True:
    bill_string = input("What is the bill (in $)? ")
    if bill_string == 'q':
        break
    try:
        bill = float(bill_string)
        if bill <= 0:
            print("Please enter a positive value for the bill.")
            continue
    except ValueError:
        print("Please enter only the dollar amount of the bill.")
    else:
        percentage_string = input("What is the tip percentage? ")
        if percentage_string == 'q':
            break

        try:
            percentage = float(percentage_string)
            if percentage < 0:
                print("Please enter a non-negative value for the tip percentage")
                continue
        except ValueError:
            print("Please enter the percentage amount as a number.")
        else:
            info = calculate_bill_and_tip(bill, percentage)
            print("The tip is $" + str(info[1]) + ".")
            print("The total is $" + str(info[0]) + ".")