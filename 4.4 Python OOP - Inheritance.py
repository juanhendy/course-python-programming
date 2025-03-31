
class Animal:
    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = "lambat"
    def grow(self):
        print("Mamalia ini bertumbuh...")

class Cat(Animal):
    def __init__(self, nama, tipe):
        super().__init__()
        self.nama = nama
        self.tipe = tipe
    def run(self):
        print(f"Kucing {self.tipe} ini berlari")
kinako = Cat("Kinako", "Oren")

kinako.run()
kinako.grow()