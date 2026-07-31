---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 1-Intro

> [!abstract] Öğrenme hedefi
> Linux, kernel, işletim sistemi ve temel bileşenleri birbirinden ayırmak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- Linux teknik olarak çekirdektir; dağıtım ise Linux çekirdeği + GNU araçları + paket yöneticisi + kullanıcı alanı yazılımlarından oluşur.
- Kernel, uygulama ile “OS” arasında ayrı bir katman değil; işletim sisteminin donanım, süreç, bellek ve I/O yöneten çekirdek parçasıdır.
- GNOME/KDE birer masaüstü ortamıdır; pencere yöneticisi bunların yalnızca bir bileşenidir. Modern sistemlerde X11 yanında Wayland da kullanılır.

## Eksik kalabilecek kavramlar

- user space ve kernel space
- system call kavramı
- dağıtım–çekirdek–shell ilişkisi

## Bilişsel bağlantılar

[[3-Intro|Dosya sistemi ve dağıtımlar]] · [[4-Prompt Description|Shell istemi]]

## Aktif tekrar / mini lab

```bash
`uname -a; cat /etc/os-release; echo "$SHELL"` çıktılarında çekirdek, dağıtım ve shell bilgisini ayır.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

# What is Linux ?
- Actually it is a kernel which is a little man between the application and the os and the hardwares.
- The distrubition of linux kernel is a costumasized os since the linux is open-source
- The overall Android operating system that runs on smartphones and tablets is based on the Linux kernel, and because of this, Linux is the most widely installed operating system.
# What is OS?
- An OS is software that manages all of the hardware resources associated with our computer. That means that an OS manages the whole communication between software and hardware.
# Linux follows five core principles?
1. Everything is a file
2. Small, single-purpose programs
3. Ability to chain programs together to perform complex tasks
4. Avoid captive user interfaces (gui diyor burada)
5. Configuration data stored in a text file (An example of such a file is the `/etc/passwd` file, which stores all users registered on the system.)
# What is the components of linux?
1. **Bootloader** : A piece of code that runs to guide the booting process to start the operating system. Parrot Linux uses the GRUB Bootloader.
2. **OS Kernel** : The kernel is the main component of an operating system. It manages the resources for system's I/O devices at the hardware level.
3. **Daemons** : Background services are called "daemons" in Linux. Their purpose is to ensure that key functions such as scheduling, printing, and multimedia are working correctly. These small programs load after we booted or log into the computer.
4. **OS Shell** : The operating system shell or the command language interpreter (also known as the command line) is the interface between the OS and the user. This interface allows the user to tell the OS what to do. The most commonly used shells are Bash, Tcsh/Csh, Ksh, Zsh, and Fish.
5. **Graphics Server** : This provides a graphical sub-system (server) called "X" or "X-server" that allows graphical programs to run locally or remotely on the X-windowing system.
6. **Window Manage**r : Also known as a graphical user interface (GUI). There are many options, including GNOME, KDE, MATE, Unity, and Cinnamon. A desktop environment usually has several applications, including file and web browsers. These allow the user to access and manage the essential and frequently accessed features and services of an operating system.
7. **Utilities** : Applications or utilities are programs that perform particular functions for the user or another program.

# Commands
- `pwd`: stands for print working directory tell us where we are at.
- `ls`: stands for list. It shows directory etc. you are around.
- `cd`: stands change directory. Usage: cd *nameofdirectory*.
- `cd ..`:  it helps to go backwards. One time.
- `cd ../..`:  2 times goes backwards.

