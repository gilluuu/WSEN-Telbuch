# import
import sys
import csv

# Funktionen

# Suchfunktion
def search(telbuch):
    #Hauptschleife Suche
    m = 0
    while m == 0:
        print("Sie können nach folgenden Datensätzen suchen:")
        print("1 = Vorname")
        print("2 = Nachname")
        print("3 = Telefonnummer")
        print("9 = Suche Beenden")

    #Testen ob int
        a = input("Ihre Auswahl: ")
        try:
            a = int(a)
        except:
            print("Eingabe war keine Zahl")

        # Vorname
        if a == 1:
            z = 0
            vorname = str(input("Geben Sie den Vornamen an: "))
            temp = []
            if vorname == str(9):
                m = 1
                break

            # Falls Such-Vorname == Telbuch-Vorname; in neuer Liste eintragen
            for i in range(0, len(telbuch)):
                if telbuch[i][0].lower() == vorname.lower():
                    temp.append(i)

            # Anzahl gefundener Einträge mit Suchparameter
            for x in temp:
                z = z + 1
                print()
                print(str(z) + "." + " Gefundener Eintrag")
                print(telbuch[x])
                print()

            if temp == []:
                print("Keine Person in der Datenbank mit dem Vornamen", vorname)
                del a

        # Nachname
        elif a == 2:
            z = 0
            name = str(input("Geben Sie den Nachnamen an: "))
            temp = []
            if name == str(9):
                m = 1
                break

            # Falls Such-Name == Telbuch-Name; in neuer Liste eintragen
            for i in range(0, len(telbuch)):
                if telbuch[i][1].lower() == name.lower():
                    temp.append(i)

            # Anzahl gefundener Einträge auflisten
            for x in temp:
                z = z + 1
                print()
                print(str(z) + "." + " Gefundener Eintrag")
                print(telbuch[x])
                print()

            if temp == []:
                print("Keine Person in der Datenbank mit dem Nachnamen", name)
                del a

        # Telefonnummer
        elif a == 3:
            z = 0
            try:
                tel = int(input("Geben Sie die Telefonnummer an: "))
                temp = []
                if tel == int(9):
                    m = 1
                    break

            except:
                print("Ungültige Eingabe")

                # Falls Such-Tel == Telbuch-Tel; in neuer Liste eintragen
                for i in range(0, len(telbuch)):
                    if telbuch[i][2] == tel:
                        temp.append(i)

                # Anzahl gefundener Einträge auflisten
                for x in temp:
                    z = z + 1
                    print()
                    print(str(z) + "." + " Gefundener Eintrag")
                    print(telbuch[x])
                    print()


                if temp == []:
                    print("Keine Person in der Datenbank mit der Telefonnummer", tel)

        elif a == 9:
            m = 1

        else:
            print("Eingabe wurde nicht erkannt")
            continue

    print()
    print("Zurück zum Hauptmenü...")
    print()

# Anlegefunktion
def new(telbuch):
    m = True
    while m == True:
        vorname = str(input("Geben Sie den Vornamen an: "))
        name = str(input("Geben Sie den Nachnamen an: "))
        try:
            tel = int(input("Geben Sie die Telefonnummer an: "))
        except:
            print("Ungültige Eingabe")
            print()
            continue

        telbuch.append([vorname, name, tel])

        print()
        print("Weiterer Eintrag anlegen?")
        print("1 = Ja")
        print("2 = Nein")

        try:
            auswahl = int(input("Ihre Auswahl: "))

        except:
            continue

        # Suche Wiederholen
        if auswahl == 1:
            m = True
            print()
            continue

        elif auswahl == 2:
            print()
            print("Zurück zum Hauptmenü...")
            print()
            m = False
            return telbuch
            break

        else:
            print("Ungültige Eingabe")
            print()

# Ausgabefunktion
def view(telbuch):
    print()
    print("Alle Einträge im Telefonbuch:")
    print(telbuch)

