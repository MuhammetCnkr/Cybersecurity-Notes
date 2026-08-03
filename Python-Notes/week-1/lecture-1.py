#terminalde code hello.py dediğin zaman sana hello.py adında bir dosya oluşturur.
#terminalde bir python dosyası çalıştırmak için python hello.py demen yeterlidir.



print("Hello, World!")
#böyle dediğin zaman burada print senin fuction oluyor "hello, World!" ise senin argument oluyor. yani print("Hello, World!") dediğin zaman print fonksiyonuna "Hello, World!" argument olarak göndermiş oluyorsun.

print ("Hello, World!" #burada parantezi kapatmadığın için sana SyntaxError verir

#input("What is your name?") böyle dediğin zaman ayrı ayrı print kullanmana gerek kalmadan input hem print işlevi yapar hem de input kendi işlevini yapar. yani input("What is your name?") dediğin zaman ekrana "What is your name?" yazdırır ve kullanıcıdan bir input bekler. kullanıcı bir input verdikten sonra bu inputu kullanabilirsin.

#return values bazı functions böyle mesela input sen cevabı giridi zaman sana return eder. yani input("What is your name?") dediğin zaman kullanıcı bir input verdikten sonra bu inputu kullanabilirsin. mesela name = input("What is your name?") dediğin zaman kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun. böylece name değişkenini kullanarak kullanıcıdan aldığın inputu kullanabilirsin.
#variables bu ise senin return values dödüren fonksiyonları kullanabilmen için değişkenlere ataman gerekiyor. mesela name = input("What is your name?") dediğin zaman kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun. böylece name değişkenini kullanarak kullanıcıdan aldığın inputu kullanabilirsin.


#python ya da birçok prgramala dilinde single = anlamı eşittir değil aslında bir assignment operator yani atama operatörü. yani name = input("What is your name?") dediğin zaman kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun.

#print(name) böyle yaptığım zaman "" içinde olmadığı için name değişkeninin içindeki değeri ekrana yazdırır. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve print(name) dediğin zaman name değişkeninin içindeki değeri ekrana yazdırır.

#comments sen bunu kodunda açıklama falan yapmak için kullanırsın bu ignore edilir

#pseudocode : express your thoughts in a way that is easy to understand. yani senin kodunu yazmadan önce ne yapmak istediğini anlatmak için kullanılır. mesela sen bir program yazmak istiyorsun ama nasıl yapacağını bilmiyorsun. bu durumda sen pseudocode kullanarak ne yapmak istediğini anlatabilirsin.
name = input("what is your name? ")
print("hello, " + name) #böyle dediğin zaman ekrana "hello" ve name değişkeninin içindeki değeri yazdırır. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve print("hello" + name) dediğin zaman ekrana "hello" ve name değişkeninin içindeki değeri yazdırır.

print("hello, ", name) #burada virgül bu artı işareti gibi işe yarar ama bir farkla artıda otomatik bir boşluk ekelem yok bunda var otomatik bir boşluk ekler
#virgülde birleştirme yaptığın veri türleri galiba farklı olabilir str ile int birleştirebilirsin
# str : string yani metin demek. mesela name değişkini bir stringdir.
#print fonskiyonunda otomatik olarak işini bitirdikten sonra alt satıra geçme şeyi var.

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) #print fonksiyonunun parametreleri. yani print fonksiyonu bu parametreleri alır. objects : yazdırmak istediğin şeyler. sep : yazdırmak istediğin şeylerin arasına ne koymak istediğin (sen , koyduğun zaman objectlerin arasında bu sep boşluk birakır). end : yazdırmak istediğin şeylerin sonunda ne koymak istediğin. file : yazdırmak istediğin şeyleri nereye yazdırmak istediğin. flush : yazdırmak istediğin şeyleri hemen yazdırmak isteyip istemediğin.
#yukarıdaki * işareti istediği kadar input girebilirsin demek. yani print("hello", "world") dediğin zaman ekrana "hello world" yazdırır. yani print fonksiyonu istediğin kadar input alabilir.
#yukarıdaki sep end aslında senin parametrelerindir.


