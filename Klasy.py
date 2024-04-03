class Pojazd:
    def __init__(self, kolor, liczbaKol, marka):
        self.kolor = kolor
        self.liczbaKol = liczbaKol
        self.marka = marka
        self.__czyJedzie = False
    def czyJedzie(self):
        return str(self.__czyJedzie)
    def jedz(self):
        self.__czyJedzie = True
    def zatrzymaj(self):
        self.__czyJedzie = False