# Mutationsfunktion
def change(telbuch):
    # Hauptschleife change
    m = 0
    while m == 0:
        print()
        print("Um einen Eintrag zu Mutieren, führen Sie die untenstehende Suche aus.")
        print("Sie können jederzeit Abbrechen, wenn Sie die Zahl 9 eingeben")
        print()
        temp = []
        temp2 = []
        temp3 = []

        # Vorname
        vorname = str(input("Geben Sie den Vornamen an: "))
        if vorname == str(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            return telbuch
            m = 1
            break

        for i in range(0, len(telbuch)):
            if telbuch[i][0].lower() == vorname.lower():
                temp.append(telbuch[i])
        print()
        print("Gefundene Einträge:")
        print(temp)
        print()

        if temp == []:
            print("Keine Person in der Datenbank mit dem Vornamen", vorname)
            break

        # Nachname
        name = str(input("Geben Sie den Nachnamen an: "))
        if name == str(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            del temp
            return telbuch
            m = 1
            break

        for i in range(0, len(temp)):
            if temp[i][1].lower() == name.lower():
                temp2.append(temp[i])

        print()
        print("Gefundene Einträge:")
        print(temp2)
        print()

        if temp2 == []:
            print("Keine Person in der Datenbank mit dem Nachnamen", name)

        # Telefonnummer
        try:
            tel = int(input("Geben Sie die Telefonnummer an: "))

        except:
            print("Ungültige Eingabe")
            break

        if tel == int(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            del temp2
            return telbuch
            m = 1
            break

        for i in range(0, len(temp2)):
            if temp2[i][2] == int(tel):
                temp3.append(temp2[i])

        print()
        print("Zu mutierender Eintrag:")
        print(temp3)
        print()

        z = 0
        print("Wollen Sie diesen Eintrag mutieren und die neue Liste speichern?")
        print("1 = Ja")
        print("2 = Nein")
        z = int(input("Ihre Auswahl: "))

        if z == 1:
            for element in temp3:
                if element in telbuch:
                    telbuch.remove(element)

            b = True
            while b == True:
                vorname = str(input("Geben Sie den Vornamen an: "))
                name = str(input("Geben Sie den Nachnamen an: "))
                try:
                    tel = int(input("Geben Sie die Telefonnummer an: "))
                    b = False
                except:
                    print("Ungültige Eingabe")
                    print()
                    continue

            telbuch.append([vorname, name, tel])

            try:
                csv = open("Telefonbuch.csv", "w")
            except:
                print()
                print("Dateizugriff nicht erfolgreich.")
                print("Erforderliche Datei wird erstellt...")
                with open("Telefonbuch.csv", "w") as my_empty_csv:
                    pass
                print("Datei wurde erstellt. Bitte Programm neustarten")
                sys.exit(0)

            for i in telbuch:
                csv.write(i[0] + "," + i[1] + "," + str(i[2]) + "\n")
            csv.close()
            m = 1
            break

        elif z == 2:
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            m = 1
            return telbuch
            break

        else:
            print()
            print("Eingabe ungültig")
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            m = 1
            return telbuch
            break

    print()
    print("Zurück zum Hauptmenü...")
    print()

# Speicherfunktion
def save(telbuch):
    try:
        csv = open("Telefonbuch.csv", "w")
    except:
        print()
        print("Dateizugriff nicht erfolgreich.")
        print("Erforderliche Datei wird erstellt...")
        with open("Telefonbuch.csv", "w") as my_empty_csv:
            pass
        print("Datei wurde erstellt. Bitte Programm neustarten")
        sys.exit(0)

    for i in telbuch:
        csv.write(i[0] + "," + i[1] + "," + str(i[2]) + "\n")
    csv.close()

# Löschfunktion
def delete(telbuch):
    # Hauptschleife Löschen
    m = 0
    while m == 0:
        print()
        print("Um einen Eintrag zu Löschen, führen Sie die untenstehende Suche aus.")
        print("Sie können jederzeit Abbrechen, wenn Sie die Zahl 9 eingeben")
        print()
        temp = []
        temp2 = []
        temp3 = []

        #Vorname
        vorname = str(input("Geben Sie den Vornamen an: "))
        if vorname == str(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            return telbuch
            m = 1
            break

        for i in range(0, len(telbuch)):
            if telbuch[i][0].lower() == vorname.lower():
                temp.append(telbuch[i])
        print()
        print("Gefundene Einträge:")
        print(temp)
        print()

        if temp == []:
            print("Keine Person in der Datenbank mit dem Vornamen", vorname)
            break


        # Nachname
        name = str(input("Geben Sie den Nachnamen an: "))
        if name == str(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            del temp
            return telbuch
            m = 1
            break


        for i in range(0, len(temp)):
            if temp[i][1].lower() == name.lower():
                temp2.append(temp[i])

        print()
        print("Gefundene Einträge:")
        print(temp2)
        print()

        if temp2 == []:
            print("Keine Person in der Datenbank mit dem Nachnamen", name)

        # Telefonnummer
        try:
            tel = int(input("Geben Sie die Telefonnummer an: "))

        except:
            print("Ungültige Eingabe")
            break

        if tel == int(9):
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            del temp2
            return telbuch
            m = 1
            break

        for i in range(0, len(temp2)):
            if temp2[i][2] == int(tel):
                temp3.append(temp2[i])

        print()
        print("Zu löschender Eintrag:")
        print(temp3)
        print()

        z = 0
        print("Wollen Sie diesen Eintrag löschen und die neue Liste speichern?")
        print("1 = Ja")
        print("2 = Nein")
        z = int(input("Ihre Auswahl: "))

        if z == 1:
            for element in temp3:
                if element in telbuch:
                    telbuch.remove(element)

            try:
                csv = open("Telefonbuch.csv", "w")
            except:
                print()
                print("Dateizugriff nicht erfolgreich.")
                print("Erforderliche Datei wird erstellt...")
                with open("Telefonbuch.csv", "w") as my_empty_csv:
                    pass
                print("Datei wurde erstellt. Bitte Programm neustarten")
                sys.exit(0)

            for i in telbuch:
                csv.write(i[0] + "," + i[1] + "," + str(i[2]) + "\n")
            csv.close()
            m = 1
            break

        elif z == 2:
            print()
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            m = 1
            return telbuch
            break

        else:
            print()
            print("Eingabe ungültig")
            print("Abbrechen...")
            print("Zurück zum Hauptmenü...")
            print()
            m = 1
            return telbuch
            break

    print()
    print("Zurück zum Hauptmenü...")
    print()

# initialisieren
w = 0
x = 0
y = 0
z = 0
n_hm = True

# Willkommensmeldung
print()
print("Guten Tag,")
print("Willkommen im digitalen Telefonbuch!")
print()

# Hauptprogramm
while n_hm == True:                 # Hauptschleife
    print("Wählen Sie das entsprechende Menü aus:")
    print("1 = Suchfunktion")
    print("2 = Adressausgabe")
    print("3 = Eintrag anlegen")
    print("4 = Mutation")
    print("5 = Löschen")
    print("9 = Beenden")
    menu = input("Auswahl: ")

    # Zugriffsversuch / Lesen des Inhalts / Schliessen der Datei
    # Umwandeln in eine Liste von Zeilen / Zeilen Umwandeln
    try:
        csv = open("Telefonbuch.csv", "r")
    except:
        print()
        print("Dateizugriff nicht erfolgreich.")
        print("Erforderliche Datei wird erstellt...")
        with open("Telefonbuch.csv", "w") as my_empty_csv:
            pass
        print("Datei wurde erstellt. Bitte Programm neustarten")
        sys.exit(0)

    csvlist = csv.read()
    csv.close()
    kontaktinformation = csvlist.split(chr(10))
    ki = []
    for zeile in kontaktinformation:
        if zeile:
            kiliste = zeile.split(",")
            ki.append([str(kiliste[0]), str(kiliste[1]), int(kiliste[2])])

    # Testen, ob int
    try:
        menu = int(menu)
    # Kein int
    except:
        print("Ihre Eingabe wurde nicht erkannt")
        print()

    # 1 Öffnet Adresssucher
    if menu == 1:
        print()
        search(ki)
        del menu
        continue

    # 2 Öffnet Adressausgabe
    elif menu == 2:
        view(ki)
        print()
        del menu
        continue

    # 3 Öffnet Anlegen neuer Adressen
    elif menu == 3:
        print()
        savefile = new(ki)
        save(savefile)
        del menu
        continue

    # 4 Öffnet das Mutationsprogramm
    elif menu == 4:
        print()
        change(ki)
        del menu
        continue

    # 5 Öffnet die Löschfunktion
    elif menu == 5:
        delete(ki)
        del menu
        continue

    # 4 Programm ganz beenden
    elif menu == 9:
        print()
        print("Beenden...")
        n_hm = False

    # Falls eine andere Zahl angegeben wird
    else:
        print("Ihre Eingabe wurde nicht erkannt")
        print()
        continue

# Programm beenden
print()
print("Herzlichen Dank für Ihren Besuch und bis bald!")