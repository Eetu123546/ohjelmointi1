
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Idai98rou.',
         autocommit=True
         )

def print_airport_types(code):
    sql = f"""select type, count(*) from airport where iso_country = '{code}' group by type order by count(*) desc"""
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()

    if cursor.rowcount > 0:
        for rivi in tulos:
            print(f"Tyyppi: {rivi[0]} Määrä: {rivi[1]}")
    else:
        print("Tällä maakoodilla ei löydy lentokenttiä.")

koodi = input("Anna maakoodi: ")

print_airport_types(koodi)
