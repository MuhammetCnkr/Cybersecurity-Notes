---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# Extra by Bandit

> [!abstract] Öğrenme hedefi
> Bandit’te karşılaşılan kodlama/dönüştürme tekniklerini güvenlik bağlamıyla öğrenmek.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- ROT13 şifreleme sayılmamalıdır; sabit yerine koyma/kodlama tekniğidir ve güvenlik sağlamaz.
- ROT13 kendi tersidir: aynı dönüşüm ikinci kez uygulanınca özgün metin elde edilir.

## Eksik kalabilecek kavramlar

- hex dump
- compression türleri
- file/magic bytes
- base64

## Bilişsel bağlantılar

[[12-Filter Contents|tr ve base64]] · [[13-Regular Expressions|Metin desenleri]]

## Aktif tekrar / mini lab

```bash
`printf "Hello" | tr "A-Za-z" "N-ZA-Mn-za-m" | tr "A-Za-z" "N-ZA-Mn-za-m"`.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

- **Rot13:** knk bu bir şifreleme yöntemi özellikle ingilizce alfabede kullanılan çünkü 26 harf var olayı bir harfi kendisinden sonra gelen 13. harf ile replace ediyor.
- ![[Screenshot 2026-07-31 at 17.49.27.png]]
- knk tr toolunda böyle şeyler için çevirme olayı var.
