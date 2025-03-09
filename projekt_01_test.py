ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyber možnost (1-4): ")
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu")
            exit()
        else:
            print("Neplatná volba, zkus to znovu.")

def pridat_ukol():
    nazev = input("Zadej název úkolu: ")
    popis = input("Zadej popis úkolu: ")
    
    if nazev and popis:
        ukoly.append({"název": nazev, "popis": popis})
        print("Úkol byl přidán.")
    else:
        print("Název a popis úkolu nemůžou být prázdné.")

def zobrazit_ukoly():
    if ukoly:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['název']} - {ukol['popis']}")
    else:
        print("\nŽádný úkol nebyl přidán.")

def odstranit_ukol():
    if not ukoly:
        print("\nŽádný úkol k odstranění.")
        return
    
    zobrazit_ukoly()
    try:
        cislo_ukolu = int(input("Zadej číslo úkolu, který chceš odstranit: "))
        if 1 <= cislo_ukolu <= len(ukoly):
            odstraneny_ukol = ukoly.pop(cislo_ukolu - 1)
            print(f"Úkol '{odstraneny_ukol ['název']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Prosím zadej platné číslo.")
        
if __name__ == "__main__":
    hlavni_menu()