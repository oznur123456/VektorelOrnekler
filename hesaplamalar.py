def hesapmenu():

    print("╔═════════════════════╗")
    print("║    HESAPLAMALAR     ║")
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

    s = int(input("Seçiminiz?"))
    if s == 1: topla()
    if s == 2: cikar()
    if s == 10:
        import proje_ana_ekrani

def topla():
    print("2+5=",2+5)

def cikar():
    print("5-3=",5-3)

hesapmenu()


