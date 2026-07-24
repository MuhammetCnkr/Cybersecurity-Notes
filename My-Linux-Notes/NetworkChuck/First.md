# Nmap Port Taraması Rehberi
**Kategori:** #tools #networking
**Tarih:** 2026-07-22

## Temel Mantık
Nmap, ağdaki açık portları ve çalışan servisleri tespit etmek için kullanılır.

## En Çok Kullanılan Komut
```bash
nmap -sC -sV -p- -oN scan_results.txt <TARGET_IP>
```

### Parametre Detayları:
- `-sC`: Varsayılan güvenlik script'lerini çalıştırır.
- `-sV`: Servis versiyonlarını tespit eder.
- `-p-`: 1'den 65535'e kadar **tüm** portları tarar.
- `-oN`: Çıktıyı normal metin dosyası olarak kaydeder.

## İlgili Konular
- Bağlantılı Not: [[TCP-3-Way-Handshake]]