print("Type 'q' to quit.")
while True:
    sentence = input("What is the input string? ")
    if sentence == 'q':
        break
    
    if sentence:
        print(sentence + " has " + str(len(sentence)) + " characters.")
    else:
        print("Please enter a non-empty sentence.")