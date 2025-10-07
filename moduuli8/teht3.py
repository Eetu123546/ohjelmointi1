
from geopy.distance import geodesic
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True
)

def count_distance(icao1, icao2):
    sql = f"select latitude_deg, longitude_deg from airport where ident in ('{icao1}', '{icao2}')"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()

    if len(tulos) == 2:
        koord1 = tulos[0]
        koord2 = tulos[1]
        etäisyys = geodesic(koord1, koord2).kilometers
        print(f"Kahden lentokentän etäisyys on {etäisyys:.2f} km.")
    else:
        print("ICAO-koodit kirjoitettu väärin")

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

count_distance(icao1, icao2)