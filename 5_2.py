class Ogrenci():
    ad = "Tanımsız"
    nu = 0
    tc = "--"
    dn = 0
    def __init__(xx):
        pass

    def adekle(aa, adi):
        aa.ad = adi
    def cezaver(cc,miktar):
        cc.dn += miktar
    
ogr1 = Ogrenci()
ogr2 = Ogrenci()
ogr3 = Ogrenci()

print(ogr1)
print(ogr1.ad)
ogr1.ad="Rüzgar"
ogr2.ad="Uğur"
print(ogr1.ad, ogr1.dn)
print(ogr2.ad, ogr2.dn)
print(ogr3.ad, ogr3.dn)
ogr2.cezaver(30)
ogr2.cezaver(20)
print(ogr2.ad, ogr2.dn)
