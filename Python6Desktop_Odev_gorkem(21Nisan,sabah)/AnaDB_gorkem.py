import sqlite3 as sql
import os
class Veritabani:
    def __init__(self,adres):
        self.adres = adres
        
    def veritabaniAc(self):
        self.db = sql.connect(self.adres)
        cursor = self.db.cursor()
        return cursor 
 
    def Listele(self,Ay,Kalem):
        try:
            officeboy = self.veritabaniAc()
            sorgu = """
            SELECT * FROM V_HESAP WHERE 1=1
            """
            if not Ay == "Seçiniz":
                sorgu+= " AND Ay='"+Ay+"'"
            if not Kalem == "Seçiniz":
                sorgu+= " AND Kalem='"+Kalem+"'"
                       
            officeboy.execute(sorgu)
            return officeboy.fetchall()
        except Exception as Hata:
            print("Hata Mesajı:",Hata)
        finally:
            self.db.close()


    def SozlukListele(self,TabloID):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            SELECT
            SOZLUK_ADI,
            SOZLUK_ID            
            FROM HSP_SOZLUK
            WHERE TABLO_ID = {}
            """.format(TabloID))
            return officeboy.fetchall()
        except Exception as Hata:
            print("Hata Mesajı:",Hata)
        finally:
            self.db.close()

    def SozlukListeleSozluk(self):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            SELECT * FROM HSP_SOZLUK
            WHERE 1 = 1
            """)
            return officeboy.fetchall()
        except Exception as Hata:
            print("Hata Mesajı:",Hata)
        finally:
            self.db.close()

    def VeriGuncelle(self,kalem,ay,tutar,ID):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            UPDATE HSP_BILGI SET 
            HSP_AY = {},
            HSP_BLG_KALEM = {},
            HSP_BLG_TUTAR = {}
            WHERE HSP_BLG_ID = {}
            """.format(ay,kalem,tutar,ID)
            )
            self.db.commit()
            return "1"
        except Exception as Hata:
            return "Hata Mesajı: {}".format(Hata)
        finally:
            self.db.close()

    def VeriGuncelleSozluk(self,tablo_id,sozluk_id,sozluk_adi,ID):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            UPDATE HSP_SOZLUK SET 
            TABLO_ID = {},
            SOZLUK_ID = {},
            SOZLUK_ADI = {}
            WHERE ID = {}
            """.format(tablo_id,sozluk_id,sozluk_adi,ID)
            )
            self.db.commit()
            return "1"
        except Exception as Hata:
            return "Hata Mesajı: {}".format(Hata)
        finally:
            self.db.close()

    def VeriSil(self,ID):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
                DELETE FROM 
                HSP_BILGI 
                WHERE HSP_BLG_ID = {} 
            """.format(ID)
            )
            self.db.commit()
            return "1"
        except Exception as Hata:
            return "Hata Mesajı: {}".format(Hata)
        finally:
            self.db.close()


    def VeriEkle(self,kalem,ay,tutar):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            INSERT INTO HSP_BILGI 
            (HSP_AY,
            HSP_BLG_KALEM,
            HSP_BLG_TUTAR)
            values
            ({},{},{})
            """.format(ay,kalem,tutar)
            )
            self.db.commit()
            return "1"
        except Exception as Hata:
            return "Hata Mesajı: {}".format(Hata)
        finally:
            self.db.close()

    def VeriEkleSozluk(self,tablo_id,sozluk_id,sozluk_adi):
        try:
            officeboy = self.veritabaniAc()
            officeboy.execute("""
            INSERT INTO HSP_SOZLUK 
            (TABLO_ID,
            SOZLUK_ID,
            SOZLUK_ADI)
            values
            ({},{},{})
            """.format(tablo_id,sozluk_id,sozluk_adi)
            )
            self.db.commit()
            return "1"
        except Exception as Hata:
            return "Hata Mesajı: {}".format(Hata)
        finally:
            self.db.close()

if __name__ == "__main__":
    vt = Veritabani(os.getcwd()+r"\IEDB.db")
    vt.SozlukListele(1)