def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    str = (d.replace("$",""))
    #print(type(str))
    d = float(str)
   # print(type(d))
    return d


def percent_to_float(p):
    # TODO
    percent = int(p.replace("%",""))
    #p = int(p)
    p = float(percent)/100
    #print(p)
    return p

main()
