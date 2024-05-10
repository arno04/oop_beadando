from datetime import datetime

class Szoba():
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyAgyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetAgyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_feltoltes(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        if datum < datetime.now():
            print("Hibás dátum! Csak jövőbeli foglalás lehetséges.")
            return
        for foglalas in self.foglalasok:
            if foglalas[0] == szoba and foglalas[1] == datum:
                print("Ez a szoba már foglalt ezen a napon.")
                return
        self.foglalasok.append((szoba, datum))
        print("Sikeres foglalás.")

    def lemondas(self, szoba, datum):
        if (szoba, datum) in self.foglalasok:
            self.foglalasok.remove((szoba, datum))
            print("Sikeres lemondás.")
        else:
            print("Nincs ilyen foglalás az adott szobára és dátumra.")

    def listaz_foglalasok(self):
        if len(self.foglalasok) == 0:
            print("Nincsenek foglalások.")
        else:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"Szoba: {foglalas[0]}, Dátum: {foglalas[1]}")

szalloda = Szalloda("hotel egy")
szalloda.szoba_feltoltes(EgyAgyasSzoba("1"))
szalloda.szoba_feltoltes(KetAgyasSzoba("2"))
szalloda.szoba_feltoltes(KetAgyasSzoba("3"))


foglalas = Foglalas()
foglalas.foglalas("1", datetime(2024, 5, 20))
foglalas.foglalas("2", datetime(2024, 5, 12))
foglalas.foglalas("3", datetime(2024, 5, 14))
foglalas.foglalas("2", datetime(2024, 5, 16))
foglalas.foglalas("2", datetime(2024, 5, 18))
foglalas.listaz_foglalasok()

while True:
    print("Válasszon műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    valasztas = input("Művelet kiválasztása (1/2/3): ")

    if valasztas == "1":
        be_szobaszam = input("Adja meg a foglalandó szoba számát: ")
        datum_input = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(datum_input, "%Y-%m-%d")
        except ValueError:
            print("Hibás dátumformátum!")
            continue
        foglalas.foglalas(be_szobaszam, datum)
        foglalas.listaz_foglalasok()
    elif valasztas == "2":
        szobaszam = input("Adja meg a lemondandó foglalás szoba számát: ")
        be_datum = input("Adja meg a lemondandó foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(be_datum, "%Y-%m-%d")
        except ValueError:
            print("Hibás dátumformátum!")
            continue
        foglalas.lemondas(szobaszam, datum)
        foglalas.listaz_foglalasok()
    elif valasztas == "3":
        foglalas.listaz_foglalasok()
    else:
        print("Hibás választás! Kérem, válasszon a megadott lehetőségek közül.")
