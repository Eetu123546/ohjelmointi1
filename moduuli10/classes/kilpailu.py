import random

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self, ):
        print(f"""
        {self.kilpailun_nimi} Tilanne:""")
        for auto in self.autot:
            print(f"""
            Rekisteritunnus: {auto.rekisteritunnus}
            Huippunopeus: {auto.huippunopeus} km/h
            Nopeus: {auto.nopeus} km/h
            Matka kuljettu: {auto.matka} km""")

    def kilpailu_ohi(self):
        if any(auto.matka >= self.kilpailun_pituus for auto in self.autot):
            return True
