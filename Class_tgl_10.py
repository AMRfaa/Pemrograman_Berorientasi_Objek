class hewan_berkaki_empat:
    def __init__(self, nama, jenis):
        self.nama  = nama
        self.jenis = jenis

    def berlari (self):
        print (self.nama,"berlari")

    def berdiri (self):
        print (self.nama ,"berdiri")

print("-"*47)

class kucing (hewan_berkaki_empat):
    def __init__(self, nama, jenis, umur):
        super(). __init__(nama, jenis, ) # lempar ke class utama
        self.umur  = umur

    def umur_kucing (self):
        print(self.nama, "berumur", self.umur)

kucing_aku = kucing ("zoro","Savannah", 4)
kucing_aku.berlari ()
kucing_aku.berdiri ()

print("-"*47)

class anjing (hewan_berkaki_empat):
    def __init__(self, nama, jenis):
        super(). __init__(nama, jenis, ) # lempar ke class utama
     
    def melompat (self):
        print(self.nama,"melompat")

anjing_kmu = anjing ("zaki","ang ang ang")
anjing_kmu.berlari ()
anjing_kmu.berdiri ()
anjing_kmu.melompat ()

print("-"*47)
