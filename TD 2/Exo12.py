print("Veuillez saisir votre age")
a = int(input())
if(a >= 0) and (a <= 14):
    print("Enfants")
elif(a >= 15) and (a <= 24):
    print("Adolescent")
elif(a >= 25) and (a <= 64):
    print("Adulte")
else:
    print("Vieux")
