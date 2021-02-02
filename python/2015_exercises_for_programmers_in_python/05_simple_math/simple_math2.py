def read_number(prompt):
    x_str = input(prompt)
    return int(x_str)

def compute(x, y):
    result = []
    result.append(x+y)
    result.append(x-y)
    result.append(x*y)
    result.append(int(x/y))

    return result

def get_output(result):
    output = ""
    for i in range(4):
        if i == 0:
            output += (str(x) + ' + ' + str(y) + ' = ' + str(result[i]) + "\n")
        elif i == 1:
            output += (str(x) + ' - ' + str(y) + ' = ' + str(result[i]) + "\n")
        elif i == 2:
            output += (str(x) + ' * ' + str(y) + ' = ' + str(result[i]) + "\n")
        else:
            output += (str(x) + ' / ' + str(y) + ' = ' + str(result[i]))
    
    return output

try:
    x = read_number('What is the first number? ')
except ValueError:
    print('Invalid first number.')
else:
    try:
        y = read_number('What is the second number? ')
    except ValueError:
        print('Invalid second number.')
    else:
        try:
            result = compute(x, y)
        except ZeroDivisionError:
            print('Cannot divide by zero.')
        else:
            print(get_output(result))
