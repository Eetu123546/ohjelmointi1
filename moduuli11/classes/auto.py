class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, arvo):
        self.arvo = arvo
        if self.arvo + self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.arvo < 0:
            if self.nopeus + self.arvo < 0:
                self.nopeus = 0
            else:
                self.nopeus = self.nopeus + self.arvo
        else:
            self.nopeus = self.nopeus + self.arvo

    def kulje(self, aika):
        self.aika = aika
        if self.matka + self.aika * self.nopeus < 0:
            self.matka = 0
        else:
            self.matka = self.matka + self.aika * self.nopeus

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        self.tankin_koko = tankin_koko
        super().__init__(rekisteritunnus, huippunopeus)