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
    if s== 3: ucgenciz()
    
def kareciz():
    import turtle
    for xx in range(4):
        turtle.forward(100)
        turtle.right(90)
        kareciz()

def ucgenciz():
    import turtle
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
        ucgenciz()

cizim_menu()