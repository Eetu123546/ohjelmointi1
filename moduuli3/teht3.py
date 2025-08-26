suku = input("Kerro sukupuoli: ")
hemo = float(input("Kerro hemoglobiini(g/l): "))

if suku == "mies":
    if hemo < 134:
        print("liian alhainen hemoglobiini")
    elif hemo > 195:
        print("liian korkea hemoglobiini")
    else:
        print("normaali hemoglobiini")

elif suku == "nainen":
    if hemo < 117:
        print("liian alhainen hemoglobiini")
    elif hemo > 175:
        print("liian korkea hemoglobiini")
    else:
        print("normaali hemoglobiini")

else:
    print("sukupuoli annettu väärin")
