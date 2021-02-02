conversion_factor = 0.09290304

try:
    length_feet = float(input('What is the length of the room in feet? '))
    if length_feet <= 0:
        print('Length must be positive.')
        raise ValueError()
    else:
        width_feet = float(input('What is the width of the room in feet? '))
        if width_feet <= 0:
            print('Width must be positive.')
            raise ValueError()
except ValueError:
    print('Invalid input.')
else:
    print('You entered dimensions of ' + str(length_feet) + " feet by " + str(width_feet) + " feet.")
    area_sq_feet = length_feet * width_feet
    area_sq_meter = area_sq_feet * conversion_factor
    print('The area is\n' + str(round(area_sq_feet, 3)) + " square feet.\n" + str(round(area_sq_meter, 3)) + " square meters.")