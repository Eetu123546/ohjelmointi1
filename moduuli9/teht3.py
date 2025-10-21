from classes.auto import Auto

auto1 = Auto("ABC-123", 185)

auto1.nopeus = 60
auto1.matka = 2000
auto1.kulje(1.5)

print(f"Auto on kulkenut {auto1.matka:.0f} km.")