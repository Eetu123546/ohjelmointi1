luodit = 13.3 * float(input("Kerro luodit: "))
naulat = 425.6 * float(input("Kerro naulat: "))
leiviskat = 8512 * float(input("Kerro leiviskät: "))

summa = naulat + leiviskat + luodit
kg = summa / 1000
g = summa - int(kg) * 1000

print("Massa nykymittojen mukaan:")
print(f"{int(kg)} kilogrammaa ja {int(g)} grammaa")