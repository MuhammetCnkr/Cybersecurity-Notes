---
Date: 2026-07-31 17:45
category:
tags:
Tools:
---
- **Rot13:** knk bu bir şifreleme yöntemi özellikle ingilizce alfabede kullanılan çünkü 26 harf var olayı bir harfi kendisinden sonra gelen 13. harf ile replace ediyor.
- ![[Screenshot 2026-07-31 at 17.49.27.png]]
- knk tr toolunda böyle şeyler için çevirme olayı var.


# Bandit13:
- Eğer elinde bir openssh private key varsa onu düzgün bir şekilde bir dosyaya kaydederek ve sonrasında chmod 600 yapman lazım. Ardından bu private key ile bağlanmak istersen ssh -i sshprivate_key user_name@ip_address -p <port> ile giriş yapabilirsin. 
- uzaktaki remote bir cihazdan bir belgeyi lokale çekmek için kopyalamak için scp denen bir şey kullanıyoruz scp -P <port> remote_username@remote_ip:/home/dosya /root(local yer burası).     ``scp -P <port> <user>@<IP>:<remotefilepath> <localfilepath>``    


diff pass.new pass.old aradaki farklı line'ı ekrana yazar