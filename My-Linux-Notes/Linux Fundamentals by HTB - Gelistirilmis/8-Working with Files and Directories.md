---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 8-Working with Files and Directories

> [!abstract] Öğrenme hedefi
> Dosya/dizin oluşturma, taşıma, kopyalama ve güvenli silme akışını öğrenmek.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `touch` yalnızca boş dosya oluşturmaz; var olan dosyanın zaman damgalarını da günceller.
- `mv` hem yeniden adlandırır hem taşır; hedef dizin yazılabilir olmalıdır.
- Regex ile shell glob (`*`, `?`, `[]`) aynı şey değildir.

## Eksik kalabilecek kavramlar

- `cp -a`, `rm -i`, `rmdir`
- brace expansion
- boşluk içeren yolları tırnaklama

## Bilişsel bağlantılar

[[7-Navigation|Yollar]] · [[14-Permission Management|İzinler]]

## Aktif tekrar / mini lab

```bash
`mkdir -p /tmp/lf-lab/{src,dst}; touch /tmp/lf-lab/src/{a,b}.txt; cp -a /tmp/lf-lab/src/. /tmp/lf-lab/dst/`.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

**Reminder:** Keep in mind that online research is a valuable part of the learning process—it’s not cheating. You’re not being tested right now, but rather building your knowledge. Searching for solutions online can expose you to different approaches and alternative methods, giving you a broader understanding of how things work and helping you discover the most efficient ways to solve problems.

**regex:** regular expressions. Bu bir komut değil genel bir kısaltma.

# Creating:
- create a file use `touch <name>` i.e touch info.txt it is an empty file btw.
- create a directory use `mkdir <name>` i.e mkdir storage.
- When organizing your system, you may need to create multiple directories within other directories. Manually running the `mkdir` command for each one would be time-consuming. Fortunately, the mkdir command has the `-p` (parents) option, which allows you to create parent directories automatically. Knk bu içi içine aynı matruşkalar gibi klasör yapıyor. i.e. `mkdir -p storage/local/user/documents`
- Bak böyle bir şey yaptın ya sonra eserini görmek istediğin bu katman katman olun için *tree* denen bir tool var. kullanmak için `tree .`yap sana bulunduğun yerden sonraki içindeki yerleri gösterir ve kac direc var kac file var yazar
- Btw you can create a file or directory where you want for this you can use `touch or mkdir /path`işte knk
# move and rename:
- for rename `mv <file/directory> <renamed file/directory>`. mesela if you want info to new_info you use mv info.txt new_info.txt 
- multiple move for this mv things1 things 2 ... where you want for this i.e. mv info.txt readme.txt /etc/aha_burada
