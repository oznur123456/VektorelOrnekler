# Bu örnekte çok biçimlilik kullanılmadı. Neden gerektiği anlatıldı.
class Ilan(): # Ilan sınıfı tanımlama / Ilan modeli oluşturma / !!! Ilan kalıbı tanımlama.
    def __init__(xx,num="--", bas="Tanımsız", tar="--",xxx = "Açıklama girilmedi"): # kurma/ouşturma/init/constract  
        xx.ilan_no = num
        xx.baslik = bas
        xx.tarihi = tar
        xx.aciklamasi = xxx
        # xx.depozito = depoz
       
    def bilgiver(self): # bilgiver metodu oluşturduk.    
        print(f"\n\nİlan bilgileri:\nİlan numarası:\t{self.ilan_no}\n\
İlan başlığı:\t{self.baslik}\nTarihi:\t\t{self.tarihi}\nAçıklaması:\t{self.aciklamasi}\n\
")

class EvIlani(Ilan): # ilan sınıfından miras yoluyla özellik vb. her şeyini aldık.
    def __init__(self, num="--", bas="Tanımsız", tar="--",xxx = "Açıklama girilmedi",buyukluk=50):
        super().__init__(num, bas, tar,xxx)
        self.buyuklugu = buyukluk

class KiralikEv(EvIlani):
    def __init__(self, num="--", bas="Tanımsız", tar="--",xxx = "Açıklama girilmedi", buyukluk=100, depozit=0):
        super().__init__(num, bas, tar,xxx, buyukluk)
        self.depozito = depozit
       
    def bilgiver(self): # bilgiver metodu oluşturduk.    
        print(f"\n\nİlan bilgileri:\nİlan numarası:\t{self.ilan_no}\n\
İlan başlığı:\t{self.baslik}\nTarihi:\t\t{self.tarihi}\nAçıklaması:\t{self.aciklamasi}\n\
Depozito:{self.depozito}")


ilan1 = Ilan(254158,"Acil satılık daire","22.08.25","3+1 metroya yakın...")
ilan2 = Ilan(587462,"Sahibinden kiralık daire","23.08.25","4+1 ana caddeye yakın...")
ilan3 = EvIlani(587462,"Sahibinden kiralık daire","23.08.25","4+1 ana caddeye yakın...",200)
ilan4 = KiralikEv(587462,"Sahibinden kiralık daire","23.08.25","4+1 ana caddeye yakın...",300,25000)


ilan1.bilgiver()
ilan2.bilgiver()
print(ilan3.buyuklugu)
print(ilan4.buyuklugu, ilan4.depozito)


print(ilan4.depozito) # yazılabilir
# print(ilan3.depozito) # yazılamaz
print(ilan3.buyuklugu) # yazılabilir
# print(ilan2.buyuklugu) # yazılamaz


# print(ilan3.)


class Arac(Ilan): # Sınıf adları büyük harfle ve tekil olur.
    def __init__(self,num, bas,tar,xxx,model,marka):
        super().__init__(num, bas,tar,xxx)
        self.modeli = model
        self.markasi = marka

arac1 = Arac(325474,"Acil satılık, öğretmenden","23.08.2025","Muayeni yeni, 220binde ...", "Egea cross", "Fiat")
arac1.bilgiver()  
print("Marka:\t\t:",arac1.markasi)
print("Model:\t\t:",arac1.modeli)

class Otomobil(Arac):
    def __init__(self,num, bas,tar,xxx,model,marka,kapisayisi):
        super().__init__(num, bas,tar,xxx,model,marka)
        self.kapis = kapisayisi
 
    def bilgiver(self): # bilgiver metodu oluşturduk.    
        print(f"\n\nİlan bilgileri:\nİlan numarası:\t{self.ilan_no}\n\
İlan başlığı:\t{self.baslik}\nTarihi:\t\t{self.tarihi}\nAçıklaması:\t{self.aciklamasi}\n\
Markası:\t{self.markasi}\nModeli:\t\t{self.modeli}\nKapı sayısı:\t{self.kapis}")
       
arac2 = Otomobil(8854795,"Acil satılık araç","23.08.2025","50binde, temiz, dosta gider ...", "Lİnea", "Fiat",5)

arac2.bilgiver()    
# print("Marka:\t\t:",arac2.markasi)
# print("Model:\t\t:",arac2.modeli)
# print("Kapı sayısı:\t:",arac2.kapis)
ilan1.bilgiver()
