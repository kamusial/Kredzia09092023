from funkcja_waluty import *
import funkcja_ryzyko, funkcja_rodzaj_inwestycji
#program pryzjmuje ilość pieniędzy z złutych
#program konwertuje na dolary
#program ustala akceptowalny poziom ryzyka
#program podpowiada, w co inwestować

kasa = int(input('Ile masz pieniedzy '))
kasa_w_USD = przelicznik(kasa)

wiek = int(input('Ile masz lat? '))
plec = input('Plec K/M')
wyksztalcenie = input('Wyksztalcenie? ')

poziom_ryzyka = funkcja_ryzyko.poziom_ryzyka(wiek, plec, wyksztalcenie)


