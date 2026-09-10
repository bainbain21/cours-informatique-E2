# approximation de pi

n = int(input("entrer le nombre d'approximation de pi souhaitées : "))

def npi(a) :
    pi = 3
    j = 3
    for i in range(1,a,2):
        pi += 4/((j-1)*j*(j+1))
        j+=2
        pi -= 4/((j-1)*j*(j+1))
        j+=2
    return pi

print(f"la valeur pi souhaitée est {round(npi(n),n-1)}")