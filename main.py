from PyQt5.QtWidgets import *
import fonksiyonlar
import panel
import panel1
import panel2
import panel3
import panel4

class p(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p = panel.Ui_MainWindow()
        self.p.setupUi(self)
        self.p1 = p1()
        self.p2 = p2()
        self.p3 = p3()
        self.p4 = p4()
        self.p1.set_p3(self.p3)
        self.p4.set_p3(self.p3)
        self.p.pushButton.clicked.connect(self.buton)
        self.p.pushButton_2.clicked.connect(self.buton2)
        self.p.pushButton_3.clicked.connect(self.buton3)

    def buton(self):
        self.close()
        self.p1.show()

    def buton2(self):
        self.close()
        self.p2.show()

    def buton3(self):
        self.close()

class p1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p1 = panel1.Ui_MainWindow()
        self.p1.setupUi(self)
        self.p3 = None
        self.p1.pushButton.clicked.connect(self.buton)
        self.p1.pushButton_2.clicked.connect(self.anaEkran)
        self.deneme = 1

    def set_p3(self, p3_instance):
        self.p3 = p3_instance

    def buton(self):
        self.kullaniciAdi = self.p1.lineEdit.text()
        self.sifre = self.p1.lineEdit_2.text()
        (girisDurum, self.kullaniciAdi, self.sifre, self.para, self.rebirth, self.prestige, self.artis, self.carpan1,
         self.carpan2, self.fiyat1, self.fiyat2, self.fiyat3, self.stok1, self.stok2) = fonksiyonlar.giris(self.kullaniciAdi, self.sifre)

        if girisDurum == 0:
            self.p1.label_3.setText(f"Kullanici adi ve/veya sifre yanlis. <{self.deneme}. deneme>")
            self.deneme += 1

        else:
            if self.p3:
                self.p3.setData(self.kullaniciAdi, self.sifre, self.para, self.rebirth, self.prestige, self.artis,
                            self.carpan1, self.carpan2, self.fiyat1, self.fiyat2, self.fiyat3, self.stok1, self.stok2)
            self.close()
            self.p3.show()

    def anaEkran(self):
        self.close()
        self.p = p()
        self.p.show()

class p2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p2 = panel2.Ui_MainWindow()
        self.p2.setupUi(self)
        self.p2.pushButton.clicked.connect(self.buton)
        self.p2.pushButton_2.clicked.connect(self.anaEkran)
        self.deneme = 1

    def buton(self):
        self.kullaniciAdi = self.p2.lineEdit.text()
        self.sifre = self.p2.lineEdit_2.text()
        kayitDurum = fonksiyonlar.kayit(self.kullaniciAdi, self.sifre)
        if kayitDurum == 0:
            self.p2.label_3.setText(f"Kullanıcı adı bulunuyor lütfen başka bir kullanıcı adı seçiniz. <{self.deneme}. deneme>")
            self.deneme += 1

        else:
            self.p2.label_3.setText("Kayıt başarılı!")

    def anaEkran(self):
        self.close()
        self.p = p()
        self.p.show()

class p3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p3 = panel3.Ui_MainWindow()
        self.p3.setupUi(self)
        self.p3.pushButton.clicked.connect(self.tikla)
        self.p3.pushButton_2.clicked.connect(self.market)
        self.p3.pushButton_3.clicked.connect(self.anaEkran)

    def setData(self, kullaniciAdi, sifre, para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2):
        self.kullaniciAdi = kullaniciAdi
        self.sifre = sifre
        self.para = para
        self.rebirth = rebirth
        self.prestige = prestige
        self.artis = artis
        self.carpan1 = carpan1
        self.carpan2 = carpan2
        self.fiyat1 = fiyat1
        self.fiyat2 = fiyat2
        self.fiyat3 = fiyat3
        self.stok1 = stok1
        self.stok2 = stok2

        self.p3.label.setText(f"Para = {self.para}")
        self.p3.label_2.setText(f"/{self.kullaniciAdi}")
        self.p3.label_3.setText(f"Rebirth = {self.rebirth}")
        self.p3.label_4.setText(f"Prestige = {self.prestige}")
        self.p3.label_5.setText(f"{self.carpan1*self.carpan2}x Carpan")

    def tikla(self):
        self.para = fonksiyonlar.tikla(self.para, self.artis, self.carpan1, self.carpan2)
        self.p3.label.setText(f"Para = {self.para}")

    def market(self):
        self.p4 = p4()
        self.p4.setData(self.kullaniciAdi, self.sifre, self.para, self.rebirth, self.prestige, self.artis,
                        self.carpan1, self.carpan2, self.fiyat1, self.fiyat2, self.fiyat3, self.stok1, self.stok2)
        self.p4.set_p3(self)
        self.close()
        self.p4.show()

    def anaEkran(self):
        self.close()
        self.p = p()
        self.p.show()

class p4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.p4 = panel4.Ui_MainWindow()
        self.p4.setupUi(self)
        self.p3 = None
        self.p4.pushButton.clicked.connect(self.buton)
        self.p4.pushButton_2.clicked.connect(self.buton2)
        self.p4.pushButton_3.clicked.connect(self.buton3)
        self.p4.pushButton_4.clicked.connect(self.geri)

    def set_p3(self, p3_instance):
        self.p3 = p3_instance

    def setData(self, kullaniciAdi, sifre, para, rebirth, prestige, artis, carpan1, carpan2, fiyat1, fiyat2, fiyat3, stok1, stok2):
        self.kullaniciAdi = kullaniciAdi
        self.sifre = sifre
        self.para = para
        self.rebirth = rebirth
        self.prestige = prestige
        self.artis = artis
        self.carpan1 = carpan1
        self.carpan2 = carpan2
        self.fiyat1 = fiyat1
        self.fiyat2 = fiyat2
        self.fiyat3 = fiyat3
        self.stok1 = stok1
        self.stok2 = stok2

        self.p4.label.setText(f"Para = {self.para}")
        self.p4.label_2.setText(f"/{kullaniciAdi}")

    def buton(self):
        self.close()
        self.p = p()
        self.p.show()

    def buton2(self):
        self.close()
        self.p = p()
        self.p.show()

    def buton3(self):
        self.close()
        self.p = p()
        self.p.show()

    def geri(self):
        if self.p3:
            self.p3.setData(self.kullaniciAdi, self.sifre, self.para, self.rebirth, self.prestige, self.artis,
                            self.carpan1, self.carpan2, self.fiyat1, self.fiyat2, self.fiyat3, self.stok1, self.stok2)
        fonksiyonlar.oyuncuGuncelle(self.kullaniciAdi, self.sifre, self.para, self.rebirth, self.prestige, self.artis,
                            self.carpan1, self.carpan2, self.fiyat1, self.fiyat2, self.fiyat3, self.stok1, self.stok2)
        self.close()
        self.p3.show()


app = QApplication([])
pencere = p()
pencere.show()
app.exec_()