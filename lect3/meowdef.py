def main():
    num = get_number()
    (meow(num))

def get_number():
    number = int(input("Whats n ? "))
    while True:
        if number > 0:
            break
    return number
def meow(x):
    for _ in range(x):
        print("meow")
    
main()


students = ["harry","hermoine","Ron"]

while True:
    for i in range(len(students)):
        print(i +1,students[i]) 
    break