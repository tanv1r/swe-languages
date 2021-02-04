tax_rate = 5.5/100

total = 0
count = 1
print("Enter 'done' when finished.")
while True:
    try:
        price_str = input("Enter the price of item " + str(count) + ": ")
        if price_str == 'done':
            break
        price = float(price_str)

        quantity_str = input("Enter the quantity of item " + str(count) + ": ")
        if quantity_str == 'done':
            break
        quantity = float(quantity_str)

        total += (price * quantity)
        count += 1
    except ValueError:
        print("Invalid input")

tax = total * tax_rate
print("Subtotal: $" + str(round(total, 2)))
print("Tax: $" + str(round(tax, 2)))
print("Total: $" + str( round( total + tax, 2 ) ))
