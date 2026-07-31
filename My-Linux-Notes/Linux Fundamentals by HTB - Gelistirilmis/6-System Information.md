---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 6-System Information

> [!abstract] Öğrenme hedefi
> Kimlik, donanım, ağ ve süreç bilgisini doğru araçla toplamak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `hostname` argümansız adı gösterir; ad değiştirmek ayrı ve yetkili bir işlemdir.
- `ifconfig` ve `netstat` eski net-tools paketindendir; güncel karşılıklar çoğunlukla `ip` ve `ss` komutlarıdır.
- `uname -a` alanları dağıtıma göre değişebilir; dağıtım bilgisi için `/etc/os-release` daha uygundur.

## Eksik kalabilecek kavramlar

- `ip addr`, `ip route`, `ss -tulpn`
- `ps aux` ve `/proc`
- yetki bağlamı için `id`

## Bilişsel bağlantılar

[[17-Service and Process Management|Süreç ve servisler]] · [[19-Network Services|Ağ servisleri]]

## Aktif tekrar / mini lab

```bash
`id; uname -r; cat /etc/os-release; ip -brief addr; ss -lntup` ile mini sistem envanteri çıkar.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

# Commands:

| `whoami`   | Displays current username. In windows and linux                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `id`       | Returns users identity                                                                                                             |
| `hostname` | Sets or prints the name of current host system.                                                                                    |
| `uname`    | Prints basic information about the operating system name and system hardware.                                                      |
| `pwd`      | Returns working directory name.                                                                                                    |
| `ifconfig` | The ifconfig utility is used to assign or to view an address to a network interface and/or configure network interface parameters. |
| `ip`       | Ip is a utility to show or manipulate routing, network devices, interfaces and tunnels.                                            |
| `netstat`  | Shows network status.                                                                                                              |
| `ss`       | Another utility to investigate sockets.                                                                                            |
| `ps`       | Shows process status.                                                                                                              |
| `who`      | Displays who is logged in.                                                                                                         |
| `env`      | Prints environment or sets and executes command.                                                                                   |
| `lsblk`    | Lists block devices.                                                                                                               |
| `lsusb`    | Lists USB devices                                                                                                                  |
| `lsof`     | Lists opened files.                                                                                                                |
| `lspci`    | List PCI devices.                                                                                                                  |
- **uname:** uname -a : kernel-name -s, nodename -s, kernel-release -v, machine -m, processor -p, hardware-platform -i, operating-system -o bunların hepsini ekrana yazdırır
- **uname -r:** Suppose we want to print out the kernel release to search for potential kernel exploits quickly.
