---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 13-Regular Expressions

> [!abstract] Öğrenme hedefi
> Regex desenlerini shell globlarından ayırıp güvenle kullanmak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `*` regexte önceki öğeyi 0 veya daha çok kez tekrarlar; tek başına “her şey” demek değildir.
- Her araç aynı regex lehçesini kullanmaz; `grep` BRE, `grep -E` ERE kullanır.
- Shell’in deseni değiştirmemesi için regex genellikle tek tırnak içine alınır.

## Eksik kalabilecek kavramlar

- anchors `^`/`$`
- character classes
- quantifiers ve grouping
- escaping

## Bilişsel bağlantılar

[[12-Filter Contents|grep/sed/awk]] · [[10-Find Files and Directories|find desenleri]]

## Aktif tekrar / mini lab

```bash
`printf "%s\n" root user1 user_2 | grep -E "^[a-z]+[0-9]?$"` sonucunu tahmin et ve doğrula.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

| **Operators** | **Description**                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `(a)`         | The round brackets are used to group parts of a regex. Within the brackets, you can define further patterns which should be processed together.                             |
| `[a-z]`       | The square brackets are used to define character classes. Inside the brackets, you can specify a list of characters to search for.                                          |
| `{1,10}`      | The curly brackets are used to define quantifiers. Inside the brackets, you can specify a number or a range that indicates how often a previous pattern should be repeated. |
| `\|`          | Also called the OR operator and shows results when one of the two expressions matches                                                                                       |
| `.*`          | Operates similarly to an AND operator by displaying results only when both expressions are present and match in the specified order                                         |

# Or Operator:
- Suppose we use the `OR` operator. The regex searches for one of the given search parameters. In the next example, we search for lines containing the word `my` or `false`. To use these operators, you need to apply the extended regex using the `-E` option in grep.
```bash
grep -E "(my|false)" /etc/passwd
# İçinde my veya false olan çıktıları basar
```
# And Operator:
- Since one of the two search parameters always occurs in the three lines, all three lines are displayed accordingly. However, if we use the `AND` operator, we will get a different result for the same search parameters.
```bash
grep -E "(my.*false)" /etc/passwd
# Burada içinde hem my olan hem false olanı basar
```

# RegEx:
- Standart `grep` komutunda bazı özel karakterleri (örneğin `|`, `+`, `?`, `()`) tanıyabilmesi için önüne ters eğik çizgi (`\`) koyman gerekir (`\|` gibi). `grep -E` (ya da kısaca `egrep`) kullandığında ise bu karakterler **doğrudan özel anlamlarıyla** çalışır. Yani karmaşık arama kalıplarını kaçış karakteri (`\`) kalabalığı olmadan, çok daha temiz yazabilirsin.
- ![[Screenshot 2026-07-27 at 10.42.38.png]]
