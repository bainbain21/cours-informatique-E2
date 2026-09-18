import collections

def ajout_coef(poly,coef):
    p = collections.deque(poly)
    p.insert(0,coef)
    return p

print(ajout_coef('3X+5',2))

def polynome():
    poly=collections.deque()
    deg=int(input('entrer le degrée du polynome : '))
    val1 = int(input('entrer le premier coef : '))
    poly.append(val1)
    for i in range(1,deg+1) :
        val=int(input('entrer le coef suivant : '))
        poly.appendleft('+')
        poly.appendleft(i)
        poly.appendleft('x')
        poly.appendleft(val)
    return poly

def imp(deque):
    x=''
    for el in deque:
        x+=str(el)
    return x

# print(imp(polynome()))

def destruction(poly):
    return 0

# print(destruction(imp(polynome())))

# def addition(p1,p2):