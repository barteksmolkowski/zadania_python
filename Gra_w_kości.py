from random import randint
from collections import Counter
import re

gracze = ["Gracz 1", "Gracz 2"]
tabele_punktacji = [
    {  # Tabela Gracza 1
        "Jedynki": 0, "Dwójki": 0, "Trójki": 0, "Czwórki": 0, "Piątki": 0, "Szóstki": 0,
        "Trzy jednakowe": 0, "Cztery jednakowe": 0, "Full": 0, "Mały strit": 0, "Duży strit": 0, "Yahtzee": 0,
        "Szansa": 0, "Bonus Yahtzee": 0
    },
    {  # Tabela Gracza 2
        "Jedynki": 0, "Dwójki": 0, "Trójki": 0, "Czwórki": 0, "Piątki": 0, "Szóstki": 0,
        "Trzy jednakowe": 0, "Cztery jednakowe": 0, "Full": 0, "Mały strit": 0, "Duży strit": 0, "Yahtzee": 0,
        "Szansa": 0, "Bonus Yahtzee": 0
    }
]
kości = [1, 2, 3, 4, 5]

def ocena_kategorii(kategoria, kości):
    kości_count = Counter(kości)
    match kategoria:
        case "Jedynki": return kości.count(1)
        case "Dwójki": return kości.count(2) * 2
        case "Trójki": return kości.count(3) * 3
        case "Czwórki": return kości.count(4) * 4
        case "Piątki": return kości.count(5) * 5
        case "Szóstki": return kości.count(6) * 6
            
        case "Trzy jednakowe":
            for count in kości_count.values():
                if count >= 3:
                    return sum(kości)
            return 0
        case "Full":
            if set(kości_count.values()) == {2, 3}:
                return 25
            return 0
        case "Mały strit":
            mały_strit = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
            if set(kości) in mały_strit:
                return 30
            return 0
        case "Duży strit":
            duży_strit = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]
            if set(kości) in duży_strit:
                return 40
            return 0
        case "Yahtzee":
            if len(set(kości)) == 1:
                return 50
            return 0
        case "Szansa":
            return sum(kości)
        case _:
            return 0

def usunPoprzednie():
    print("\n" * 30)

def pokazKości():
    print("\nTwoje aktualne kości:")
    print("+" + "-" * 22 + "+")
    for i in range(len(kości)):
        print(f"| {i+1}. Kość: {kości[i]}{' ' * (11 - len(str(kości[i])))}|")
    print("+" + "-" * 22 + "+\n")

def rzućKoścmi(numery_kości: str):
    for i in map(int, numery_kości):
        if 1 <= i <= len(kości):
            kości[i - 1] = randint(1, 6)

def sprawdzCzyPrzerzucamy():
    if BezTestu:
        odp = input("Czy chcesz przerzucić kości? (t/n): ").strip().lower()
    else:
        odp = "t"
    return odp in ["t", "tak"]

def sprawdz_kategorie(pole):
    if re.match(r"^[Jj]ed[uytgh]n?k?i?", pole):
        return "Jedynki"
    
    elif re.match(r"^[Dd]w[óo]jk?i?", pole):
        return "Dwójki"
    
    elif re.match(r"^[Tt]r[óo]j?k?i?", pole):
        return "Trójki"
    
    elif re.match(r"^[Cc]zw[óo]r?k?i?", pole):
        return "Czwórki"
    
    elif re.match(r"^[Pp]i[ąa]t?k?i?", pole):
        return "Piątki"
    
    elif re.match(r"^[Ss]z[óo]s?t?ki?", pole):
        return "Szóstki"
    
    elif re.match(r"^[Tt]rzy?\s?[j]edn?a?k?o?w?e?", pole): 
        return "Trzy jednakowe"
    
    elif re.match(r"^[Cc]ztery?\s?[j]ed?n?a?k?o?w?e?", pole): 
        return "Cztery jednakowe"
    
    elif re.match(r"^[Ff]ull?", pole): 
        return "Full"
    
    elif re.match(r"^[Mm]ały\s?[Ss]tr?i?t?", pole): 
        return "Mały strit"
    
    elif re.match(r"^[Dd]uży\s?[Ss]tr?i?t?", pole): 
        return "Duży strit"
    
    elif re.match(r"^[Yy]aht?z?e?e?", pole): 
        return "Yahtzee"
    
    elif re.match(r"^[Ss]z?a?n?s?a?", pole): 
        return "Szansa"
    
    elif re.match(r"^[Bb]onus\s?[Yy]ah?t?z?e?e?", pole): 
        return "Bonus Yahtzee"
    
    else:
        return "Nie znaleziono"

