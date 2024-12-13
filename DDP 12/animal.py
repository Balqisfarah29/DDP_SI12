class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print("Nama \t\t\t\t\t: ", self.nama,
               "\nMakanan \t\t\t\t: ", self.makanan, 
               "\nHidup \t\t\t\t\t: ", self.hidup,
               "\nBerkembang biak \t\t\t: ", self.berkembang_biak,
               )

object = animal("buaya", "daging", "amphibi", "bertelur")
# object.cetak()

        