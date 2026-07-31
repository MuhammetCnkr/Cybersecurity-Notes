---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 4-Prompt Description

> [!abstract] Öğrenme hedefi
> Shell promptunun kullanıcı, makine, konum ve yetki bilgisini okumak.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- `$` normal kullanıcıyı, `#` genellikle root kullanıcısını gösterir; “dash” değildir.
- PS1 yalnızca görüntülenen prompt biçimidir; yetki vermez ve değiştirilmesi kullanıcıyı root yapmaz.

## Eksik kalabilecek kavramlar

- PS1 kaçış dizileri (`\u`, `\h`, `\w`)
- exit status için `$?`
- environment variable kavramı

## Bilişsel bağlantılar

[[1-Intro|Shell nedir?]] · [[6-System Information|Kimlik ve sistem bilgisi]]

## Aktif tekrar / mini lab

```bash
`echo "$PS1"; printf "%s\n" "$USER" "$HOSTNAME" "$PWD"` çalıştır ve prompt parçalarıyla eşleştir.
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

**means**: `<username>@<hostname><current working directory>$`  Bunu istediğin gibi ayarlayabilirsin. Bunun için **bash prompt generator** gibi şeylere bak.
1. The home directory for a user is marked with a tilde <`~`> and is the default folder when we log in.
2. The dollar sign, in this case, stands for a user. As soon as we log in as `root`, the character changes to a `hash` <`#`> and looks like this: `root@htb[/htb]#`

# PS1 Variable:
- dolar : unprivileged - User Shell Prompt
- dash : Privilged - Root Shell Prompt

