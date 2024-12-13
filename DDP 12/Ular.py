from animal import *

class Ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("berbisa \t\t\t\t: ", self.berbisa,
              "\nracun \t\t\t\t\t: ", self.racun)
        
Anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Tidak berbisa", "Tidak berracun")
Anaconda.cetak_ular()
