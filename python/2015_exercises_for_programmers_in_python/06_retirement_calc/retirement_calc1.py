from datetime import datetime as dt

try:
    age = int(input( 'What is your age? ' ))
    retirement_age = int(input('At what age would you like to retire? '))
except ValueError:
    print('Invalid input.')
else:
    year_till_retirement = retirement_age-age
    if year_till_retirement < 0:
        print('You can retire right away!')
    else:
        retirement_year = dt.now().year + year_till_retirement
        print('You have ' + str(year_till_retirement) + ' years left until you can retire.')
        print("It's " + str(dt.now().year) + ", so you can retire in " + str(retirement_year) + ".")