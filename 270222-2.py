sayi1=int(input("1. Sayıyı Giriniz"))#İnputtan girilen değerler "string" tipindedir.
sayi2=int(input("2. Sayıyı Giriniz"))#Başa int ekleyerek integer dönüşümü yaptık.
#print(sayi1+sayi2)
#Toplama yapabilmek için string değeri ineger'a çevirmek gerekir.
#print(int(sayi1)+int(sayi2))
print("Sayılarınızın Toplamı:",sayi1+sayi2)
print("Sayılarınızın Çarpımı:",sayi1*sayi2)
print("Sayılarınızın Farkı:",sayi1-sayi2)
print("Sayılarınızın Bölümü:",sayi1/sayi2)
print("Sayılarınızın Bölümü:",sayi1//sayi2)#Tam bölme yapar
print("1. Sayı Üzeri 2. Sayı:",sayi1**sayi2)#Üs alma
print("1. Sayının 2. Sayıya Bölümünden Kalan:",sayi1%sayi2)