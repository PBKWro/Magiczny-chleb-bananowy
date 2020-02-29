import sys
import os
import time
import webbrowser

def wyswietl_menu():
    print("###########################")
    print("# Magiczny Chleb Bananowy #")
    print("###########################")
    print("#      Witaj w menu!      #")
    print("#-------------------------#")
    print("#    - Rozpocznij gre -   #") 
    print("#        - Opcje -        #")
    print("#        - Pomoc -        #")
    print("###########################")
    print("#      Studio PBKWro      #")
    print("###########################")              

def wyswietl_pomoc():
    print("##############################################################################")
    print("#                              Witaj w poradniku!                            #")
    print("##############################################################################")
    print("#      Grą sterujesz za pomocą komend ktore wpisujesz malymi literami        #")
    print("# - Lista podstawowych komend -                                              #")
    print("# 1. Poruszanie sie:                                                         #")
    print("# -Idz, ruch, rusz, bieg                                                     #")
    print("# -Lewo, Prawo, Gora, Dol                                                    #")
    print("# 2. Interakcje:                                                             #")
    print("#-Patrz, zobacz, inspektuj, uzyj, wez, podnies, upusc, rzuc, wyjmij, zabierz #")
    print("##############################################################################")
    input("> ")
    os.system("cls")


def wyswietl_autorow():
    print("####################")
    print("#     - Rudy -     #")
    print("#   - Wieśniak -   #")
    print("#    - Kajtek -    #")
    print("####################")
    input("> ")
    os.system("cls")


def wolne_wyswietlanie(wiadomosc):
    for character in wiadomosc:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

def tryb_samolotowy():
    wiadomosc_tryb_samolotowy = "Nastąpi teraz przeniesienie do trybu samolotowego."
    wolne_wyswietlanie(wiadomosc_tryb_samolotowy)
    webbrowser.open('https://www.youtube.com/watch?v=PpOoIaYm-Yo')


def wyswietl_opcje():
    print("####################################")
    print("#            - Grafika -           #")
    print("#            - Muzyka -            #")
    print("#             - Mysz -             #")
    print("#           - Rozgrywka -          #")
    print("#         - Tryb sieciowy -        #")
    print("#             - Język -            #")
    print("#         - Tryb sterowania -      #")
    print("#        - Tryb streamowania -     #")
    print("#         - Tryb samolotowy -      #")
    print("#         - Tryb pociągowy -       #")
    print("# - Tryb kontroli rodzicielskiej - #")
    print("#            - Tryb 2D -           #")
    print("#            - Tryb 3D -           #")
    print("#              - VR -              #")
    print("#          - Tryb ( ͡° ͜ʖ ͡°)  -      #")
    print("#          - Tryb koszerny -       #")
    print("#     - Nie uruchamiaj tego!!! -   #")
    print("#        - rudy sie nie myje  -    #")
    print("####################################")
    input("> ")
    os.system("cls")

