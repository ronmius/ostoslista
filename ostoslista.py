
lista =[ {'nimi':'leipä', 'määrä':2 }, {'nimi':'maito', 'määrä':5},{'nimi':'kahvi','määrä':10}]
while True:
    
    print("1. näytä ostos lista")
    print("2. Lisää")#kaikki eri moodit jota voi tehdä
    print("3. lopeta")
    print("4. poista tuote")
    vaiht = input("")

    if vaiht =="1":
        for ostos in lista:#vaihtoetho 1 näytää listan
            print(ostos['nimi']+' '+ str(ostos['määrä'])) 
            

    elif vaiht =="2":
        tuot = input("mitä haluat lisätä ")
        määrä =int(input("kuinka monta "))#vaihtoehto 2 lisää listaan tavaraa
        tuote = {'nimi': tuot, 'määrä':määrä}#lisätään tuoteen nimi ja määrä muutujaan
        lista.append(tuote)
    elif vaiht=="3":
        break
    elif vaiht=="4":
        for tuote in enumerate(lista):#saadan listan numerot
            print(tuote)
        nimi =int(input("mikä poistetaan"))#poistettavan numero
        lista.pop(nimi)#poistetaan poistettava asia