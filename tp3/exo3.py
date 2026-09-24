import sys

print ('argument list', sys.argv)
ht = sys.argv[1]
if ht.lower() != 'head' and ht.lower() != 'tail' : print("ValueError, entrer head ou tail")
lignes = int(sys.argv[2])
if lignes < 0 : print("ValueError, entrer une valuer positive")
loc = sys.argv[3]

try :
    with open(loc, 'r', encoding='utf-8') as f :
        for i in range(lignes):
            l = f.readline()
            if l == None:
                break 
            print(l)
except :
    print('fichier introuvable')