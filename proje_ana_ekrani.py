def selamla(): print("Merhaba!")
def anamenu():
    print("\033[1;35;40m")
    print("╔═════════════════════╗")
    print("║\033[1;33;40m    VEKTOREL APP   \033[1;35;40m  ║")
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
    print("\033[0m")  
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
        proje_oyunlar_menusu.oyun_menu()
    
    elif secim == 3:
        print("Cizimleri seçtiniz.")
        import cizimler
        cizimler.cizim_menu()
    
    anamenu()

selamla()
anamenu()





