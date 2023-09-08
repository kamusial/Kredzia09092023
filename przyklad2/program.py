from f1 import *
from f2 import *
from f3 import *

#program oblicza koszt budowy domu

#f1 - funkcja przyjmuje metraz domu i zwraca podatek do zapłaty
#f2 - funkcja przyjmuje listę wykorzystywanych materiałów i zwraca
# informację, czy mozna budowac
#f3 - funkcja przyjmuje metraż domu i zwraca całościowy potrzebny metraż działki


metraz = int(input('Podaj metraz domu, ktory budujesz '))
podatek = podatek(metraz)

lista_materialow = []

while True:
    material = input('Z czego budujesz? ')
    lista_materialow.append(material)
    decyzja = input('Czy chcesz wprowadzic kolejny material?   ')
    if decyzja == 'Nie':
        break

if pozwolenie(lista_materialow):
    print('Mozna budowac')
    a, b = input('Podaj wymiary domu ').split()
    metraz_dzialki = powierzchnia(int(a), int(b))
    print(f'calkowity metraz dzialki potrzebny do budowy domu {a}x{b} = {metraz_dzialki}')
else:
    print('koniec, nie mozna budowac')



