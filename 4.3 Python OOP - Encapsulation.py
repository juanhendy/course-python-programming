
class Mobil:
    def __init__(self, plat):
        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = 40 # liter

    def lihatMaksimumBensin(self):
        print(f"Maksimum Bensin yaitu: {self.__bensin} liter")
    
    def aturMaksimalBensin(self, bensin):
        self.__bensin = bensin

avanza = Mobil(plat="A 0394 S")
avanza.__bensin = 90
print(avanza.__bensin)
avanza.lihatMaksimumBensin()
avanza.aturMaksimalBensin(90)
avanza.lihatMaksimumBensin()