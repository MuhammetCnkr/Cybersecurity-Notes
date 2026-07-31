---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 3-Intro

> [!abstract] Öğrenme hedefi
> Linux dağıtımlarını ve FHS dizinlerinin amaçlarını anlamak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- Linux kök dizini `/` işaretidir; `\` değildir.
- `/etc` “etcetera” değildir; sistem çapındaki yapılandırmaları barındırır, IP/MAC bilgisinin kendisini zorunlu olarak saklayan tek bir yer değildir.
- `/usr` tarihsel olarak “Unix System Resources” şeklinde yorumlanır ve çoğu kullanıcı alanı programı/verisini taşır; modern sistemlerde `/bin` ve `/sbin`, `/usr` altına sembolik bağ olabilir.
- `/dev` sürücülerin kendisini değil, çekirdeğin aygıtları temsil eden özel dosyalarını içerir.

## Eksik kalabilecek kavramlar

- FHS ile mount kavramı
- mutlak ve göreli yollar
- `/proc`, `/sys`, `/run`, `/opt` ve `/srv`

## Bilişsel bağlantılar

[[7-Navigation|Dizinlerde gezinme]] · [[14-Permission Management|İzinler]]

## Aktif tekrar / mini lab

```bash
`findmnt; ls -ld /bin /sbin /usr/bin; ls /proc /sys /run` ile canlı sistemi FHS notuyla karşılaştır.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

# Distributions (Distros):
1. **Debian** uses an Advanced Package Tool (`apt`) package management system to handle software updates and security patches. The package management system helps keep the system up-to-date and secure by automatically downloading and installing security updates as soon as they are available
#  File System Hierarchy standard(FHS):
- Linux'ta her şey file haldedir. Mesela ls'in kendisi bir filedır.
- **bin:** bu ana dizinde olan binary'e stand eden. İçinde sistem tool dosyalarını barından bir dosya. i.e. ls, cp, rm
- **sbin:** bu da ana dizinde olan bin'e benzeyen ama superbin olduğu için adminlerin kullandığı komutları barındırır. i.e. adduser
- **usr:** içinde bin sbin vs çoğu şeyi ana dizinde olduğu gibi bulundurur. Sebebi ???   .
- **boot:** içinde boot dosyaları var.
- **tmp:** temprorary dosyalar var içinde.
- **var:** log files and also web application related files
- **lib:** more shared library files your system needs to boot
- **home:** where we live users live
- **root**: The home directory for the root user.
- **dev:** stands for devices. İçinde senin driverların disklerin falan olabilir. Vda or Vda1 stands for virtual disk, Sda or Sda1 stands for fiziksel disk. ve bu arada bunlar da file şeklinde 
- **etc:** stands for etcetera, etsy. içinde senin sistem ayarlarını network ayarlarını falan bulundurur. Mesela senin network ayarlarından ip mac vs bulunur
- **media:** Bir usb takıtığında otomatik olarak oraya file olarak düşer. External removable media devices such as USB drives are mounted here.
- **mnt:** Bunda ise yine media ile aynı ama senin manual şekilde yapman lazım. Temporary mount point for regular filesystems.

**Note** : A Linux terminal, also called a `shell` or command line, provides a text-based input/output (I/O) interface between users and the kernel for a computer system
**Note**: The most commonly used shell in Linux is the `Bourne-Again Shell` (`BASH`), and is part of the GNU project. Besides Bash, there also exist other shells like [Tcsh/Csh](https://en.wikipedia.org/wiki/Tcsh), [Ksh](https://en.wikipedia.org/wiki/KornShell), [Zsh](https://en.wikipedia.org/wiki/Z_shell), [Fish](https://en.wikipedia.org/wiki/Friendly_interactive_shell) shell and others.

# Commands:

- `whoami`: Tell us who we are logged in as
- `\`: The root of file system
- `clear`: Cleans your currently terminal windows. Aynı zamanda control+l yaparak da silebilirisin.
- `cat`: Stands for Concatenate. Dosyalardakileri okumanı falan sağlar. Usage: cat *nameoffile* 
- `cp`: Copy command. Usage: cp *eskidosyaname yenidosyaname* 
- `sudo`: Root veya admin olarak işlem yapmanı sağlar.
- `rm`: Stands for remove. Usage: rm *filename*
- `adduser`: Bu komut sayesinde yeni user eklersin. Usage: adduser supermc. Since it is in sbin, you have to be admin. Btw users which you added are in the /home directory.
- `which`: Kullandığın komuttun kime ait olduğunu söyler /usr/bin or /bin gibi. Usage: which ls 

