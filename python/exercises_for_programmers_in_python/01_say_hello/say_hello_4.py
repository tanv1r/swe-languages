messages = [
    "nice to meet you!",
    "good to meet you!",
    "peace be upon you!"]

name = input("What is your name? ")

# ord returns integer representation of unicode character
print("Hello, " + name.title() + ", " + messages[ord(name[0])%3])