class Uzytkownik:
    def __init__(self, imie, nazwisko, saldo = 0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo
        print("stworzono użytkownika")

    def wplata(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            print(f"wpłacono {kwota}. jest teraz {self.saldo}")
        else:
            print("kwota musi być większa niż 0")
    
    def wyplata(self, kwota):
        if kwota > self.saldo:
            print("nie masz wystarczającej ilości środków")
        elif kwota > 0:
            self.saldo -= kwota
        else:
            print(f"kwota wypłaty musi być większa od 0")

    def pokaz_saldo(self):
        print(f"Aktualna ilość pieniędzy u użytkownika {self.imie} {self.nazwisko} wynosi {self.saldo} zł.")

class Bankomat:
    def __init__(self):
        self.konta = {}
        self.zalogowany_uzytkownik = None
        print("Stworzono bankomat")

    def dodaj_konto(self, numer_karty, imie, nazwisko, pin, saldo = 0):
        if numer_karty not in self.konta:
            self.konta[numer_karty] = {"uzytkownik": Uzytkownik(imie, nazwisko, saldo),
                                       "pin": pin}
            print(f"Konto dla {imie} {nazwisko} zostało dodane")
        else:
            print("Numer karty jest już zajęty")

    def zaloguj(self, numer_karty, pin):
        if numer_karty in self.konta:
            if self.konta[numer_karty]["pin"] == pin:
                self.zalogowany_uzytkownik = numer_karty
                print(f"Zalogowano do konta {numer_karty}.")
                return True
            else:
                print(f"błędny numer pin")
                return False
        else:
            print("Nie znaleziono karty o podanym numerze.")
            return False
    
    def wyloguj(self):
        if self.zalogowany_uzytkownik:
            print(f"Wylogowano użytkownika: {self.zalogowany_uzytkownik}")
            self.zalogowany_uzytkownik = None
        else:
            print("Żaden użytkownik nie jest zalogowany")
    
    def wplata_wyplata(self, kwota, wplataCzyWyplata):
        if self.zalogowany_uzytkownik:
            uzytkownik = self.konta[self.zalogowany_uzytkownik]["uzytkownik"]
            match wplataCzyWyplata:
                case "wplata":
                    uzytkownik.wplata(kwota)
                case "wyplata":
                    uzytkownik.wyplata(kwota)
        else:
            print("Żaden użytkownik nie jest zalogowany")

    def pokazSaldo(self):
        if self.zalogowany_uzytkownik:
            uzytkownik = self.konta[self.zalogowany_uzytkownik]["uzytkownik"]
            uzytkownik.pokaz_saldo()
        else:
            print("Żaden użytkownik nie jest zalogowany")

    def pokaz_wszystkie_konta(self):
        if self.konta:
            print("\nLista wszystkich kont:")
            for numer_karty, dane_konta in self.konta.items():
                uzytkownik, pin = dane_konta["uzytkownik"], dane_konta["pin"]

                print(f"Karta: {numer_karty}, PIN: {pin}, Imię: {uzytkownik.imie}, Nazwisko: {uzytkownik.nazwisko}, "
                    f"Saldo: {uzytkownik.saldo:.2f} zł")
        else:
            print("Brak kont w bankomacie.")
bankomat = Bankomat()
start_prog = True
while start_prog:
    wybor = input("\n--- MENU ---\n1. Dodaj konto\n2. Zaloguj się\n3. Pokaż wszystkie konta\n4. Wyjdź z programu\nWybierz opcję: ")
    match wybor:
        case "1":
            numer_karty = input("Podaj numer karty: ")
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            pin = input("Podaj PIN: ")
            saldo_input = input("Podaj początkowe saldo (domyślnie 0): ")
            saldo = float(saldo_input) if saldo_input.strip() else 0.0
            bankomat.dodaj_konto(numer_karty, imie, nazwisko, pin, saldo)

        case "2":
            numer_karty = input("Podaj numer karty: ")
            pin = input("podaj pin: ")
            if bankomat.zaloguj(numer_karty, pin):
                zalogowany = True
                while zalogowany:
                    wybor2 = input("\n--- MENU ---\n1. Sprawdź saldo\n2. Wpłać lub wypłać środki\n3. Wyloguj\nWybierz opcję: ")
                    match wybor2:
                        case "1":
                            bankomat.pokazSaldo()
                        case "2":
                            co_robic = input("Napisz czy chcesz wpłacać(wplata) czy wypłacać(wyplata): ")
                            kwota = float(input(f"Podaj kwotę ({co_robic}): "))
                            bankomat.wplata_wyplata(kwota, co_robic)
                        case "3":
                            bankomat.wyloguj()
                            zalogowany = False
                        case _:
                            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            else:
                print("Nie udało się zalogować. Sprawdź numer karty i PIN")
        case "3":
            bankomat.pokaz_wszystkie_konta()
        case "4":
            print("Dziękujemy za skorzystanie z bankomatu")
            start_prog = False
        case _:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            
            
    #historia, kontoADM, ilosc prob logowania i blokada po 3,  