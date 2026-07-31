---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 15-User Management

> [!abstract] Öğrenme hedefi
> Kullanıcı, grup, UID/GID ve hesap yaşam döngüsünü yönetmek.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `useradd` düşük seviyeli ve dağıtıma göre varsayımları değişen bir araçtır; Debian/Ubuntu’da `adduser` etkileşimli sarmalayıcıdır.
- Kullanıcı silmek home dizinini otomatik silmeyebilir; `userdel -r` etkisi dikkatle değerlendirilmelidir.
- Grup üyeliği değişikliği mevcut oturuma hemen yansımayabilir.

## Eksik kalabilecek kavramlar

- `/etc/passwd`, `/etc/shadow`, `/etc/group`
- primary vs supplementary group
- account locking

## Bilişsel bağlantılar

[[14-Permission Management|İzinler]] · [[6-System Information|id/who]]

## Aktif tekrar / mini lab

```bash
`id; getent passwd "$USER"; getent group | grep -F "$USER"` ile mevcut kimliği incele.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

- The `/etc/shadow` file is a critical system file that stores encrypted password information for all user accounts. For security reasons, it is readable and writable only by the root user to prevent unauthorized access to sensitive authentication data.
# Sudo:
- To perform tasks that require elevated privileges, users can utilize the `sudo` command. The `sudo` command, short for "superuser do," allows permitted users to execute commands with the security privileges of another user, typically the superuser or root. This enables users to perform administrative tasks without logging in as the root user, which is a best practice for maintaining system security. We will explore sudo permissions in greater detail in the `Linux Security`section.

|**Command**|**Description**|
|---|---|
|`sudo`|Execute command as a different user.|
|`su`|The `su` utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed.|
|`useradd`|Creates a new user or update default new user information.|
|`userdel`|Deletes a user account and related files.|
|`usermod`|Modifies a user account.|
|`addgroup`|Adds a group to the system.|
|`delgroup`|Removes a group from the system.|
|`passwd`|Changes user password.|

# Su:
- To run a command as the target user without starting an interactive shell, use the `-c`, `--command` option. For example, to invoke the [`ps`](https://linuxize.com/post/ps-command-in-linux/) command as root: `su -c "whoami" tyrion` `su -c "ps aux"` 
