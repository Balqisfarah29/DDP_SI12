from person import *

class Mahasiswa(Person):
    prodi = ""
    semester = 0
    
    def __init__(self, nama, gender, umur, prodi, semester):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester

    def cetak(self):
        super().cetak()
        print("Prodi \t\t:", self.prodi,
              "\nSemester \t:", self.semester,
              "\n-------------------------------")