def get_name():
    return input("What is your name? ")

def build_message(name):
    return "Hello, " + name.title() + ", nice to meet you!"

name = get_name()
message = build_message(name)
print(message)