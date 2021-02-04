people = input("How many people? ")
pizza = input("How many pizzas do you have? ")
slices = input("How many slices per pizza? ")
try:
    people_count = int(people)
    pizza_count = int(pizza)
    slice_per_pizza = int(slices)

    total_slices = slice_per_pizza * pizza_count

    if total_slices < people_count:
        print("Too few slices.")
    else:
        print(people + " people with " + pizza + " pizzas with " + slices + " pieces per pizza")
        slice_per_person = int( total_slices/people_count )
        left_over = total_slices - slice_per_person * people_count

        if slice_per_person > 1 :
            print("Each person gets " + str(slice_per_person) + " pieces of pizza.")
        else:
            print("Each person gets 1 piece of pizza.")
        
        if left_over == 1:
            print("There are 1 leftover piece.")
        else:
            print("There are " + str(left_over) + " leftover pieces.")
except ValueError:
    print("Invalid input.")