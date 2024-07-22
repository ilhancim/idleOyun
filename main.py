def market(para, artis, fiyatArtis):
    while True:
        secim = int(input(f" 1-artis(+1) >{fiyatArtis} para<\n 2-***\n 3-Cik\n>-<\n "))
        print(">-<")
        if secim == 1:
            if para >= fiyatArtis:
                artis += 1
                para -= fiyatArtis
                fiyatArtis = int(fiyatArtis * 1.5)
                print(f"******\n1artis {artis} ye yukseldi!\n******")
                continue
            else:
                print("para yetersiz!")
                continue

        elif secim == 2:
            print("Yakinda!")
            continue

        elif secim == 3:
            print("Marketten cikiliyor...")

        else:
            print("Gecersiz secim!")

        return para, artis, fiyatArtis

def tikla(para, artis):
    para += artis
    return int(para)
def basla():
    para = 10
    artis = 1
    fiyatArtis = 10
    while True:
        print(f"para = {para}")
        secim = int(input(" 1-Tikla\n 2-Market\n>-<\n "))
        print(">-<")
        if secim==1:
            para = tikla(para, artis)

        elif secim==2:
            para, artis, fiyatArtis = market(para, artis, fiyatArtis)

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