---
category: Linux Fundamentals
source: HTB Academy notes
status: enhanced
tags:
  - linux
  - htb
  - study-note
---
# 20-Working with Web Services

> [!abstract] Öğrenme hedefi
> Apache modüllerini, sanal hostları, logları ve HTTP testini bir araya getirmek.

## Hızlı özet

- Bu notu çalışırken “komut ne yapıyor?” kadar “hangi veri akışını veya sistem katmanını etkiliyor?” sorusunu da sor.
- Komutları ezberlemek yerine küçük bir lab ortamında `man`, `--help` ve gözlem komutlarıyla doğrula.

## Düzeltmeler ve önemli nüanslar

- Apache “web sitesinin motoru” benzetmesi yararlıdır ama Apache bir HTTP sunucusudur; uygulama mantığı ayrı bir runtime/uygulama sunucusunda olabilir.
- `mod_ssl` TLS desteği sağlar; güvenlik yalnızca modülü açmakla tamamlanmaz, sertifika ve protokol ayarları gerekir.
- `mod_proxy` reverse/forward proxy yetenekleri sunar; erişim kontrolleri yanlışsa ciddi risk doğurabilir.

## Eksik kalabilecek kavramlar

- virtual host
- `a2enmod`/`a2ensite`
- `apache2ctl configtest`
- access/error log
- `curl -I`

## Bilişsel bağlantılar

[[19-Network Services|Ağ servisleri]] · [[16-Package Management|Paket kurulumu]]

## Aktif tekrar / mini lab

```bash
`apache2ctl configtest; systemctl status apache2; curl -I http://127.0.0.1` (yalnızca kendi lab sisteminde).
```

> [!warning] Güvenli çalışma
> `sudo`, izin değişikliği, servis, kullanıcı ve ağ komutlarını yalnızca kendi lab/HTB ortamında çalıştır. Üretim veya başkasına ait sistemlerde deneme.

---

## Korunan özgün not

> Aşağıdaki bölüm kaynak notun kopyasıdır. Orijinal klasördeki dosyaya dokunulmamıştır; yukarıdaki bölüm doğrulama ve öğrenme katmanıdır.

- Think of Apache as the engine that powers your website, ensuring smooth communication between your website and visitors.

- Apache's true strength lies in its modularity—it can be customized and extended with various modules to perform specific tasks. For example, `mod_ssl` acts like a lockbox, securing the communication between the browser and the web server by encrypting the data. The `mod_proxy` module is like a traffic controller, directing requests to the correct destination, especially useful when setting up proxy servers. Other modules such as `mod_headers` and `mod_rewrite` give you fine control over the data traveling between browser and server, allowing you to modify HTTP headers and URLs on the fly, like adjusting the course of a stream.

- **Installation:** `sudo apt install apache2 -y` yardımıyla indirme yapabilirsin
- 
