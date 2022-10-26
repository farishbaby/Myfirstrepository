heure = int(input("Veuillez saisir l'heure "))
minute = int(input("Veuillez saisir la minute "))
seconde = int(input("Veuillez saisir la seconde "))

if(heure <= 23):
    if(minute ==59):
        if(seconde ==  59):
            heure += 1
            minute = 0
            seconde = 0
    
    else:
        minute +=1
        seconde += 1
else:
    if(minute ==59):
        heure = 0
        minute = 0
        seconde =0
    else:
        minute += 1
        seconde += 1
print("Apres une minute il fait", heure, "H", minute, "min et", seconde, "s")