#print("hello, "friend"") dediğin zaman bu hatalı olur çünkü senin stringin içinde çift tırnak var. yani print("hello, "friend"") dediğin zaman ekrana "hello, "friend"" yazdırmak istiyorsun ama senin stringin içinde çift tırnak var. bu yüzden python bunu anlayamaz ve hata verir. bu hatayı düzeltmek için ya tek tırnak kullanabilirsin ya da çift tırnak kullanabilirsin. mesela print('hello, "friend"') dediğin zaman ekrana 'hello, "friend"' yazdırır. ya da print("hello, 'friend'") dediğin zaman ekrana "hello, 'friend'" yazdırır.
#print("hello, \"friend\"") dediğin zaman escaping character kullanarak hatadan kaçmış oldun



print(f"hello, {name}") # f-string kullanmak için f-string kullanabilirsin. yani print(f"hello, {name}") dediğin zaman ekrana "hello, name değişkeninin içindeki değer" yazdırır. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve print(f"hello, {name}") dediğin zaman ekrana "hello, name değişkeninin içindeki değer" yazdırır.

# Remove whitespace from strings: strip(), lstrip(), rstrip() #strip() : stringin başındaki ve sonundaki boşlukları siler. lstrip() : stringin başındaki boşlukları siler. rstrip() : stringin sonundaki boşlukları siler.
name = name.strip() #böyle dediğin zaman name değişkeninin başındaki ve sonundaki boşlukları siler. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve name = name.strip() dediğin zaman name değişkeninin başındaki ve sonundaki boşlukları siler.


# Capataliza user's name
name = name.capitalize() #böyle dediğin zaman name değişkeninin ilk harfini büyük yapar. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve name = name.capitalize() dediğin zaman name değişkeninin ilk harfini büyük yapar.


name = name.title() #böyle dediğin zaman name değişkeninin her kelimesinin ilk harfini büyük yapar. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve name = name.title() dediğin zaman name değişkeninin her kelimesinin ilk harfini büyük yapar.


# Capataliza user's name and capitalize the first letter of each word in the name
name = name.strip().title() #böyle dediğin zaman name değişkeninin başındaki ve sonundaki boşlukları siler ve her kelimesinin ilk harfini büyük yapar. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve name = name.strip().title() dediğin zaman name değişkeninin başındaki ve sonundaki boşlukları siler ve her kelimesinin ilk harfini büyük yapar.

name = input().strip().title() #böyle dediğin zaman kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve name = input().strip().title() dediğin zaman name değişkeninin başındaki ve sonundaki boşlukları siler ve her kelimesinin ilk harfini büyük yapar.

# Split user's name into first name and last name

first, last = name.split(" ") #böyle dediğin zaman name değişkeninin içindeki değeri boşluk karakterine göre böler ve ilk kelimeyi first değişkenine atar ve ikinci kelimeyi last değişkenine atar. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve first, last = name.split(" ") dediğin zaman name değişkeninin içindeki değeri boşluk karakterine göre böler ve ilk kelimeyi first değişkenine atar ve ikinci kelimeyi last değişkenine atar.


#INTEGERS
#bunda + - * / % yardımıyla matemtiksel işlemler yapabilirsin. mesela 5 + 3 dediğin zaman ekrana 8 yazdırır. 5 - 3 dediğin zaman ekrana 2 yazdırır. 5 * 3 dediğin zaman ekrana 15 yazdırır. 5 / 3 dediğin zaman ekrana 1.6666666666666667 yazdırır. yani bölme işlemi float döndürür. yani float : ondalıklı sayı demek. yani float : decimal number demek.

#interactive mode : python interpreter ile etkileşimli modda çalışabilirsin. yani terminalde python dediğin zaman python interpreter açılır ve burada python kodlarını yazabilirsin. mesela terminalde python dediğin zaman python interpreter açılır ve burada print("hello") dediğin zaman ekrana hello yazdırır. yani interactive mode : python interpreter ile etkileşimli modda çalışabilirsin. yani terminalde python dediğin zaman python interpreter açılır ve burada python kodlarını yazabilirsin. mesela terminalde python dediğin zaman python interpreter açılır ve burada print("hello") dediğin zaman ekrana hello yazdırır.

