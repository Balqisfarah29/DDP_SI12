from animal import *

class Burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.warna_bulu = warna_bulu
    def cetak_burung(self):
        super().cetak()
        print("warna bulu \t\t\t\t: ", self.warna_bulu)
        
Cendrawasih = Burung("Cendrawasih", "Biji-bijian, serangga, ulat", "Papua dan Maluku", "Bertelur", "Kuning dan Coklat")
Cendrawasih.cetak_burung()
