from bs4 import BeautifulSoup
import urllib.request
import shutil
import requests
from urllib.parse import urljoin

# Ulohou je vytvorit downloader na obrazky

# Algoritmus:
#     Nacitam http/https adresu (command line, input)

def nacitaj_stranku(url):
    html = urllib.request.urlopen(url)
    return BeautifulSoup(html)

#     Otvorim http/https adresu (spravim get request na adresu)
def uloz_obrazok(url):
    soup = nacitaj_stranku(url)
    images = [img for img in soup.findAll('img')]
    data = [x.get('src') for x in images]
    for x in data:
        try:
            print(x)
            filename = x.split("/")[-1]
            if x.startswith("http"):
                pass
            else:
                x = x + url
            response = requests.get(x)
            with open(f"Pictures/{filename}", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print("Nazov obsahuje nevhodne znaky, preto ho nemozem ulozit")


#     Z response (response = requests.get(xy).text) vyhladam vsetky <img src>
#         a naplnim si ich do pola requests.get.text vrati string s obsahom
#         stranky
#     Po 1 pojdem stahovat obrazky a ukladat do adresara pictures
#         stiahnutie obrazka je jeho otvorenie a nasledne ulozenie do adresara
#         (alebo iny sposob, ktory najdete)

# Bonusove body:
# PRVE SA ZAMERAJTE NA FUNKCNOST KODU, POTOM NA BONUSY
#     PEP8 kompatibilny kod
#     Spravne pouzitie funkcii
#     Osetrenie chyb ..  napr:
#         zadam adresu v tvare abcd.xy (bez http/https)
#         zadam neexistujucu adresu (requests mi vrati 404 kod)
#         ....
#     Niektore stranky maju za adresou subor sitemap.xml kde je zoznam
#         vsetkych stranok na webe.. pouzite ho a stiahnite vsetky obrazky
#         zo vetkych podstranok
#     Unit testy
#         otestovanie funkcionality downloadera
#     Osetrenie toho, ak uz obrazok s takym menom existuje, aby nepadol program
#     Osetrenie vynimiek, zabranenie ich vzniku

if __name__ == "__main__":
    url = input("Zadaj url:")
    nacitaj_stranku(url)