#magic keyword

print("Berikut data mahasiswa")

class datasiswa : 
    def __init__(self, name, fakultas, prodi) :
        self.name = name
        self.fakultas = fakultas
        self.prodi = prodi

object1 = datasiswa("Arasya", "Ekonomi Bisnis", "Manajemen")
object2 = datasiswa("akbar", "Hukum", "Hukum perdata")
object3 = datasiswa("Dyesica", "Kedokteran", "Dokter gigi")

print(object1.name)
print(object2.prodi)
print(object3.fakultas)
        