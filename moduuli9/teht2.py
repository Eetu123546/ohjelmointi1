from classes.auto import Auto

auto1 = Auto("ABC-123", 185)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f"Auton nopeus: {auto1.nopeus}")

auto1.kiihdytä(-200)

print(f"Auton nopeus jarrutuksen jälkeen: {auto1.nopeus}")