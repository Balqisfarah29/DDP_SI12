from animal import *

class Penguin(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, karakteristik):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.karakteristik = karakteristik
    def cetak_penguin(self):
        super().cetak()
        print("karakterintik \t\t\t\t: ", self.karakteristik)
        
Penguin = Penguin("Penguin", "Ikan, krill, dan cumi-cumi", "AmazKutub Selatan", "Bertelur", "Termasuk jenis burung yang tidak bisa terbang")
Penguin.cetak_penguin()