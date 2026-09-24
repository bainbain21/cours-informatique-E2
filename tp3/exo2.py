# fonction reccursive de Sycarrus

def Syc(n):
    if n <= 1 : return [1]
    if n%2 == 0 : 
        res = [n] + Syc(n//2)
        return res
    elif n%2 != 0 : 
        res = [n] + Syc(n*3+1)
        return res

print(Syc(30))