import json

class Mapa:

    def __init__(self, xd, yt):
        self.nazwa = xd
        self.opis = yt
        
    def wyswietlMnie(self):
        print("Nazwa: " + self.nazwa + ", Opis: " + self.opis)


with open("map.json") as f:
    data_string = f.read()

data = json.loads(data_string)
print(data)

lista_lokacji = []

for obj in data:
    nazwa = data[obj]['nazwa']
    opis = data[obj]['opis']
    lista_lokacji.append(Mapa(nazwa,opis))

for lokacja in lista_lokacji:
    lokacja.wyswietlMnie()