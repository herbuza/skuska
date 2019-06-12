# v requirements.txt mas chybu   beautyfulsoup4 -> beautifulsoup4 tj.. nejde nainstalovat z toho prerequizita
# spustitelny subor sa mal volat   pic-download.py
from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
# importy sa podla PEP8 davaju v poradi:
# klasicky import
# ostatne
# eg.
# import urllib.request
# import shutil
# from bs4 import BeautifulSoup
# po importoch idu 2x medzera..
# nepouzity import, treba dat prec
from urllib.parse import urljoin

# Ulohou je vytvorit downloader na obrazky

# Algoritmus:
#     Nacitam http/https adresu (command line, input)

# idealne je, ak su nazvy funkci/premennych anglicky ale nieje to nejaka velka vec
def nacitaj_stranku(url):
    html = urllib.request.urlopen(url)
    return BeautifulSoup(html)

#     Otvorim http/https adresu (spravim get request na adresu)
# 2 medzery medzi funkciami  (PEP8)
def uloz_obrazok(url):
    soup = nacitaj_stranku(url)
    # tieto 2 polia by sa dali spojit do 1 a prechadzat vsetko naraz a robit, ale nieje to problem
    images = [img for img in soup.findAll('img')]
    # teoreticky vies spravit aj
    # images = [img.get('src') for img in soup.findAll('img')
    # a dostanes rovno source obrazkov do pola
    data = [x.get('src') for x in images]
    # x/a/b/c nevhodne zvolene nazvy premennych, treba aby boli zrejme zo zaciatku
    for x in data:
        try:
            # zbytocny print
            print(x)
            filename = x.split("/")[-1]
            # ak je jediny statement za ifom pass... ten if sa nedava, je to zbytocne zvysenie komplexity
            # tj... tvoj if by sa mal prerobit na:
            # if not x.startswith("http"):
            #     x = x + url
            if x.startswith("http"):
                pass
            else:
                # toto mas otocene
                # x = /images/ajtyvit_1-300x158.jpg
                # url = https://www.ajtyvit.sk
                # x = x + url ->  /images/ajtyvit_1-300x158.jpghttps://www.ajtyvit.sk
                # malo by samozrejme byt -> https://www.ajtyvit.sk/images/ajtyvit_1-300x158.jpg
                # tj  x = url + x
                x = x + url
            response = requests.get(x)
            # v repository si neulozila adresar Pictures... tj ak neexistuje, vsetko padne na exception
            # a nic sa nevykona (este aj tym, ze ju chytas takto)
            # cize, idealne je skontrolvat, ci ten adresar exsituje a ak nie, tak ho vytvorit, to je bulletproof alebo
            # aspon ten adresar dodat spolu so zdrojakom
            with open(f"Pictures/{filename}", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
        # do exceptu treba dat aj co ma chytit, inak zachyti vsetky chyby
        # a neprides na to co sa stalo
        # tj.. except OSError:  napr
        except:
            # tu by som si vyprintoval aj to, ze ktore su tie znaky, ktore url, v tvojom pripade x
            # sposobilo tu chybu, aby si vedela pracovat s tym s cim treba
            print("Nazov obsahuje nevhodne znaky, preto ho nemozem ulozit")


if __name__ == "__main__":
    url = input("Zadaj url:")
    # asi urcite volas zlu funkciu... chces volat uloz_obrazok(url) a nie nacitaj_stranku(url)
    nacitaj_stranku(url)
    # celkovo by som to zhodnotil takto
    # za idealnych podmienok to cele funguje, ak sa co i len 1 z nich zmeni... mame problem
    # su to skor chyby z nepozornosti (napr  x = x + url  namiesto  x = url + x)
    # kazdopadne treba tie veci fixnut, urcite sa na to nevykaslat