# Burada basit bir toplama işlemi yapıyoruz. kullanıcıdan iki sayı alıyoruz ve bu sayıları topluyoruz.
variable1 = int(input("what is variable1? ")) #input fonksiyonu strinf return value yapar sen onu integer yapman lazım matematiksel toplama yapabilmek için. yani variable1 = int(input("what is variable1? ")) dediğin zaman kullanıcı bir input verdikten sonra bu inputu integer yapar ve variable1 değişkenine atar. yani kullanıcı bir input verdikten sonra bu inputu variable1 değişkenine atamış oluyorsun ve variable1 = int(input("what is variable1? ")) dediğin zaman kullanıcı bir input verdikten sonra bu inputu integer yapar ve variable1 değişkenine atar.
variable2 = int(input("what is variable2? ")) #burada aslında int de bir functiondır.
print(variable1 + variable2)
#yukarıda eğer integer çevirme yapmasaydın concantianting string yapar yani sen ilk başta eğer 23 girdin ve sonra 43 girdiysen sana 2342 yazar onları string toplamasına göre toplar




print(int(input("what is variable1? ")) + int(input("what is variable2? "))) #böyle dediğin zaman yine aynı şeyi elde edersin ama fazla clean code olmaz, fazla compliacte yaparsın

#FLOATS
#böyle dediğin zaman float yani ondalıklı sayı ile matematiksel işlemler yapabilirsin. mesela 5.0 + 3.0 dediğin zaman ekrana 8.0 yazdırır.

x = float(input("what is x? ")) #böyle dediğin zaman kullanıcı bir input verdikten sonra bu inputu float yapar ve x değişkenine atar. yani kullanıcı bir input verdikten sonra bu inputu x değişkenine atamış oluyorsun ve x = float(input("what is x? ")) dediğin zaman kullanıcı bir input verdikten sonra bu inputu float yapar ve x değişkenine atar.
y = float(input("what is y? ")) #burada aslında float de bir functiondır.
print(x + y) #böyle dediğin zaman ekrana x ve y değişkenlerinin içindeki değerleri toplar ve ekrana yazdırır. yazdırma yaparken float formatta yazar.


round(number[, ndigits]) #round() fonksiyonu number parametresini alır ve ndigits parametresini alır. number : yuvarlamak istediğin sayı. ndigits : yuvarlamak istediğin ondalık basamak sayısı. yani round(3.14159, 2) dediğin zaman ekrana 3.14 yazdırır.

z = round(x + y)
print(z)

print(f"{z:,}") #böyle dediğin zaman ekrana z değişkeninin içindeki değeri binlik basamak ayırıcı ile yazdırır. yani kullanıcı bir input verdikten sonra bu inputu z değişkenine atamış oluyorsun ve print(f"{z:,}") dediğin zaman ekrana z değişkeninin içindeki değeri binlik basamak ayırıcı ile yazdırır.
print(f"{z : .2f}") #böyle dediğin zaman ekrana z değişkeninin içindeki değeri 2 ondalık basamak ile yazdırır. yani kullanıcı bir input verdikten sonra bu inputu z değişkenine atamış oluyorsun ve print(f"{z : .2f}") dediğin zaman ekrana z değişkeninin içindeki değeri 2 ondalık basamak ile yazdırır.
z = round(x / y, 2) #böyle dediğin zaman ekrana z değişkeninin içindeki değeri 2 ondalık basamak ile yazdırır. yani kullanıcı bir input verdikten sonra bu inputu z değişkenine atamış oluyorsun ve z = round(x / y, 2) dediğin zaman ekrana z değişkeninin içindeki değeri 2 ondalık basamak ile yazdırır.




def hello(to): # burada def ile bir function tanımlıyorsun. yani def hello(to): dediğin zaman hello adında bir function tanımlıyorsun ve to parametresini alıyor. yani hello("world") dediğin zaman ekrana "hello, world!" yazdırır. yani kullanıcı bir input verdikten sonra bu inputu to parametresine atamış oluyorsun ve print(f"hello, {to}!") dediğin zaman ekrana "hello, to parametresinin içindeki değer!" yazdırır.
    print(f"hello, {to}!") # böyle dediğin zaman ekrana "hello, to değişkeninin içindeki değer!" yazdırır. yani kullanıcı bir input verdikten sonra bu inputu to değişkenine atamış oluyorsun ve print(f"hello, {to}!") dediğin zaman ekrana "hello, to değişkeninin içindeki değer!" yazdırır.
