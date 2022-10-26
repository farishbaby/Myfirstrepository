print("Veuillez saisir le nom du produit")
n = input()
print("Veuillez saisir le prix du produit")
pht = int(input())
tva = 0.18
print("Le prix hors taxe du produit est:", pht)
print("Le prix hors tout taxe comprise  du produit est:", pht +(pht +tva))
