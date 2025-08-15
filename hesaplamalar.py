def hesapmenu():
    print("1-Toplama")
    print("2-Çıkarma")
    s = input("Seçiminiz?")
    if s =="1": topla()
    if s =="2": cikar()

def topla():
    print("2+5=",2+5)

def cikar():
    print("5-3=",5-3)

hesapmenu()