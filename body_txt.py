def body_txt(a, b, c, delta, raiz, division, x1, x2):
    archive = open("Passo a passo.txt", "a", encoding="UTF-8")
    archive.write("                DELTA:")
    archive.write("\n")
    archive.write("\n")
    archive.write(f"Delta = {b}² - (4 x {a} x {c}) ")
    archive.write("\n")
    archive.write(f"Delta = {delta}")
    if delta >= 0:
    
        archive.write("\n")
        archive.write("\n")
        archive.write("                CALCULAR X:")
        archive.write("\n")
        archive.write("\n")
        archive.write(f"X1 = -({b})² + raiz({delta}) dividido({division})")
        archive.write("\n")
        archive.write(f"X1 = {b ** 2} + {raiz} dividido({division})")
        archive.write("\n")
        archive.write(f"X1 = {x1}")
        archive.write("\n")
        archive.write("\n")
        archive.write(f"X2 = -({b})² - raiz({delta}) dividido({division})")
        archive.write("\n")
        archive.write(f"X2 = {b ** 2} - {raiz}")
        archive.write("\n")
        archive.write(f"X2 = {x2}")
    else:
        pass

