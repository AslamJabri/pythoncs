greeting = input("Greeting: ")


if greeting == "Hello" or greeting == "hello":
    print("$0")
elif greeting.startswith("h") or greeting.startswith("H"):
    print("$20")
else:
    print("$100")