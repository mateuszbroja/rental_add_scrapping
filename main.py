from OLXParser import OLXParser
import argparse
print("""
Program do zapisywania ofert ze strony OLX do dokumentu JSON.
Wybierz miasto (warszawa, wroclaw, poznan, katowice, gdansk)
oraz ilość stron, jakie chcesz pobrać.
""")

my_parser = argparse.ArgumentParser(description='Pobieranie zawartości stron OLX')
my_parser.add_argument('Miasto',
                       type=str,
                       choices=['warszawa', 'wroclaw', 'poznan', 'katowice', 'gdansk'])
my_parser.add_argument('Liczba_stron',
                       type=int,
                       help=f'Podaj liczbę stron do eksportu (maks. 25)')
args = my_parser.parse_args()
miasto = args.Miasto
liczba_stron = args.Liczba_stron

OLX = OLXParser()

for i in range(1, liczba_stron):
    OLX.pobierz_dane_requests(f'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{miasto}/?page={i}')
    OLX.transformuj_soup()
    OLX.znajdz_mieszkania()
    OLX.zbierz_dane_ze_strony()

OLX.rozpoznaj_liczbe_stron()
OLX.zapisz_dane_json("mieszkania_OLX.json")

if OLX.liczba_str == liczba_stron:
    print(f'{liczba_stron} stron zapisanych w miejscu docelowym (format JSON).')
else:
    print(f'{OLX.liczba_str} stron zapisanych (z podanych {liczba_stron}) w miejscu docelowym (format JSON).')