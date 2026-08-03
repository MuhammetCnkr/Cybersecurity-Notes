def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft): # aşağıda f string methodu var
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """
main()


spacecraft["distance"] = 0.01 # spacecrafta distance keyi yok varsayalım sen böyle yaparak hem key oluşturup hem de value atayabilirsin
# key in olup olmadığından emin değilsen :
spacecraft.get("distance", "Unknown") # böyle yaptığın durumda distance keyi varsa onun valuesunu basar yoksa ekrana Unknown yazar
spacecraft.update({"distance": 0.01, "orbit": "Sun"}) # bu da yeni bir ekleme yapma yöntemi distance ve orbit adında key ekledin ve bunlara karşılarındaki valueyu ekledin



distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}
def main():
    for name in distances.keys(): # bu kısımda name sadece keyler üzerinde hareket eder
        print(f"{name} is {distances[name]} AU from Earth")
main()





distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}
def main():
    for distance in distances.values(): # distance sadece values üzerinde geziyor
        print(f"{distance} AU is {convert(distance)} m")
def convert(au):
    return au * 149597870700
main()





#DICTIONARY
len(dictinory) #yaptığın zaman dictte kaç tane key olduğunu söyler
if guess in WORDS.keys(): # böyle bir kullanım var guess stringi eğer keyler arasında varsa True döner yoksa False döner
WORDS.pop(guess) # pop sayesinde guess değişkinin sahip olduğu değer olan key WORDS adlı dictinoryden silinir ve ayrıca bu keyin valuesunu ekrana return eder.
WORDS.clear() # clear sayesinde dictinorydeki tüm keyler ve valueslar silinir.
for key, value in WORDS.items(): # bu kısımda item() sayesinde tüm keyleri key'e liste olarak tüm valueları ie value'ya liste olarak atadık



#LIST
lists = []
lists.append("veri") #Listenin "en sonuna" veri eklemek için kullanılır
lists.append(["Muhammet","Çınkır"]) #.append ve içine liste verirsen listenin içine liste eklersin (sublist) itemler ayrı ayrı eklenmiş olmaz.
lists.remove(["Muhammet","Çınkır"]) #.remove sayesinde yazdığım itemi listeden kaldırırsın. Bu durumda ["Muhammet","Çınkır"] kaldırıldı.
lists.extend(["Muhammet","Çınkır"]) #.extend yardımıyla listenin sonuna ayrı bir liste eklemek yerine verdiğin listedeki her itemı ayrı ayrı ekler.
lists.insert(0, "Bowser") #.insert ilk aldığı parametre index ardından o eklemek istediğin veriyi girersin onu yazdığın index nnumarılı yere atar.
#.insert ile atamada yazdığın index numaralı yerdeki item silinmez o bir sağ kaydırılır yani indeksine 1 eklenir
lists.reverse() #.reverse sayesinde listen tam tersine döner -1. indeks 0. indeks olur.
lists.pop() #bu kullanımda listenin en sonundaki item silinir
lists.clear() #.clear sayesinde listedeki her şeyi silersin empty listen olur


#Elinde bir liste olsun listede de kelimeler olsın bazıları büyük harf içersin o listedeki büyük harf içeren kelimeleri küçük harfe çevirmek için
words = []
lowercase_words = [word.lower() for word in words]
lowercase_words = [word.lower() for word in words if len(word) > 4] #Burada if yapısnı ekleyerek sadece 4'den fazla uzunluğa sahip olan kelimeleri lowercase yapacak

counts = {word: lowercase_words.count(word) for word in lowercase_words} #lowercase_wrod'deki her item word ile gezilirken o itemı key yap ve valuesunu ise lowercase_words.count(word) sayısı ile aynı yap. Buradaki listedeki word olan itemların sayısını verir




#STRING METHODS:
show = ""
show.capitalize() #bu method sadece stringin ilk indeksini büyük yapar boşluk varsa büyütemez mesela diğer kelimelerin ilk harflerini büyütemez
show.strip() #bu method sayesinde ilklerdeki ve sonlardaki boşluklar kaldırılır
show.title() #bu method sayesinde every wordün ilk harfleri büyük oldu başta boşluk falan olması etkilemez
print(' '.join(cleaned_shows)) #yaptığın zaman o listenin bracketlerini virgüllerini göstermez daha clean şekilde liste göstermesi yapar



#STRING SLICING:
phone = "617-495-1000"
phone_list = phone.split("-")
print(phone[0:3]) #0. indeksten 3. indekse kadar olan karakterleri ekrana yazar. 3. indeks yazılmaz
print(phone[:3]) #yukarıdaki ile aynı işlemi yapar boş bırakırsan 0 kabul edilir
print(phone[8:12])
print(phone[8:]) #boş bıraktığın bu yeri en son indeks olarak alır
print(phone[-4:]) #bunun sayesinde -4. indeksten en son indekse kadar gösterme yapar



#TUPLES: bunlarda yeni value ekleme, silme, değiştirme yapamazsın. Bunun için tuple'ını list yap.
coordiantes_tuple = (42.376, -71.115) #() sayesinde tuple oluşturmuş oldun ve itemları , ile ayırmış oldun
coordinates_tuple[0] #0. indeksteki itema erişmek için kullanırsın like lists
latitude, longitude = coordinates_tuple #bunun sayesinde içindeki itemları sırasıyla variablelarına atamış oldun

import sys
print(f"{sys.getsizeof(coordiantes_tuple)} bytes") #bu sys kütüphanesi sayesinde tuple'ın kaç byte yer kaplaması yaptığını görebilirsin
#tuplelar memeory açaısından listlerden avantajları bu yüzden kullanıyorlar. 56 - 72 bytes. bunu kullanırken değiştirme v.s. yapamadığını unutma




