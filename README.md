# Scrapping apartment rental offers data

## Description

Program downloads the data from portal called OLX, which is a polish website with apartment rental offers. User needs to provide the name of the city (from a list of Warszawa, Poznań, Katowice, Wrocław and Gdańsk) along with a number of pages to scrap.

Scrapped data includes:
- name of the offer
- price
- place
- date

Data is saved to a default location in a JSON format.

Example of the document:
```json
    {
        "Nazwa": "wynajme mieszkanie - 2 pokojowe 30 m",
        "Cena": "1 800 zł",
        "Miejsce": [
            "Warszawa",
            "Wola"
        ],
        "Czas": "24  lip"
    },
    {
        "Nazwa": "Mieszkanie 2 pokoje Skorosze / Wlochy - nowe.",
        "Cena": "2 200 zł",
        "Miejsce": [
            "Warszawa",
            "Włochy"
        ],
        "Czas": "24  lip"
    }
```

Project was a part of Python learning process with an emphesis on web scrapping and CLI building.

## Tools and libraries used

Language:
- Python 3

Libraries:
- requests
- json
- BeautifulSoup4
- argparse

## Structure of the program

Program is divided into two parts, one is the Parser (OLXParser.py) to scrap the data from the page. Second is the main one to run moduls from the parser and to provide CLI with use of argparse library.

## License
MIT License

Copyright (c) 2021 Mateusz Broja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
