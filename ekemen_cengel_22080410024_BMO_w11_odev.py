# Dictionary liste oluşturup içine İsim, Cinsiyet, Matematik ve Türkce isimli keyler oluşturduk ve tablodaki bilgileri buraya aktardık.
sinav_sonuc = {'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'Cinsiyet':['K','E','E','E','K','K'],
'Matematik':[80,60,77,25,36,75],
'Türkce':[90,50,53,100,98,66]}
# Kullanacagimiz liste ve degiskenlere baslangıc degeri verdik.
kTnotlist = [] # kadin Türkce not listesi
eTnotlist=[] # erkek Türkce not listesi
ks=0 # kadın sayisi
knotop=0 # kadin not toplamı
kTnotop=0 # kadin Türkce not toplamı
eTnotop=0 # erkek Türkce not toplami
es=0 # erkek sayisi
enotop=0 # erkek not top
sınTnottop=0 # sınıf Türkce not ort
i=-1 # index 
# for dongusune cinsiyet keyini verdik ve dongu onu dondurecek. Aynı zamanda i degiskenini de index yerine kullandim.
# Böylelikle if ve elif içerisinde kadinlarin ve erkeklerin sayilarini ve notlarini ayirt etmekte kullandim
for x in (sinav_sonuc['Cinsiyet']):
    i+=1
    if (x=='K'):
        ks=ks+1
        knot=sinav_sonuc['Matematik'][i]
        knotop=knotop+knot
        kTnot=sinav_sonuc['Türkce'][i]
        kTnotop=kTnot + kTnotop
        kTnotlist.append(kTnot)
    elif (x =='E'):
        es=es+1
        enot=sinav_sonuc['Matematik'][i]
        enotop=enotop+enot
        eTnot=sinav_sonuc['Türkce'][i]
        eTnotop=eTnot+eTnotop 
        eTnotlist.append(eTnot)
    sınTnot = sinav_sonuc['Türkce'][i]
    sınTnottop = sınTnottop + sınTnot
# for döngüsünün icinde hesaplanan degerleri yazdırma asamasına gectik printlerin icinde ortalamaya donusturuyoruz.
print(f"Kadınlar Matematik Ortalama= {knotop/ks}")
print(f"Erkekler Matematik Ortalama= {enotop/es}")
print(f"Kadın Türkçe Ortalama= {kTnotop/ks}")
print(f"Erkek Türkçe Ortalama= {eTnotop/es}")
print(f"Sınıf Türkçe ortalama= {sınTnottop/(es+ks)}")

# Kadinlarin ve erkeklerin max notlarini atadigimiz listelerin en büyük degerlerini kmax ve emax kismna atiyoruz ve onlari yazdiriyoruz.
kmax = max(kTnotlist)
emax = max(eTnotlist)
print(f"Kadınlar Türkçe Max= {kmax}")
print(f"Erkekler Türkçe Max= {emax}")