def main():
    exp = input("Expression: ")
    x,y,z = exp.split(" ")
    x = int(x)
    z = int(z)
    r = logic(x,y,z)
    print(float(r))

def logic(x,n,z):
     match n:
         case "+":
             return (x)+(z)
         case "-":
             return x-z
         case "/":
             return x/z
         case "*":
             return x*z

main()
