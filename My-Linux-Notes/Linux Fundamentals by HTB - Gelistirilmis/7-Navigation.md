---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 7-Navigation

> [!abstract] Öğrenme hedefi
> Yolları, gizli dosyaları, inode ve dosya metadatasını okuyabilmek.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `ls -l` başındaki `total`, dosya boyutlarının KB toplamı değildir; kullanılan blokların toplamıdır ve blok birimi sisteme/ortama göre değişebilir.
- Dizin satırındaki boyut genellikle içerdiği dosyaların toplamı değildir; dizin girdileri için ayrılan alanı gösterir.
- Inode numarası dosya sistemi içinde tanımlıdır; tüm sistem genelinde evrensel benzersiz değildir.

## Eksik kalabilecek kavramlar

- `cd -`, `cd ~`, `.` ve `..`
- symlink ve hard link
- globbing

## Bilişsel bağlantılar

[[3-Intro|FHS]] · [[8-Working with Files and Directories|Dosya işlemleri]]

## Aktif tekrar / mini lab

```bash
`ls -lai; stat .; pwd; cd /tmp; cd -` ile yol ve metadata ilişkisini gözlemle.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

**pwd:** Print Working Directory. It shows which directory you are

# ls:
## `-l`:
- Using it without any additional options will display the directories and files only. However, we can also add the `-l` option to display more information on those directories and files.
- İlk görüdüğün şey total 32 mesela 32 Kb yer kaplıyor oradaki tüm dosyalar. Aslında bu 32 blocks demek her block ise 1024 bytes
- |`drwxr-xr-x`|Type and permissions|
- |`2`|Number of hard links to the file/directory|
- |`cry0l1t3`|Owner of the file/directory|
- |`htbacademy`|Group owner of the file/directory|
- |`4096`|Size of the file or the number of blocks used to store the directory information|
- |`Nov 13 17:37`|Date and time|
- |`Desktop`|Directory name|
## `-la`:
- However, we will not see everything that is in this folder. A directory can also have hidden files that start with a dot at the beginning of its name (e.g., `.bashrc` or `.bash_history`). Therefore, we need to use the command `ls -la` to `list all` files of a directory:
- bu ls toolunda sen ls /var/mail yazarsan oraya navigate etmene gerek kalmadan oradakileri show edersin
## `-i`:
- bunun sayesinde dosyanın index numarasını görürsün. —officially known as an **inode** (index node)—is a unique integer assigned to every file and directory. It acts as a primary identifier for the operating system to track file metadata rather than its name
## `-t`:
- knk bu altındaki dosyları klasörleri en son modifiye edilene göre sıralar. kullanım `ls -t`.
# `stat`:
- knk bu da bir komut. This will display the inode number alongside detailed access rights and modification dates. Yani buda aklında bulunsun.
