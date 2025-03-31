
class Cat:
    def __init__(self):
        self.nama = "Meong"
        self.tipe = "Anggora"
    def forward(self):
        print("Kucing berlari...")
    def walk(self):
        print("Kucing berjalan...")

class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"
    def forward(self):
        print("Burung terbang...")
    def walk(self):
        print("Burung berjalan...")

def melaju(objek):
    objek.forward()
def maju(objek):
    objek.walk()

meong = Cat(); erago = Bird()
melaju(meong)
melaju(erago)
maju(erago)
maju(meong)