class kucing ():
    def bersuara (self):
        print("mengeong")
        
class anjing ():
    def bersuara (self):
        print("menggonggong")

kucing = kucing()
kucing.bersuara()

anjing = anjing()
anjing.bersuara()
      
      class persegi():
          def luas(self,sisi):
              return sisi*sisi
          
      class persegi_panjang():
          def luas(self,panjang,lebar):
              return panjang * lebar
              
      persegi_a = persegi()
      persegi_panjang_a = persegi_panjang()
      
      print(persegi_panjang_a.luas(4,6))
      print(persegi_a.luas(6))
