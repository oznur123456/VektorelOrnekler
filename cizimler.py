def cizim_menu():
    print("╔═════════════════════╗")
    print("║     CIZIM MENU      ║")
    print("║                     ║")
    print("║  1-Kare             ║")
    print("║  2-Desen            ║")
    print("║  3-Ucgen            ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-Ana menüye dön   ║")
    print("║                     ║")
    print("║  Seçiminiz nedir?   ║")
    print("╚═════════════════════╝")

    s = int(input("Seçiminiz?"))
    if s== 1: kareciz()
    elif s== 3: ucgenciz()
    elif s == 6:
        import proje_ana_ekrani
    
def kareciz():
    import turtle
    for xx in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    cizim_menu()

def ucgenciz():
    import turtle
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
    cizim_menu()
       
cizim_menu()