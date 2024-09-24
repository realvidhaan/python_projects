import math


def entry():
    try:
        user = int(input(" 1. sum\n 2. difference\n 3. product\n 4. quotient\n 5. exponent\n 6. square root\n 7. cosine\n 8. sine\n 9. tangent\n 10. percent\n 11. division with a remainder\n 12. logarithm\n out of these choices what are you looking for? (answer in the corresponding numbers, e.g: 1, that means sum) "))
        
        match user:
            case 1:
                sum_operation()
            case 2:
                difference_operation()
            case 3:
                product_operation()
            case 4:
                quotient_operation()
            case 5:
                exponent_operation()
            case 6:
                square_root_operation()
            case 7:
                cos_operation()
            case 8:
                sin_operation()
            case 9:
                tan_operation()
            case 10:
                percent_operation()
            case 11:
                modulo_operator()
            case 12:
                logarithm_operation()
            case _:
                print("Invalid choice")
                
    except ValueError:
        print("Invalid operation choice.")
        
def sum_operation():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        c = a + b
        print(f"{a} plus {b} is equal to {round(c, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def difference_operation():
    try:
        d = float(input("First number: "))
        n = float(input("Second number: "))
        if d > n:
            r = d - n
            print(f"{d} minus {n} is equal to {round(r, 4)}")
        elif n > d:
            r = n - d
            print(f"{n} minus {d} is equal to {round(r, 4)}")
        else:
            r = 0
            print(f"{n} minus {d} is equal to {round(r, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def product_operation():
    try:
        g = float(input("First number: "))
        h = float(input("Second number: "))
        q = g * h
        print(f"{g} times {h} is equal to {round(q, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def quotient_operation():
    try:
        erw = float(input("First number: "))
        qew = float(input("Second number: "))
        if qew > erw:
            qws = qew / erw 
            print(f"{qew} divided by {erw} is equal to {round(qws, 4)}")
        elif erw > qew:
            qws = erw / qew
            print(f"{erw} divided by {qew} is equal to {round(qws, 4)}")
        else:
            qws = 0
            print(f"{erw} divided by {qew} is equal to {round(qws, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")
    
def exponent_operation():
    try:
        s = float(input("Base number: "))
        e = float(input("Exponent number: "))
        f = s ** e
        print(f"{s} to the power of {e} is equal to {round(f, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def square_root_operation():
    try:
        o = float(input("Number for square root: "))
        v = math.sqrt(o)
        print(f"The square root of {o} is {round(v, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def cos_operation():
    try:
        q = float(input("Angle in degrees: "))
        cos_value = math.cos(math.radians(q))
        print(f"The cosine of {q} degrees is {round(cos_value, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def sin_operation():
    try:
        ad = float(input("Angle in degrees: "))
        sin_value = math.sin(math.radians(ad))
        print(f"The sine of {ad} degrees is {round(sin_value, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def tan_operation():
    try:
        ax = float(input("Angle in degrees: "))
        tan_value = math.tan(math.radians(ax))
        print(f"The tangent of {ax} degrees is {round(tan_value, 4)}")
    except ValueError:
        print("you can only use positive integers, not strings.")

def percent_operation():
    try:
        df = float(input("Number for percent (part): "))
        sd = float(input("Number for percent (whole): "))
        qfk = (df / sd) * 100
        print(f"{df} percent out of {sd} percent is equal to {round(qfk, 4)} percent")
    except ValueError:
        print("you can only use positive integers, not strings.")

def modulo_operator():
    try:
        er = float(input("Number for division w/ remainder: "))
        e = float(input("Number for division w/ remainder: "))
        if er > e:
            ds = er % e
            print(f"The remainder of {er} divided by {e} is {ds} ")

        elif e > er:
            ds = e % er
            print(f"The remainder of {e} divided by {er} is {ds} ")

        else:
            ds = 0
            print(f"The remainder of {er} divided by {e} is {ds} ")
        
    except ValueError:
        print("you can only use positive integers, not strings.")

def logarithm_operation():
    try:
        sf = float(input("Number for logarithm (base): "))
        s = float(input("Number for logarithm (argument): "))
        efc = math.log(s, sf)
        print(f"log {sf} to {s} is equal to {round(efc, 4)}")
    except ValueError:
         print("you can only use positive integers, not strings.")


if __name__ == "__main__":
    entry()