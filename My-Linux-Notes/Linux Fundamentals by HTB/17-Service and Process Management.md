---
Date: 2026-07-29 11:57
category:
tags:
Tools:
---
- Services, also known as daemons, are fundamental components of a Linux system that run silently in the background "without direct user interaction".
- Bu servisler önemli görevleri gerçekleştiriyorlar ve ikiye ayrılırlar.
1. **System Services:** These are internal services required during system startup. They perform essential hardware-related tasks and initialize system components necessary for the operating system to function properly. These are like the engine and transmission systems. They start when you turn the ignition key and are essential for the car to run. Without them, the car wouldn't move.
2. **User-Installed Services:** These services are added by users and typically include server applications and other background processes that provide specific features or capabilities. These types of services are like the car's air conditioning or GPS navigation system. While not critical for the car to operate, they enhance functionality and provide additional features based on the driver's preferences.
- Bu daemons genelde `d` harfi ile tanımlanırlar ve genelde `sshd` veya `systemd` ile biterler. (SSH daemon)


- Most modern Linux distros have adopted ` systemd` as thir initialization system (init system).
- Knk ilk işlem bu boot process sırasında başlar ve ona Process ID (` PID`) derler. Linux sistemlerinde tüm işlemler ` PID` ile assign edilmiştir ve ` /proc/` altındadırlar. Bazıları Parent Process ID (` PPID`) ile gösterilir bu ise bu program başka bir program tarafından başlatıldığı için bunlara child processes denir

# Systemctl: 
- knk section 17'de bu anlatılıyor ben fazla bir şey anlamdım sonra buna bak lazım olursan
- galiba çalışan tüm şeyleri falan listelemeye yarıyor falan

# Kill a Process:
- knk bir process : Running, Waiting (waiting for an event or system resoruce), Stopped, Zombie (stopped but still has an entry in the process table) halinda olabilir.
- knk processler ` kill, pkill, pgrep, killall` yardımıyla kontrol edilebilir.
- knk ` kill -l` yaptıktan sonra karşına birkaç bir şey çıkar.
![[Screenshot 2026-07-31 at 12.24.32.png]]
- Burada ` kill 9 <PID>` kullanarak eğerki bir program donmuşsa onu kapatmaya zorlarsın

# Bacground a Process:
- Sometimes it will be necessary to put the scan or process we just started in the background to continue using the current session to interact with the system or start other processes. As we have already seen, we can do this with the shortcut `[Ctrl + Z]`. As mentioned above, we send the `SIGTSTP` signal to the kernel, which suspends the process.
- knk mesela bir yere ping atıyorsun ctrl z yaptığın zaman bu sursuruluyor sen ` jobs` yazarsen terminale neleri durdurduğunu falan görebilirsin. kısaca bu komutlar suspend edilir sonra çalıştırılmaz ama sen bunun arka planda çalışmasını istersen ` bg` komutunu kullanarak bunu arka plana koyabilirsin. 
- başak bir seçenek ise sona & işareti koymak bunun sayesinde o komut bittiği zaman galiba gereksiz şeyleri görmeyiz ve sadece sonucu gösterir.


# Foreground a Process:
- After that, we can use the `jobs` command to list all background processes. Backgrounded processes do not require user interaction, and we can use the same shell session without waiting until the process finishes first. Once the scan or process finishes its work, we will get notified by the terminal that the process is finished.
- eğer arka plana koyduğun bir şeyi tekrar öne almak istiyorsan ` fg <ID>` yaparak alabilirsin.

# Execute Multiple Commands:
- knk bunlar Semicolon (;), (&&) ve (|).
- knk bunlar arasındaki fark processin başarılı başarısız tamamşanıp tamamlanmasına bağlı.
- Bu semicolon öncesindeki komutta hata olup olmasına bakmadım çalıştırır. Ardı ardına bir komut hata verse bile rahat şekilde çalıştırır. Usage: `echo '1'; ls MISSING_FILE; echo '3'` However, (&&) ise eğer bir komut hata verirse ondan sonrakileri çalıştırmaz. Usage: ` echo '1' && ls MISSING_FILE && echo '3'` 
- Pipes (`|`) depend not only on the correct and error-free operation of the previous processes but also on the previous processes' results.
