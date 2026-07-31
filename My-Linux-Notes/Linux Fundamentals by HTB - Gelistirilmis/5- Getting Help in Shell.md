---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 5- Getting Help in Shell

> [!abstract] Öğrenme hedefi
> Komutları ezberlemek yerine yerleşik yardım sistemini etkin kullanmak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- Uzun seçenek çoğunlukla `--help` biçimindedir; `-help` evrensel değildir.
- `-h` her programda yardım anlamına gelmez; komutun belgesine bakılmalıdır.
- `apropos`, man sayfası veritabanında arama yapar; sonuç yoksa `mandb` gerekebilir.

## Eksik kalabilecek kavramlar

- `man` bölüm numaraları
- `info`, `type`, `help` ve `whatis`
- shell built-in ile harici program ayrımı

## Bilişsel bağlantılar

[[4-Prompt Description|Shell temeli]] · [[9-Editing Files|Editör yardımı]]

## Aktif tekrar / mini lab

```bash
`type cd; help cd; man 1 passwd; man 5 passwd; apropos "copy files"` komutlarının farkını gözlemle.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

# Man:
- One such method is using the `man` command, which displays the manual pages for commands and provides detailed information about their usage. Usage man *toolname*
# Help:
- `--help` detaylı bilgi verir tool hakkında. Usage: *tool* -help
- `-h` --help'den daha kısa daha öz bilgi verir. Usage: *tool* -h
# Apropos:
- Another tool that can be useful in the beginning is `apropos`. Each manual page has a short description available within it. This tool searches the descriptions for instances of a given keyword. Usage: apropos *keyword* i.e. apropos sudo

