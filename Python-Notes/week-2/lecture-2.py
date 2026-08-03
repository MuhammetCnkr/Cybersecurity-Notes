# == equality = asignment != not equality

if x < y: #burada fark ettiysen paarantez kullanılmadı
    print("x is less than y") #syntax gereği if bloğunun içinde kod çalıştırmak istersen bir tab veya 4 defa space yapman lazım. buna indentation requirment denir

#knk arka arkasında if blokları kurduğun zaman program bundan öncekilerin doğru yanlış olmasını bakmadan tim if bloklarını check eder so greeksiz bir işlem maliyeti olur.
#start => if => if => if => stop

#ELIF == else if
#if => elif => elif yapsını kurduğun zaman eğer ki if doğruysa else if lere hiç girmeden stop kısmına gider ama eğer if doğru değilse else if lere girer ordan sırasıyla duruma göre gider.
#eğer bir elif doğruysa program geri kalanlara bakmadan direkt stop kısmına gider

#buralarda yapacağın sisteme az yük bindirme işi büyük projelerde gözle görülebilir bir fark yaratabilir.

#ELSE:
#if => elif => else bu durumlar program kendine 2 adet soru soruyor yukarıdaki örneğe göre 1 adet soru az maliyet az
#if doğru ise direkt stop. elif doğru ise direkt stop. else ifadesinde soru sormaz eğer bunun ikiside yanlış ise kesin bu durum kaldı ve bu olacak durumlarda kullanılır o da doğru olmak zorunda kaldı artık.


#! if 90 <= score <= 100: == if score >= 90 and score <= 100: #bunlar aynı anlama geliyor bunu kullanabilirsin

""" Kendime not:
Case 1: main(function()) - main() - function() => böyle bir durumda hata alırsın python main() kısmına kadar gelir ve burayı okuduktan sonra
yukarıya döner ve main(function()) çalıştırmaya başlar ama çalıştırırken daha function() kısmını okumadığı için hata alırsın
Case 2: main(function()) - function() - main() => böyle bir durumda python sıkıntısız çalışır main(funciton()) kısmını okur ardından function() kısmını okur
belleğe kaydeder gibi düşün(?) ardında main() kısmına gelince ise main(function()) çalıştırır ve sıkıntı yaşamaz function() belekte var zaten
"""

"""
Boolen Expressions: not (True) ==> False
if not (name == "muhammet"): # Bu şekilde kullanım yapabilirsin
"""
"""
Logical Expressions:
and : tüm durumlar doğru ise True en az bir tane False varsa False
or : en az bir durum True ise True tüm hepsi False ise False
"""
