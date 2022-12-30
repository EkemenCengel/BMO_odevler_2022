# Fonksiyonumuzu tanimladik ve argüman kismina ihtiyaci olan argümanları yazdık 
# Sonrasinda ise alınacak degerleri listeye ekledik
def tabek(name,cinsiyet,vize_not,final_not):
    sinav_sonuc['isim'].append(name)
    sinav_sonuc['Cinsiyet'].append(cinsiyet)
    sinav_sonuc['Vize'].append(int(vize_not))
    sinav_sonuc['Final'].append(int(final_not))
    i=0
    for x in sinav_sonuc['Vize']:
        x = (x*0.3)
        y = sinav_sonuc['Final'][i]
        y = (y*0.7)
        s = (x+y)
        s = round(s,1)
        sinav_sonuc['Gecme_Notu'].append(s)
        i+=1

sinav_sonuc = {'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'Cinsiyet':['K','E','E','E','K','K'],
'Vize':[80,60,77,25,36,75],
'Final':[90,50,53,100,98,66],
'Gecme_Notu':[]}

# Ben kullanıcıya istediği kadar giriş yapma özgürlüğü verdim.
# Eger kullanıciyi 2 kayıt girmeye zorlamak istersek i=0 yapariz ardindan while döngüsünün koşul kismina i<2 yazariz ve döngünün icerisine i+=1 şeklinde bir artırıcı koyarız
print("En az iki giris yapmanızı istiyoruz.")
# Döngüde isim bilgisi  'cik' girilene kadar bilgi girilmeye devam edilir.
while True:
    # Fonksiyonun ihtiyaci olan isim (name) alıyoruz
    N = input("Ogrencinin ismini giriniz(Cikmak ve listeyi görüntülemek icin 'cik' yaziniz): ")
    # Cikmam icin firsat sunuyoruz
    if N =='cik':
        print("Cikis yaptiniz...")
        break
    # Fonksiyonumuzun ihtiyaci olan cinsiyeti alıyoruz ardından doğru değer girildiğinden emin olmak için kontrol yapıyoruz doğru değilse doğru olana kadar tekrar istiyoruz.
    C = input("ogrencinin cinsiyetini giriniz('Erkek','erkek','E','e','Kadın','K','kadın','kadin','Kadin','k'):")
    if(C=='Erkek' or C=='erkek' or C=='E' or C=='e'):
        C ='E'
    elif(C =='Kadın' or C=='K' or C=='kadın'or C=='kadin' or C=='Kadin' or C=='k'):
        C='K'
    else:
        C = 0
    while ((C=='E' or C=='K')==False):
        C = input("Ogrencinin cinsiyetini yanlis girdiniz lütfen tekrar giriniz('Kadın','K','kadın','kadin','Kadin','k','Erkek','erkek','E','e'): ")
        if(C=='Erkek' or C=='erkek' or C=='E' or C=='e'):
            C = 'E'
            break
        elif(C =='Kadın' or C=='K' or C=='kadın'or C=='kadin' or C=='Kadin' or C=='k'):
            C = 'K'
            break
        else:
            C = 0
    # Vize notunu istiyoruz ve 0-100 arasinda olup olmadiğini kontrol edip eger degilse dogru olana kadar tekrar istiyoruz.
    VN = int(input("Ogrencinin vize notunu giriniz: "))
    while ((0<=VN<=100)==False):
        VN = int(input("Ogrencinin vize notunu yanlıs girdiniz tekrar giriniz: "))
    # Final notunu istiyoruz ve 0-100 arasinda olup olmadiğini kontrol edip eger degilse dogru olana kadar tekrar istiyoruz.
    FN = int(input("Ogrencinin final notunu giriniz: "))
    while((0<=FN<=100)==False):
        FN = int(input("Ogrencinin final notunu yanlıs girdiniz tekrar giriniz: "))
    tabek(N, C, VN, FN)
print(sinav_sonuc)