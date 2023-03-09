#x = int(input("What's x ? "))
#y = int(input("What's y ? "))

x = float(input("What's x ? "))
y = float(input("What's y ? "))

#z = round(x+y)

z = round(x / y ,2 )

print("The addition of x and y is ", end="")
#print(f"{z:,}")
#print(f"{z:.2f}")
print(z)