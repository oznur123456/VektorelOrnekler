
fhs = 4 # Faktöriyeli Hes.Say.
sonuc = 1
def faktoriyel(xx):
    global sonuc
   
    sonuc *= xx
    print("Sayi:",xx)
   
    xx -= 1
    if xx > 1: faktoriyel(xx)

faktoriyel(fhs)
print(f"{fhs} faktöriyeli: ",sonuc)

