def selamla(): print("Merhaba!")
def anamenu():
    print("╔═════════════════════╗")
    print("║    VEKTOREL APP     ║")
    print("║                     ║")
    print("║  1-Hesaplamalar     ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Çizimler         ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10-                 ║")
    print("║                     ║")
    print("║   Seçiminiz nedir?  ║")
    print("╚═════════════════════╝")
    secim = int(input())
    print("Seçiminiz:",secim,"idi.")

    if secim < 1 or secim > 10:
        print("Secim yanlis. 1-10 arasi bir deger giriniz.")
        anamenu()

    elif secim == 1:
        print("Hesaplamalari seçtiniz.")
        import hesaplamalar
        hesaplamalar.hesapmenu()
        
    elif secim == 2: 
        print("Oyunlar seçtiniz.")
        import proje_oyunlar_menusu
    
    elif secim == 3:
        print("Cizimleri seçtiniz.")
        import cizimler
        cizimler.cizim_menu()
    
    anamenu()

selamla()
anamenu()





