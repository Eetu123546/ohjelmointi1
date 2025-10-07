import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Idai98rou.',
         autocommit=True
         )

def hae_kenttä(icao):
    sql = f"select name, municipality from airport where ident = '{icao}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()

    if cursor.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokenttä: {rivi[0]} Sijainti: {rivi[1]}")
    else:
        print(f"ICAO-koodilla {icao} ei löytynyt lentokenttää.")

icao = input("Anna ICAO-koodi: ")
hae_kenttä(icao)