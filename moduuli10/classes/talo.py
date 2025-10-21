from hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []
        for i in range(hissien_määrä):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)