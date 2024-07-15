# Engeto - PA - 3. projekt - Elections Scraper

Třetí projekt na Python Akademii od Engeta.

## Popis projektu

Tento projekt slouží k extrahování výsledků parlamentních voleb z roku 2017.
Příklad odkazu k nahlédnutí
najdete <a href="https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103">
zde</a>.

## Instalace knihoven

Knihovny, které jsou použity v kódu, jsou uloženy v souboru ```requirements.txt```. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
$ pip3 --version                    # overim verzi manazeru
$ pip3 install -r requirements.txt  # nainstalujeme knihovny
```

## Spuštění projektu

Spuštění souboru ```Elections_Scraper.py``` v rámci příkazového řádku požaduje dva povinné argumenty.
```
python Elections_Scraper.py 'odkaz-uzemniho-celku' 'nazev-vysledneho-souboru'
```
Následně se Vám stáhnou výsledky jako soubor s příponou ```.csv```.

## Ukázka projektu

Výsledky hlasování pro okres Prostějov:
1. argument: ```https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103```
2. argument: ```vysledky_prostejov.csv```

Spuštění programu:
```
python Elections_Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_prostejov.csv'
```

Průběh stahování:
```
STAHUJI DATA Z VYBRANÉ URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 
UKLÁDÁM DO SOUBORU: vysledky_prostejov.csv
UKONČUJI Elections_Scraper
```

Částečný výstup:
```
code,location,registered,envelopes,valid,...
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
...
```
