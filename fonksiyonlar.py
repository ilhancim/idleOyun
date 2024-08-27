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
                para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2 = oyuncu.split("/")[1].split()
                girisDurum = 1
                return girisDurum, kullaniciAdi, sifre, int(para), int(rebirth), int(prestige), int(artis), float(carpan1), int(carpan2), int(fiyat1), int(fiyat2), int(fiyat3), int(stok1), int(stok2)
                break

    return girisDurum, None, None, None, None, None, None, None, None, None, None, None, None, None

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

    yaz.write(f"{kullaniciAdi} {sifre}/0 0 0 10 1 1 100 5000 50000 10 25\n")
    yaz.close()

    return kayitDurum

def oyuncuGuncelle(kullaniciAdi, sifre, para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2):
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
            ekle.write(oyuncu)

    ekle.write(f"{kullaniciAdi} {sifre}/{para} {rebirth} {prestige} {artis} {carpan1} {carpan2} {fiyat1} {fiyat2} {fiyat3} {stok1} {stok2}\n")
    ekle.close()

def guc(para, artis, fiyat1, stok1):
    if para >= fiyat1 and stok1 > 0:
        artis += 10
        stok1 -= 1
        para -= fiyat1
        fiyat1 = int(fiyat1 * 1.5)

        text = f"artis {artis} ye yukseldi!"

    elif stok1 == 0:
        text = "Bu esyanin stogu bitti!"

    else:
        text = "Para yetersiz!"

    return text, para, artis, fiyat1, stok1

def rebirth(para, rebirth, artis, carpan1, fiyat1, fiyat2, stok1, stok2):
    if para >= fiyat2 and stok2 > 0 and stok1 == 0:
        para = 0
        rebirth += 1
        artis = 10
        carpan1 += 0.1
        carpan1 = float(f"{carpan1:.1f}")
        fiyat1 = 100
        fiyat2 *= 2
        stok1 = 10
        stok2 -= 1

        text = f"Rebirth {rebirth} ye yukseldi!"

    elif stok1 > 0:
        text = "Güc fullenmeden Rebirth satın alamazsın!"

    elif para < fiyat2:
        text = "Para yetersiz!"

    elif stok2 == 0:
        text = "Daha fazla Rebirth satın alamazsın! Prestige satın al!"

    return text, para, rebirth, artis, carpan1, fiyat1, fiyat2, stok1, stok2

def prestige(para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2):
    if para >= fiyat3 and stok2 == 0 and stok1 == 0 :
        para = 0
        rebirth = 0
        prestige += 1
        artis = 10
        carpan1 = 1
        carpan2 *= 2
        fiyat1 = 100
        fiyat2 = 5000
        fiyat3 = int(fiyat3 * 5)
        stok1 = 10
        stok2 = 25

        text = f"Prestige {prestige} ye yukseldi!"

    elif stok2 > 1:
        text = "Rebirth fullenmeden Prestige satın alamazsın!"

    elif para < fiyat3:
        text = "Para yetersiz!"

    return text, para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2

def tikla(para, artis, carpan1, carpan2):
    para += artis*carpan1*carpan2
    return int(para)