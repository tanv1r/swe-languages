from math import ceil

conversion_factor = 1/350

try:
    width = float(input("Please enter the room's width in feet: "))
    length = float(input("Please enter the room's length in feet: "))
    area = round(width * length, 2)
    gallons_needed = ceil( area * conversion_factor )

    print(f"You will need to purchase {gallons_needed} gallons of paint to cover {area} square feet.")
except ValueError:
    print("Invalid input.")