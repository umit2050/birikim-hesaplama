# Birikim hesaplama ===============================

# Kullanıcıdan veri aldığımız bölüm================
t = int(input("Aylık tasarruf miktarınız (₺): "))
s = int(input("Tasarruf süresi (yıl): "))
f = int(input("Aylık faiz oranı (%): "))

# Formüller =======================================
sure = int(12*s)
oran = ((f/100)+1)
toplam_birikim = 0

for i in range (sure):
    sure+= 1
    faiz_geliri = (t*f)/100
    toplam_birikim = (toplam_birikim + t) * (oran)

faiz_getiri = toplam_birikim - (t*s*12)
 
# Sonucu ekrana yazdırma ==========================
print ("{} yıl sonraki toplam birikim: {}₺".format (s, round(toplam_birikim,2)))
print ("Toplam faiz getirisi: {0:.2f}₺" .format(faiz_getiri))
