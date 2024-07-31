def market(para, artis, carpan, fiyat1, fiyat2, stok1, stok2):
    while True:
        print(f"para = {para}")
        if stok1 >= 2:
            print(f" 1-artis(+1) >{fiyat1} para< ^{11-stok1}/10^")

        else:
            print(f" 1-artis x{11 - stok1}/10x")

        if stok2 >= 2:
            print(f" 2-carpan(+0.1) >{fiyat2} para< ^{11-stok2}/10^")

        else:
            print(f" 2-carpan x{11 - stok2}/10x")

        secim = int(input(" 3-Cik\n>-<\n "))
        print(">-<")

        if secim == 1:
            if para >= fiyat1 and stok1 >= 1:
                artis += 10
                stok1 -= 1
                para -= fiyat1
                fiyat1 = int(fiyat1 * 1.5)

                print(f"******\nartis {artis} ye yukseldi!\n******")
                continue

            elif stok1 == 1:
                print("******\nBu esyanin stogu bitti!\n******")
                continue

            else:
                print("******\nPara yetersiz!\n******")
                continue

        elif secim == 2:
            if para >= fiyat2 and stok2 >= 1:
                carpan += 0.1
                stok2 -= 1
                para -= fiyat2
                fiyat2 = int(fiyat2 * 2)

                print(f"******\ncarpan {carpan} ye yukseldi!\n******")
                continue

            elif stok1 == 1:
                print("******\nBu esyanin stogu bitti!\n******")
                continue

            else:
                print("******\nPara yetersiz!\n******")
                continue

        elif secim == 3:
            print("Marketten cikiliyor...")

        else:
            print("Gecersiz secim!")

        return para, artis, carpan, fiyat1, fiyat2, stok1, stok2

def tikla(para, artis, carpan):
    para += artis*carpan
    return int(para)

def basla():
    para = 0
    artis = 10
    carpan = 1
    fiyat1 = 100
    fiyat2 = 200
    stok1 = 10
    stok2 = 10
    while True:
        print(f"para = {para}")
        secim = int(input(" 1-Tikla\n 2-Market\n>-<\n "))
        print(">-<")
        if secim==1:
            para = tikla(para, artis, carpan)

        elif secim==2:
            para, artis, carpan, fiyat1, fiyat2, stok1, stok2 = market(para, artis, carpan, fiyat1, fiyat2, stok1, stok2)

        else:
            print("Gecersiz secim.")

def nasilOynanir():
    print("Yakinda!")

def menu():
    print("oyun.")
    secim = int(input(" 1-Basla\n 2-Nasıl Oynanir\n 3-Cik\n>-<\n "))
    print(">-<")
    while True:
        if secim == 1:
            basla()
            break

        elif secim == 2:
            nasilOynanir()
            break

        elif secim == 3:
            print("Cikis yapiliyor...")
            break

        else:
            secim = int(input("Gecerli bir numara seciniz\n>-<\n "))
            print(">-<")

def main():
    menu()

if __name__ == "__main__":
    main()