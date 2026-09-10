# conversion d'un décimal (base 10) en binaire (base 2) 

while True :
    b10 = int(input("entrer une valeur à convertir : "))
    if b10 < 0:
        print("entrer une valeur positive")
    else :
        break

def base2(n) :
    b2 = []
    while n != 0 :
        r = n % 2
        if r == 1 :
            n-=1
        b2.append(str(r))
        n //= 2
    b2.reverse()
    base = "".join(b2)
    return base

    
print(f"{b10} en binaire est {base2(b10)}")
