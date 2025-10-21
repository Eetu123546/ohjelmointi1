class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = self.alin_kerros

    def kerros_ylös(self):
        if self.kerros == self.ylin_kerros:
            print("Hissi on jo ylimmässä kerroksessa")
        else:
            self.kerros = self.kerros + 1
            print(f"Hissi on kerroksessa: {self.kerros}")

    def kerros_alas(self):
        if self.kerros == self.alin_kerros:
            print("Hissi on jo alimmassa kerroksessa")
        else:
            self.kerros = self.kerros - 1
            print(f"Hissi on kerroksessa: {self.kerros}")

    def siirry_kerrokseen(self, arvo):
        if arvo < self.alin_kerros or arvo > self.ylin_kerros:
            print("Tuota kerrosta ei ole olemassa.")
        else:
            while self.kerros < arvo:
                self.kerros_ylös()
            while self.kerros > arvo:
                self.kerros_alas()