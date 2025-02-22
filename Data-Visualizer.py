import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 

#örnek veri
veri = input("Lütfen excel dosyasını giriniz...")
df = pd.read_excel(f"{veri}.xlsx")
df["Tarih"] = pd.to_datetime(df["Tarih"])
df.set_index("Tarih",inplace=True)

def ekran_temizleme():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#menu fonksiyonu
def menu():
    print("Grafik seçenekleri:")
    print("1. Satışların Zaman İçindeki Değişimi (Çizgi Grafiği)")
    print("2. Aylık Toplam Satışlar (Bar Grafik)")
    print("3. Kategorilere Göre Satış Dağılımı (Pasta Grafik)")
    print("4. Fiyat ve Satış İlişkisi (Scatter Plot)")
    print("5. Fiyat Dağılımı (Histogram)")
    print("6. Aylık Satış Miktarları (Çizgi Grafik)")
    print("7. Fiyat Kategorisine Göre Toplam Satışlar (Bar Grafik)")
    print("0. Çıkış")

    return int(input("Seçiminizi yapın: "))


def grafik_secim(secilen):
    if secilen == 1:
        df["Satış"].plot(title="Satışların zaman içindeki değişimi",xlabel="Tarih",ylabel="Satış miktarı")
        plt.show()

    elif secilen == 2:
        aylik_satis = df.resample("ME")["Satış"].sum()
        aylik_satis.plot(kind="bar",title="Aylık toplam satışlar",xlabel="Ay",ylabel="Toplam Satış")
        plt.show()

    elif secilen==3:
        kategori_satis = df.groupby("Kategori")["Satış"].sum()
        kategori_satis.plot(kind="pie",autopct="%1.1f%%",title="Kategorilere göre satış dağılımı")
        plt.ylabel="" 
        plt.show()
    
    elif secilen == 4:
        df.plot(kind="scatter",x="Fiyat (TL)",y="Satış",title="Fiyat ve Satış İlişkisi")
        z = np.polyfit(df["Fiyat (TL)"],df["Satış"],1) 
        p = np.poly1d(z) 
        plt.plot(df["Fiyat (TL)"],p(df["Fiyat (TL)"]) ,  color ="red")
        plt.show()

    elif secilen == 5:
        df["Fiyat (TL)"].plot(kind="hist", bins=10, title= "Fiyat dağılımı")
        plt.xlabel= ("Fiyat (TL)")
        plt.ylabel= ("Kategori")
        plt.show()     

    elif secilen == 6:
        aylik_satis = df.resample("ME")["Satış"].sum()
        aylik_satis.plot(kind="line",title="Aylık Satış Miktarları")
        plt.xlabel("Ay")
        plt.ylabel("Satış Miktarı")
        plt.show()

    elif secilen == 7:
        bins = [0,1000,3000,5000,10000,20000] 
        labels = ["Düşük","Orta","Yüksek","Çok Yüksek","Lüks"]

        df["Fiyat Kategorisi"] = pd.cut(df["Fiyat (TL)"], bins =bins,labels=labels) 
        df.groupby("Fiyat Kategorisi")["Satış"].sum().plot(kind="bar",title="Fiyat Kategorisine Göre Toplam Satışlar")
        plt.xlabel("Fiyat Kategorisi")
        plt.ylabel("Toplam Satış")
        print(df[["Fiyat (TL)","Fiyat Kategorisi"]])
        plt.show()


while True:
    ekran_temizleme()
    secim = menu()
    if secim == 0:
        print("Çıkış yapılıyor...")
        break
    elif 1 <= secim <= 7:
        grafik_secim(secim)
    else:
        print("Geçersiz bir seçim yaptınız...")

    