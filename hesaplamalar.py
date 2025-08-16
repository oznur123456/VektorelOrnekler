def hesapmenu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m     HESAP MAK     \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Cikarma          ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10- Ana menuye don  ║")
    print("║                     ║")
    print("║   Seçiminiz nedir?  ║")
    print("╚═════════════════════╝")
    print("\033[0m")  

    s = int(input("Seçiminiz?"))
    if s == 1: topla()
    elif s == 2: cikar()
    elif s == 10:
        import proje_ana_ekrani

def topla():
    print("2+5=",2+5)
    hesapmenu()

def cikar():
    print("5-3=",5-3)
    hesapmenu()

hesapmenu()


