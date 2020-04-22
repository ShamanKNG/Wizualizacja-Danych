class material:
    rodzaj=""
    dlugosc=1
    szerokosc=1
    
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print(f"rodzaj:{self.rodzaj}")
class ubrania(material):
    rozmiar=""
    kolor=""
    dla_kogo=""
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        print(f"Rozmiar:{self.rozmiar} kolor:{self.kolor} dla kogo:{self.dla_kogo}")
class swetry(ubrania):
    rodzaj_swetra=""
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self) :
        print(f"Rodzaj swetra: {self.rodzaj_swetra}")  
cos=material("kaszmir",5,5)
cos.wyswietl_nazwe()
koszulka=ubrania("m","niebieski","Grzegorz Brzęczyszczykiewicz")
koszulka.wyswietl_dane()
elegancki=swetry("rozpinany")
elegancki.wyswietl_dane()