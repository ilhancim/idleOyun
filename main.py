def market(para, artis, fiyat1, stok1):
    while True:
        print(f"para = {para}")
        if stok1 >= 2:
            secim = int(input(f" 1-artis(+1) >{fiyat1} para< ^{11-stok1}/10^\n 2-***\n 3-Cik\n>-<\n "))
            print(">-<")

        else:
            secim = int(input(f" 1-artis x{11 - stok1}/10x\n 2-***\n 3-Cik\n>-<\n "))
            print(">-<")

        if secim == 1:
            if para >= fiyat1 and stok1 >= 1:
                artis += 1
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
            print("Yakinda!")
            continue

        elif secim == 3:
            print("Marketten cikiliyor...")

        else:
            print("Gecersiz secim!")

        return para, artis, fiyat1, stok1

def tikla(para, artis):
    para += artis
    return int(para)

def basla():
    para = 0
    artis = 1
    fiyat1 = 10
    stok1 = 10
    while True:
        print(f"para = {para}")
        secim = int(input(" 1-Tikla\n 2-Market\n>-<\n "))
        print(">-<")
        if secim==1:
            para = tikla(para, artis)

        elif secim==2:
            para, artis, fiyat1, stok1 = market(para, artis, fiyat1, stok1)

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