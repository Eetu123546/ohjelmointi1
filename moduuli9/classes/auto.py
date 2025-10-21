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

        # lisää arvo self nopeuteen
        # tarkasta että nopeus ei ole yli huippunopeus
        # tarkasta että nopeus ei ole alle nolla