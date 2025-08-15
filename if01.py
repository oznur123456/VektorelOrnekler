def menu():
    print("1-Oyun")
    print("2-Çizim")
    secim = input("Seçiminiz:")
    if secim == "1":oyunmenu() 
    if secim == "2":
        print("Güzel çizimler")
        cizimmenu()
    if int(secim) < 1 or int(secim)>2:
        print("Yanlış seçim")
    menu()
def oyunmenu():
    print("1-Yılan")
    print("2-Tetris")
    secim = input("Seçiminiz:")
    if secim == "1":print("Yılan oyunu kodlar") 
    if secim == "2":
        print("Tetris oyununa geçildi")
        # cizimmenu()
def cizimmenu():
    print("Kare")
    print("Üçgen")
print("Vektorel App")
# oyunmenu()
menu()