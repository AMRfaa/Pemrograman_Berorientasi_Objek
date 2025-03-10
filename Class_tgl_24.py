class cat:
    def __init__ (self, nama, umur, ras):
        self.nama = nama
        self.umur = umur
        self.ras = ras

    def melompat (self):
        print (f"{self.ras} sekarang sedang melompat")

    def tidur (self):
        print (f"{self.ras} sekarang sedang tidur")

kucing_saya = cat ("Levi",22,"Savannah")
kucing_dia = cat ("Louren" ,17,"Ashera")

print("------------------------------")

print (f"Kucing saya bernama {kucing_saya.nama}")
print (f"Kucing saya berumur {kucing_saya.umur} tahun")
print (f"Kucing saya merupakan ras {kucing_saya.ras}")

print("------------------------------")

print (f"Kucing dia bernama {kucing_dia.nama}")
print (f"Kucing dia berumur {kucing_dia.umur} tahun")
print (f"Kucing dia merupakan ras {kucing_dia.ras}")

print("------------------------------")

kucing_saya.melompat ()
kucing_dia.tidur ()

print("------------------------------")

