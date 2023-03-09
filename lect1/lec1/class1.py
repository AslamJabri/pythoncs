name = input("What is your name? ").strip().title()

#can create the chain of builtin methods
#name = name.strip().title()

first,last = name.split(" ")

#name = name.title()

print(f"Hello, {first}")