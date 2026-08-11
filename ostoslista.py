
lista =[ {'nimi':'leipä', 'määrä':2 }, {'nimi':'maito', 'määrä':5},{'nimi':'kahvi','määrä':10}]
while True:
    
    print("1. näytä ostos lista")
    print("2. Lisää")
    print("3. lopeta")
    print("4. poista tuote")
    vaiht = input("")

    if vaiht =="1":
        for ostos in lista:
            print(ostos['nimi']+' '+ str(ostos['määrä'])) 
            

    elif vaiht =="2":
        tuot = input("mitä haluat lisätä ")
        määrä =input("kuinka monta ")
        tuote = {'nimi': tuot, 'määrä':määrä}
        lista.append(tuote)
    elif vaiht=="3":
        break
    elif vaiht=="4":
        for tuote in enumerate(lista):
            print(tuote)
        nimi =int(input("mikä poistetaan"))
        lista.pop(nimi)