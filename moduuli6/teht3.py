
def muunnin(ga):
    li = ga * 3.785
    return li

g = 1

while True:
    g = int(input("Montako gallonia muutat litroiksi: "))
    if g < 0:
        break
    print(f"{g} gallonia on {muunnin(g)} litraa")

print("annoit negatiivisen luvun: ERROR")