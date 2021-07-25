import requests
from bs4 import BeautifulSoup
import json


class OLXParser:

    def __init__(self):
        self.OLX_html = None
        self.OLX_soup = None
        self.mieszkania = None
        self.mieszkania_czyste = []
        self.mieszkania_json = None
        self.liczba_str = 1

    def pobierz_dane_requests(self, link):
        self.OLX_html = requests.get(link).content

    def transformuj_soup(self):
        self.OLX_soup = BeautifulSoup(self.OLX_html, "html.parser")

    def znajdz_mieszkania(self):
        self.mieszkania = self.OLX_soup.find_all('div', class_='offer-wrapper')

    def zbierz_dane_ze_strony(self):
        for mieszkanie in self.mieszkania:
            #  Cena wynajmu
            cena = mieszkanie.find('p', class_='price').getText().strip()

            # Nazwa ogłoszenia
            nazwa_ogloszenia = mieszkanie.find('a', class_='marginright5').find('strong').getText().strip()

            # Miejsce wynajmu
            miejsce = mieszkanie.find('td', class_='bottom-cell').find('p').getText().strip().split('\n')[0].split(', ')

            # Kiedy wystawiono
            czas = mieszkanie.find('td', class_='bottom-cell').find('p').getText().strip().split('\n')[3]

            mieszkanie = {'Nazwa': nazwa_ogloszenia, 'Cena': cena, 'Miejsce': miejsce, 'Czas': czas}
            self.mieszkania_czyste.append(mieszkanie)

    def rozpoznaj_liczbe_stron(self):
        ostatnia = self.OLX_soup.find_all('a', class_='block br3 brc8 large tdnone lheight24')
        for i in ostatnia:
            self.liczba_str = i.find('span').getText().strip()

    def zapisz_dane_json(self, nazwa_pliku):
        with open(nazwa_pliku, 'a', encoding="utf-8") as write_file:
            json.dump(self.mieszkania_czyste, write_file, indent=4, ensure_ascii=False)
