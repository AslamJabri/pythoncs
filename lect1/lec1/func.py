
def main():    
    hello() 
    name = input("Whats your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)
    
    
#main()


def calc():
    x = int(input("What's x ? "))
    print(f"x squared is {square(x)}")
    
def square(n):
    return pow(n,3) 

calc()