print("Type 'q' to quit.")
while True:
    first_number_str = input("What is the first integer? ")
    if first_number_str == 'q':
        break
    
    try:
        x = int(first_number_str)
    except ValueError:
        print("Please enter a valid integer for the first number.")
        continue
    else:
        second_number_str = input("What is the second integer? ")
        if second_number_str == 'q':
            break

        try:
            y = int(second_number_str)
            if y == 0:
                print("Cannot divide by zero.")
                continue
        except ValueError:
            print("Please enter a valid integer for the second number.")
            continue
        else:
            sum = x+y
            diff = x-y
            prod = x*y
            div = int(x/y)
            print(first_number_str + ' + ' + second_number_str + ' = ' + str(sum))
            print(first_number_str + ' - ' + second_number_str + ' = ' + str(diff))
            print(first_number_str + ' * ' + second_number_str + ' = ' + str(prod))
            print(first_number_str + ' / ' + second_number_str + ' = ' + str(div))