from Klasy import Pojazd
pojazd1 = Pojazd("Czerwony", 4, "Toyota")#Utworzenie nowego obiektu
print(pojazd1.czyJedzie())#Zwroci status TRue/False i wypisze w print
pojazd1.jedz()#Zmieni status pola czyJedzie na True
print(pojazd1.czyJedzie())