def wstawPunkty(tabela):
    while True:
        print("\nDostępne kategorie punktacji:")

        dostępne_kategorie = {kategoria: ocena_kategorii(kategoria, kości) 
                              for kategoria, punkty in tabela.items() if punkty == 0}
        
        if dostępne_kategorie:
            if BezTestu:
                while True:
                    usunPoprzednie()
                    for kategoria, punkty in dostępne_kategorie.items():
                        print(f"{kategoria}: {punkty} punktów do zdobycia")

                    pole = input("\nWybierz kategorię, do której chcesz wstawić punkty: ").strip()
                    kategoria = sprawdz_kategorie(pole)
                    
                    if kategoria == "Nie dopasowano żadnej kategorii!":
                        print("Podano złą kategorię, spróbuj ponownie...")
                    else:
                        break

            else:
                kategoria = max(dostępne_kategorie, key=dostępne_kategorie.get)
                print(f"\nAutomatycznie wybrano kategorię: {kategoria} z wynikiem {dostępne_kategorie[kategoria]}")

            tabela[kategoria] = dostępne_kategorie[kategoria]
            print(f"\nPunkty {dostępne_kategorie[kategoria]} zostały dodane do kategorii: {kategoria}")
            break

        else:
            print("\nNie ma już dostępnych kategorii do wypełnienia!")
            break

BezTestu = input("Test? (t/n): ")
BezTestu = True if BezTestu == "n" else False

for runda in range(len(tabele_punktacji[0])):
    for i, gracz in enumerate(gracze):
        if all(punkty != 0 for punkty in tabele_punktacji[i].values()):
            print(f"{gracz} nie ma już dostępnych kategorii! Gra kończy się.")
            break

        print(f"\nTura: {gracz}")
        print("--------------------")
        
        rzućKoścmi("12345")
        pokazKości()

        for _ in range(2):
            if sprawdzCzyPrzerzucamy():
                numery = input("Wpisz numery kości, które chcesz przerzucić (bez spacji): ")
                rzućKoścmi(numery)
                pokazKości()
            else:
                break

        if BezTestu:
            wstawPunkty(tabele_punktacji[i])
        else:
            dostępne_kategorie = {kategoria: ocena_kategorii(kategoria, kości) 
                                  for kategoria, punkty in tabele_punktacji[i].items() if punkty == 0}
            if dostępne_kategorie:
                najlepsza_kategoria = max(dostępne_kategorie, key=dostępne_kategorie.get)
                tabele_punktacji[i][najlepsza_kategoria] = dostępne_kategorie[najlepsza_kategoria]
                print(f"Automatycznie wybrano kategorię: {najlepsza_kategoria} z wynikiem {dostępne_kategorie[najlepsza_kategoria]}")
            else:
                print(f"{gracz} nie ma już dostępnych kategorii!")


print("\nKoniec gry!")

wyniki = []
for i, gracz in enumerate(gracze):
    suma = sum(tabele_punktacji[i].values())
    wyniki.append((gracz, suma, tabele_punktacji[i]))
    
    print(f"\n{gracz}:")
    for kategoria, punkty in tabele_punktacji[i].items():
        if punkty > 0:
            print(f" - {kategoria}: {punkty} punktów")
    print(f"Suma punktów: {suma} punkty")

zwycięzca = max(wyniki, key=lambda x: x[1])
print(f"\nZwycięzcą jest: {zwycięzca[0]} z {zwycięzca[1]} punktami! 🎉")

print(f"\nSzczegóły punktów dla zwycięzcy:")
for kategoria, punkty in tabele_punktacji[gracze.index(zwycięzca[0])].items():
    if punkty > 0:
        print(f"{kategoria}: {punkty} punktów")
print(f"Łączna liczba punktów: {zwycięzca[1]} punktów!")
