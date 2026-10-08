from Product import *

p1 = Product("P01", "PC", 800.00)
p2 = Product("P02", "Tél", 400.00)
p3 = Product("P03", "Cuillère", 2.00)

produits = [p1,p2,p3]
taxe = 0.2

for p in produits :
    print(f"Produit : {p.code}, {p.name}, Prix : {p.get_price_it(taxe)}")