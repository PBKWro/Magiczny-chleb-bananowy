import komunikaty
import os

def petla_gry():
    pass
    while True:
        print('sesae')

def petla_opcji():
    komunikaty.wyswietl_opcje()


def petla_menu():
    komunikaty.wyswietl_menu()
    wybor = input("> ")
    opcjeMenu = ["graj", "opcje", "pomoc", "autorzy"]
    while True:
        while wybor.lower() not in opcjeMenu:
            os.system("cls")
            komunikaty.wyswietl_menu()
            wybor = input("> ")
        if wybor == "graj":
            break
        elif wybor == "opcje":
            petla_opcji()
        elif wybor == "pomoc":
            komunikaty.wyswietl_pomoc()
        elif wybor == "autorzy":
            komunikaty.wyswietl_autorow()
        komunikaty.wyswietl_menu()
        wybor = input("> ")
    petla_gry()
    
    
petla_menu()