
class Cat:
    '''
    Ini adalah class untuk membuat object kucing
    '''
    spesies = "Kucing"

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe
    
    def run(self, speed):
        print(f"Kucing {self.nama} berlari dengan {speed}...")

kinako = Cat("Kinako", "Anggora")
print(f"Kinako adalah seekor {kinako.spesies} jenis {kinako.tipe}")

kinako.run('cepat')

minto = Cat(nama="Minto", tipe="Persia")
minto.run('hebat')