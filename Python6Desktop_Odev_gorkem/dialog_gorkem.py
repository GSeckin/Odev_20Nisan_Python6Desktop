import sys
import os
from AnaDB_gorkem import Veritabani
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        ## veritabanı ve arayüz dosyaları çağırılıyor
        self.vt = Veritabani(os.getcwd()+r"\IEDB.db")
        self.pencere = uic.loadUi(os.getcwd()+r"\sozluk.ui")

        self.InitUI()
        self.TabloDoldur()

        self.pencere.btKaydet.clicked.connect(self.Kaydet)  
        self.pencere.lstSozluk.itemDoubleClicked.connect(self.secim)        

        self.pencere.actionKaydet.triggered.connect(self.Kaydet)
        self.pencere.btIptal.clicked.connect(self.pencere.close)
        self.pencere.show()

 
    def InitUI(self):
        # KayıtID 
        self.pencere.txtKayit.setText("")
        # TabloID 
        self.pencere.txtTablo.setText("")
        # SozlukID
        self.pencere.txtID.setText("")
        #SozlukAD
        self.pencere.txtAd.setText("")

    def TabloDoldur(self):
        self.pencere.lstSozluk.clear()
        self.liste = self.vt.SozlukListeleSozluk()
        self.pencere.lstSozluk.setHorizontalHeaderLabels(("ID","SOZLUK_ID","SOZLUK_ADI","TABLO_ID"))
        self.pencere.lstSozluk.setRowCount(15)
        self.pencere.lstSozluk.setColumnCount(4)
        satir = 0
        for a,b,c,d in self.liste:
            self.pencere.lstSozluk.setItem(satir,0,QTableWidgetItem(str(a)))
            self.pencere.lstSozluk.setItem(satir,1,QTableWidgetItem(str(b)))
            self.pencere.lstSozluk.setItem(satir,2,QTableWidgetItem(str(c)))
            self.pencere.lstSozluk.setItem(satir,3,QTableWidgetItem(str(d)))
            satir += 1

    def Mesaj(self,icon,baslik,metin):
        sonuc = True
        if icon == 1:
            QMessageBox.information(self,baslik,metin,QMessageBox.Ok)
        elif icon == 2:
            QMessageBox.critical(self,baslik,metin,QMessageBox.Ok)
        elif icon == 3:
            QMessageBox.warning(self,baslik,metin,QMessageBox.Ok)
        elif icon == 4:
            try:
                cevap =  QMessageBox.question(self,baslik,metin,QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Cancel)
                if cevap == QMessageBox.Ok:
                    sonuc = True
                else:
                    sonuc = False
            except:
                print("Hata")
        return sonuc

    def Kaydet(self):
        ID = self.pencere.txtKayit.text()
        tablo_id = self.pencere.txtTablo.text()
        sozluk_id = self.pencere.txtID.text()
        sozluk_adi =  self.pencere.txtAd.text()
        if ID == "":
            sonuc = self.vt.VeriEkleSozluk(tablo_id,sozluk_id,sozluk_adi)
        else:
            sonuc = self.vt.VeriGuncelleSozluk(tablo_id,sozluk_id,sozluk_adi,ID)
        
        if sonuc == "1":
            self.Mesaj(1,"Bilgi","Başarıyla Kaydedildi")
            self.InitUI()
            self.TabloDoldur()
        else:
            self.Mesaj(2,"Kayıt Hatası",sonuc)

    def secim(self):
        # print(self.liste[self.win.lstHarcama.currentRow()])
        ID = str(self.liste[self.pencere.lstSozluk.currentRow()][0])
        tablo_id = str(self.liste[self.pencere.lstSozluk.currentRow()][3])
        sozluk_id = str(self.liste[self.pencere.lstSozluk.currentRow()][1])
        sozluk_adi = str(self.liste[self.pencere.lstSozluk.currentRow()][2])
        self.pencere.txtKayit.setText(ID)
        self.pencere.txtTablo.setText(tablo_id)
        self.pencere.txtID.setText(sozluk_id)
        self.pencere.txtAd.setText(sozluk_adi)
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())