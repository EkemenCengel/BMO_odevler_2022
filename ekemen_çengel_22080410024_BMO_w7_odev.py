#kisiler isimli bos bir liste olusturuyoruz
kisiler = []
#Kullanicidan uc isim bilgisi aliyoruz
x  = input("Listeye eklenecek ilk isimi giriniz:")
y = input("Listeye eklenecek ikinci isimi giriniz:")
z = input("Listeye eklenecek ucuncu isimi giriniz:")
#Kullanicidan uc isim bilgisi aldik.
#Simdi bu isimleri kisiler isimli listemize .append metodu ile ekliyoruz
kisiler.append(x)
kisiler.append(y)
kisiler.append(z)
#Listemizi ekrana yazdiriyoruz
print(kisiler)
#Listemizin uzunlugunu uz isimli degiskenimize atadik
uz = (len(kisiler))
# uz isimli degiskenimiz yazdirarak listemizin uzunlugunu yazdiriyoruz
print(uz)
#kisiler isimli listemizin 2. elemanini yazdiriyoruz
print(kisiler[1])
#.pop metodu ile listemizin son elemanni siliyoruz
kisiler.pop()
#Listemizin son halini ekrana yazdiriyoruz
print(kisiler)