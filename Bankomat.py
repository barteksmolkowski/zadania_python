class Uzytkownik:
    def __init__(self, imie, nazwisko, saldo = 0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo
        print("stworzono użytkownika")

    def wplata(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            historia.dodaj(f"{self.imie} {self.nazwisko} dokonał wpłaty w wysokości {kwota} i ma teraz {self.saldo}")
            print(f"Wpłacono {kwota}. Jest teraz {self.saldo}")
        else:
            print("Kwota wpłaty musi być większa od zera.")
    
    def wyplata(self, kwota):
        if kwota > self.saldo:
            print("nie masz wystarczającej ilości środków")
        elif kwota > 0:
            self.saldo -= kwota
            historia.dodaj(f"{self.imie} {self.nazwisko} dokonał wypłaty w wysokości {self.kwota} i ma teraz {self.saldo}")
        else:
            print(f"kwota wypłaty musi być większa od 0")

    def pokaz_saldo(self):
        print(f"Aktualna ilość pieniędzy u użytkownika {self.imie} {self.nazwisko} wynosi {self.saldo} zł.")
        historia.dodaj(f"Wyświetlono saldo użytkownika {self.imie} {self.nazwisko} które wynosi {self.saldo} zł.")

class Bankomat:
    def __init__(self, historia):
        self.konta = {}
        self.zalogowany_uzytkownik = None
        self.historia = historia
        print("Stworzono bankomat")

    def dodaj_konto(self, numer_karty, imie, nazwisko, pin, saldo=0):
        if numer_karty not in self.konta:

            self.konta[numer_karty] = {
                "uzytkownik": Uzytkownik(imie, nazwisko, saldo),
                "pin": pin
            }

            komunikat = f"Konto dla {imie} {nazwisko} zostało dodane."
            print(komunikat)
            self.historia.dodaj(komunikat)

        else:
            komunikat = "Numer karty jest już zajęty."
            print(komunikat)
            self.historia.dodaj(komunikat)

    def zaloguj(self, numer_karty, pin):
        if numer_karty in self.konta:

            if self.konta[numer_karty]["pin"] == pin:
                self.zalogowany_uzytkownik = numer_karty
                komunikat = f"Zalogowano do konta {numer_karty}."
                print(komunikat)
                self.historia.dodaj(komunikat)
                return True
            
            else:
                komunikat = "Błędny numer PIN."
                print(komunikat)
                self.historia.dodaj(komunikat)
                return False
        else:
            komunikat = "Nie znaleziono karty o podanym numerze."
            print(komunikat)
            self.historia.dodaj(komunikat)
            return False

    def wyloguj(self):
        if self.zalogowany_uzytkownik:
            komunikat = f"Wylogowano użytkownika: {self.zalogowany_uzytkownik}."
            print(komunikat)
            self.historia.dodaj(komunikat)
            self.zalogowany_uzytkownik = None

        else:
            komunikat = "Żaden użytkownik nie jest zalogowany."
            print(komunikat)
            self.historia.dodaj(komunikat)

    def wplata_wyplata(self, kwota, wplataCzyWyplata):
        if self.zalogowany_uzytkownik:

            uzytkownik = self.konta[self.zalogowany_uzytkownik]["uzytkownik"]
            match wplataCzyWyplata:

                case "wplata":
                    uzytkownik.wplata(kwota)
                    komunikat = f"Dokonano wpłaty {kwota} zł na konto {self.zalogowany_uzytkownik}."
                    self.historia.dodaj(komunikat)

                case "wyplata":
                    uzytkownik.wyplata(kwota)
                    komunikat = f"Dokonano wypłaty {kwota} zł z konta {self.zalogowany_uzytkownik}."
                    self.historia.dodaj(komunikat)
        else:
            komunikat = "Żaden użytkownik nie jest zalogowany."
            print(komunikat)
            self.historia.dodaj(komunikat)

    def pokazSaldo(self):
        if self.zalogowany_uzytkownik:
            uzytkownik = self.konta[self.zalogowany_uzytkownik]["uzytkownik"]
            uzytkownik.pokaz_saldo()
            komunikat = f"Wyświetlono saldo użytkownika {self.zalogowany_uzytkownik}."
            self.historia.dodaj(komunikat)
        else:
            komunikat = "Żaden użytkownik nie jest zalogowany."
            print(komunikat)
            self.historia.dodaj(komunikat)

    def pokaz_wszystkie_konta(self):
        if self.konta:

            print("\nLista wszystkich kont:")
            for numer_karty, dane_konta in self.konta.items():

                uzytkownik, pin = dane_konta["uzytkownik"], dane_konta["pin"]
                komunikat = (f"Karta: {numer_karty}, PIN: {pin}, Imię: {uzytkownik.imie}, "
                             f"Nazwisko: {uzytkownik.nazwisko}, Saldo: {uzytkownik.saldo:.2f} zł")
                print(komunikat)
                self.historia.dodaj(komunikat)
        else:
            komunikat = "Brak kont w bankomacie."
            print(komunikat)
            self.historia.dodaj(komunikat)

class Historia:
    def __init__(self):
        self.historia = []

    def dodaj(self, tekst):
        self.historia.append(tekst)

    def wyswietl(self):
        for i in range(len(self.historia)):
            print(f"[ {i + 1} ] {self.historia[i]}")

    def resetuj(self):
        self.historia = []

    def cofnij(self):
        if self.historia:
            ostatni_wpis = self.historia.pop()
            print(f"Usunięto ostatni wpis: {ostatni_wpis}")
        else:
            print("Historia jest pusta. Nie można cofnąć wpisu.")

    def wyswietl_posortowane(self, odwrotnie=False):
        posortowane = sorted(self.historia, reverse=odwrotnie)
        porzadek = "malejąco" if odwrotnie else "rosnąco"
        print(f"Historia (posortowana {porzadek}):")
        for i, wpis in enumerate(posortowane, start=1):
            print(f"[ {i} ] {wpis}")

    def filtruj(self, slowo_kluczowe):
        print(f"Filtracja według: '{slowo_kluczowe}'")
        wyniki = [wpis for wpis in self.historia if slowo_kluczowe.lower() in wpis.lower()]
        if wyniki:
            for i, wpis in enumerate(wyniki, start=1):
                print(f"[ {i} ] {wpis}")
        else:
            print("Brak wyników spełniających kryteria filtrowania.")

def wiele_input(bankomat, ile_kont=1):
    for i in range(ile_kont):
        print(f"\nDodawanie konta #{i + 1}:")
        numer_karty = input("Podaj numer karty: ").strip()
        imie = input("Podaj imię: ").strip()
        nazwisko = input("Podaj nazwisko: ").strip()
        
        while True:
            print(f"\nDodawanie konta #{i + 1}:")
            print(f"Podaj numer karty: {numer_karty}")
            print(f"Podaj imię: {imie}")
            print(f"Podaj nazwisko: {nazwisko}")
            pin = input("Podaj PIN (4 cyfry): ").strip()
            if len(pin) == 4 and pin.isdigit():
                break
            print("PIN musi składać się z 4 cyfr. Spróbuj ponownie.")
        
        saldo_input = input("Podaj początkowe saldo (domyślnie 0): ").strip()
        try:
            saldo = float(saldo_input) if saldo_input else 0.0
        except ValueError:
            print("Nieprawidłowa wartość. Saldo ustawiono na 0.")
            saldo = 0.0

        # Dodanie konta do bankomatu
        bankomat.dodaj_konto(numer_karty, imie, nazwisko, pin, saldo)

    print(f"\nDodano {ile_kont} konto/kont.")

historia = Historia()
bankomat = Bankomat(historia)

# Główna pętla programu
start_prog = True
while start_prog:
    wybor = input("\n--- MENU ---\n1. Dodaj konto\n2. Stwórz wiele kont\n3. Zaloguj się\n4. Pokaż wszystkie konta\n5. Historia\nWyjdź z programu => exit\nWybierz opcję: ")
    match wybor:
        case "1":
            # Dodawanie pojedynczego konta
            numer_karty = input("Podaj numer karty: ")
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            pin = input("Podaj PIN: ")
            saldo_input = input("Podaj początkowe saldo (domyślnie 0): ")
            saldo = float(saldo_input) if saldo_input.strip() else 0.0
            bankomat.dodaj_konto(numer_karty, imie, nazwisko, pin, saldo)

        case "2":
            # Dodawanie wielu kont
            ile_kont = int(input("Ile kont chcesz dodać? "))
            wiele_input(bankomat, ile_kont)

        case "3":
            # Logowanie użytkownika
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

        case "4":
            # Wyświetlanie wszystkich kont
            bankomat.pokaz_wszystkie_konta()

        case "5":
            # Menu historii
            historia_menu = True
            while historia_menu:
                print("\n--- HISTORIA ---\n1. Wyświetl historię\n2. Filtruj historię\n3. Zresetuj historię\n4. Powrót do menu głównego")
                wybor_historia = input("Wybierz opcję: ")
                match wybor_historia:
                    case "1":
                        bankomat.historia.wyswietl()
                    case "2":
                        slowo_kluczowe = input("Podaj słowo kluczowe do filtrowania: ")
                        bankomat.historia.filtruj(slowo_kluczowe)
                    case "3":
                        bankomat.historia.resetuj()
                    case "4":
                        historia_menu = False
                    case _:
                        print("Nieprawidłowy wybór. Spróbuj ponownie.")

        case "exit":
            print("Dziękujemy za skorzystanie z bankomatu")
            start_prog = False

        case _:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")