name = input("what is your name? ")
hello(name) #böyle dediğin zaman ekrana "hello, name değişkeninin içindeki değer!" yazdırır. yani kullanıcı bir input verdikten sonra bu inputu name değişkenine atamış oluyorsun ve hello(name) dediğin zaman ekrana "hello, name değişkeninin içindeki değer!" yazdırır.


def hello(to="world"): # burada def ile bir function tanımlıyorsun. yani def hello(to="world"): dediğin zaman hello adında bir function tanımlıyorsun ve to parametresini alıyor ve default olarak "world" değerini alıyor. yani hello() dediğin zaman ekrana "hello, world!" yazdırır. yani kullanıcı bir input vermediği zaman to parametresine "world" değeri atanır ve print(f"hello, {to}!") dediğin zaman ekrana "hello, world!" yazdırır.
    print(f"hello, {to}!") # böyle dediğin zaman ekrana "hello, to değişkeninin içindeki değer!" yazdırır. yani kullanıcı bir input verdikten sonra bu inputu to değişkenine atamış oluyorsun ve print(f"hello, {to}!") dediğin zaman ekrana "hello, to değişkeninin içindeki değer!" yazdırır.

# hello() şeklinde bir kullanım yaparsan herhangi bir parametre vermeden adama sana to = "world" olarak yapar ama sen parametre verirsen
# mesela hello("muhammet") dediğin zaman to da world ignore edilir senin muhammet yazın base alınır
name = input("what is your name? ")

#python yukarıdan aşağıya okunan bir dil olduğu için bir fonskiyon yaparken önceden tanımlı oması lazım. yani hello() kullanacaksan def hello() yukarıda olmalı

"""
def main():
    name = input("what is your name? ")
    hello()

def hello():
    print(f"hello, {name}!")

main()
""" # knk burada name değişkeni main() fonksiyonunun içinde tanımlandığı için hello() fonksiyonu name değişkenini göremez. bu yüzden name değişkenini global olarak tanımlaman gerekiyor.

#scope : bir değişken veya fonksiyonun nerede geçerli olduğunu belirler. yani bir değişken veya fonksiyonun nerede geçerli olduğunu belirler. mesela bir değişken main() fonksiyonunun içinde tanımlanmışsa bu değişken sadece main() fonksiyonunun içinde geçerlidir. yani main() fonksiyonunun dışında bu değişkeni kullanamazsın. ama eğer bu değişkeni global olarak tanımlarsan bu değişkeni her yerde kullanabilirsin.

#RETURN

def main():
    x = int(input("what is x? "))
    print("x squared is ", my_square(x))

def my_square(n):
    return n * n #return : bir fonksiyonun sonucunu geri döndürür. yani my_square(n) fonksiyonu n * n sonucunu geri döndürür. yani main() fonksiyonu my_square(x) fonksiyonunu çağırdığında my_square(x) fonksiyonu x * x sonucunu geri döndürür ve main() fonksiyonu bu sonucu ekrana yazdırır.

main()

pow(n,2) #pow() fonksiyonu n sayısının 2. kuvvetini alır. yani pow(3,2) dediğin zaman ekrana 9 yazdırır. yani pow(n,2) dediğin zaman ekrana n sayısının 2. kuvvetini alır.


#bir şeyin function olup olmadığını anlama aslında name ardından gelen normal parantezler olmasıdır
# + ile birleştirmede aynı veri türünde olmalı ama , ile birleştirme farklı olursa sıkıntı olmaz.

# bir fonskiyonda return kullanman aslında burası benim fonksiyonun bittiği yer anlamına gelir ondan sonra olan kod blokları çalıştırılmaz. Be carefull.

"""
def main():
    ...
""" knk bu tarz kullanımda sen fonksiyon içine üç nokta koydupunda program sana hata vermez neden bu function boş demez

#local variable için bir functiona veridğin parametre o functionun altındaki variables dahil edilir.


#GLOBAL VARİABLE kullanmak için global <name> yapıyorsun
"""
global_house = 1
def area(uzunluk, genişlik):
    return uzunluk * genişlik

def main ():
    global global_house
    house = area(int(input("uzunluk : ")) , int(input("genişlik : ")))
    global_house = house

main()

print(global_house)
"""
