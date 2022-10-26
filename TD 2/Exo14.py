heure = int(input("Veuillez saisir l'heure "))
minute = int(input("Veuillez saisir la minute "))
if(heure <= 23):
    if(minute ==59):
        heure += 1
        minute = 0
    else:
        minute +=1
print("Apres une minute il fait", heure, "H et", minute, "min")
