def giris(kullaniciAdi, sifre):
    oku = open("Oyuncular.txt", "r")
    oyuncular = []
    for oyuncu in oku:
        oyuncular.append(oyuncu)
    oku.close()
    girisDurum = 0
    for oyuncu in oyuncular:
        if kullaniciAdi == oyuncu.split("/")[0].split()[0]:
            if sifre == oyuncu.split("/")[0].split()[1]:
                para, artis, carpan, fiyat1, fiyat2, stok1, stok2 = oyuncu.split("/")[1].split()
                girisDurum = 1
                return girisDurum, kullaniciAdi, sifre, int(para), int(artis), float(carpan), int(fiyat1), int(fiyat2), int(stok1), int(stok2)
                break

    return girisDurum, None, None, None, None, None, None, None, None, None
def kayit(kullaniciAdi, sifre):
    oku = open("Oyuncular.txt", "r")
    yaz = open("Oyuncular.txt", "a")
    oyuncular = []
    for oyuncu in oku:
        oyuncular.append(oyuncu)
    oku.close()
    kayitDurum = 1

    for oyuncu in oyuncular:
        if kullaniciAdi == oyuncu.split("/")[0].split()[0]:
            kayitDurum = 0
            return kayitDurum

    yaz.write(f"{kullaniciAdi} {sifre}/0 10 1 100 200 10 10\n")
    yaz.close()

    return kayitDurum

def oyuncuGuncelle(kullaniciAdi, sifre, para, artis, carpan, fiyat1, fiyat2, stok1, stok2):
    oku = open("Oyuncular.txt","r")
    oyuncular = []
    for oyuncu in oku:
        oyuncular.append(oyuncu)
    oku.close()

    yaz = open("Oyuncular.txt", "w")
    yaz.write("")
    yaz.close()

    ekle = open("Oyuncular.txt", "a")
    for oyuncu in oyuncular:
        if kullaniciAdi != oyuncu.split("/")[0].split()[0]:
            ekle.write(oyuncu + "\n")

    ekle.write(f"{kullaniciAdi} {sifre}/{para} {artis} {carpan} {fiyat1} {fiyat2} {stok1} {stok2}\n")
    ekle.close()

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
                carpan == float(f"{carpan:.1f}")
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

def basla(kullaniciAdi, sifre, para, artis, carpan, fiyat1, fiyat2, stok1, stok2):
    while True:
        print(f"para = {para}              /{kullaniciAdi}")
        secim = int(input(" 1-Tikla\n 2-Market\n 3-Cikis\n>-<\n "))
        print(">-<")
        oyuncuGuncelle(kullaniciAdi, sifre, para, artis, carpan, fiyat1, fiyat2, stok1, stok2)
        if secim==1:
            para = tikla(para, artis, carpan)

        elif secim==2:
            para, artis, carpan, fiyat1, fiyat2, stok1, stok2 = market(para, artis, carpan, fiyat1, fiyat2, stok1, stok2)

        elif secim==3:
            print("Hesaptan cikiliyor...")
            break
        else:
            print("Gecersiz secim.")
