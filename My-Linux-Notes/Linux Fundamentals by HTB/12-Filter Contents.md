---
Date: 2026-07-26 15:13
category:
tags:
Tools:
---
**Intro:** There are two powerful tools for this - `more` and `less`. These are known as pagers, and they allow you to view the contents of a file interactively, one screen at a time. While both tools serve a similar purpose, they have some differences in functionality, which we'll touch on later.

**Purpose:** The goal for this section is to learn how to filter content and handle the redirected output from previous commands. But before we dive into filtering, we need to become familiar with some essential tools and commands that are specifically designed to make filtering more efficient and powerful.

# Usernames:
- In Unix-like operating systems, the /etc/passwd file is a text-database that stores essential information about user accounts such as their username, groups, home directory, and more. To get the full list of users registered on the system, you can display this file using the cat command as follows: `cat /etc/passwd`
- Each line of the /etc/passwd file defines a user account and consists of 7 fields separated by colons (:):  `username:password:uid:gid:description:home:shell`
1. username is the name of the user account.
2. password is the password of the user account, which is usually displayed as an x for security reasons. Note that the actual password is stored in the /etc/shadow file.
3. uid or user ID is a unique numerical identifier assigned to each user.
4. gid or group ID is the numerical identifier of the user’s primary group.
5. description is an optional string providing additional information about the user like their full name or contact information.
6. home is the path of the user's home directory (e.g., /home/johndoe).
7. shell is the path of the user’s default login shell (e.g., /bin/bash, /bin/zsh).

# Commands:
# Base64:
- knk bu adam sayesinde base64 ile şifrelenmiş dosya veya texti normal hale getirirsin. Bunun için `base64 -d data.txt` kullanman yeterli buradaki -d decode anlamına geliyor
## More:
- Bu ve less genelde ya başlangıca bakmak ya da sona bakmak için kullanılır dosyanın
- The `/etc/passwd` file in Linux is like a phone directory for users on the system. It includes details such as the username, user ID, group ID, home directory, and the default shell they use. For this `cat /etc/passwd | more`
- After we read the content using `cat` and redirected it to `more`, the already mentioned `pager` opens, and we will automatically start at the beginning of the file.
- `q`ya basarak bu pager'dan ayrılabilirsin
## Less:
- Bu arkadaş *more* dan daha fazla özelliğe sahip eğer man page'e bakarsan
- Bu arkadaş sana *more* ile benzer bir çıktı verir. Usage: `less /etc/passwd`
- Bunda da *q* kullanarak kapatabilirsin bunda more'un aksine gördüğün output terminalde kalmaya devam etmeyecek sen more'da çıksan bile çıktı still orada olur ama bunda yok kardeş temporary
## Head:
- Bu arkadaş sayedinde by default file'ın ilk 10 satırını verir ama sen ilk satırını falan görmek istersen ayarlamalar yapabilirsin. Usage: `head /etc/passwd`

## Tail: 
- Bu arkadaş ise *head* in tam tersi ilk 10 değil son 10 satırı sana basar. Usage: `tail /etc/passwd` 

## Sort:
- Bu arkadaş sayesinde çıktıyı numerically or alphabetically sıralama yapabiliriz. Usage: `cat /etc/passwd | sort`

## Grep:
- Bu arkadaşla mesela ilk olarak çıkan çıktıda istediğin bir şey varsa onu basmasını ayarlayabilirsin. Usage: `cat /etc/passwd | grep "/bin/bash"`burada çıktıda sadece /bin/bash ifadesi olanlar olacak
- This is just one example of how grep can be applied to efficiently filter data based on predefined patterns. Another possibility is to exclude specific results. For this, the option "`-v`" is used with `grep`. In the next example, we exclude all users who have disabled the standard shell with the name "`/bin/false`" or "`/usr/bin/nologin`".
- For this: `vat /etc/passwd | grep -v "false\|nologin"` knk `\|`or anlamına geliyor
- knk bir sembol aramak istiyorun mesela = bu olsun bundan kaç tane var bilmiyorun arka arkaya sen o satırı bulmak için `| grep -E "\={2,}"`bu sayede min 2 adet = içeren satırları gösterecek. `| grep -E "\=+"`birden fazla içerenleri arka arkaya gösterecek

## Cut:
- Specific results with different characters may be separated as delimiters. Here it is handy to know how to remove specific delimiters and show the words on a line in a specified position. One of the tools that can be used for this is `cut`. Therefore we use the option "`-d`" and set the delimiter to the colon character (`:`) and define with the option "`-f`" the position in the line we want to output.
- Usage: `cat /etc/passwd | grep -v "false\|nologin" | cut -d":"-f1`. Aşağıda roottan sonra mesela : var ondan sonrasını kesti ve ekrana öyle bastı
- ```
root
sync
postgres
mrb3n
cry0l1t3
htb-student
```

## Tr:
- Another possibility to replace certain characters from a line with characters defined by us is the tool `tr`. As the first option, we define which character we want to replace, and as a second option, we define the character we want to replace it with. In the next example, we replace the colon character with space.
- Usage: `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " "` burada iki noktayı boşlukla replace etti

## Column:
- Since search results can often have an unclear representation, the tool `column` is well suited to display such results in tabular form using the "`-t`."
- Usage: `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | column -t` burada t sayesinde tabular form diye belirtik o da tablo benzeri bir şey verdi. dene de gör

## Awk:
- As we may have noticed, the line for the user "`postgres`" has one column too many. To keep it as simple as possible to sort out such results, the (`g`)`awk` programming is beneficial, which allows us to display the first (`$1`) and last (`$NF`) result of the line.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'`  ```root /bin/bash sync /bin/sync postgres /bin/bash mrb3n /bin/bash cry0l1t3 /bin/bash htb-student /bin/bash``` bunlar satır satır burada yapamadım idare et

## Sed:
- The "`s`" flag at the beginning stands for the substitute command. Then we specify the pattern we want to replace. After the slash (`/`), we enter the pattern we want to use as a replacement in the third position. Finally, we use the "`g`" flag, which stands for replacing all matches.
- Usage: ```
```
Muhammetcnkr@htb[/htb]$ cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'

root /HTB/bash
sync /HTB/sync
postgres /HTB/bash
mrb3n /HTB/bash
cry0l1t3 /HTB/bash
htb-student /HTB/bash
```

## Wc:
- Last but not least, it will often be useful to know how many successful matches we have. To avoid counting the lines or characters manually, we can use the tool `wc`. With the "`-l`" option, we specify that only the lines are counted.
- kullanmayı biliyorsun

## Ss:
- The ss command (Socket Statistics) is an important Linux utility used to display detailed information about network sockets. It helps analyze network connections, monitor open ports and troubleshoot connectivity issues efficiently. The command provides details about TCP, UDP and other socket types, including their states and associated processes. Due to its speed and efficiency, it is widely used as a modern replacement for [netstat](https://www.geeksforgeeks.org/linux-unix/netstat-command-linux/).
- knk bu baya işe yarayan bir şey -l ile ilstening yapanları -4 ile ipv4 olanları falan ayarlayabiliyorsun.



# Sort ve Uniq Kullanımı(bandit):
- knk senin elinde çok uzun bir log dosyası var sen bir defa geçen satırı bulmak istiyorsun bunun için `sort data.txt | uniq -c` yaparsan ilk önce tüm herşeyi alfabatik v.s. sıralamasını yapar bu kısım çok önemli çünkü uniq -c arka arkaya gelen aynı satırları sayabiliyor. Bundan sonra uniq -c aynı olan satırların kaç tane olduğunu başında sayı ve ardında satırı verir sana.
- Bundan sonra belki sen bazı satırlardan 10 tane bazılarından 2 tane bazılarından 1 tane olduğunu görebilirsin eğer sen bundan sonra pipe yapıp grep'e verip sadece 1 olanı bul dersen elinde şifrenin içinde 1 olan da olabilir ya da tekrar sayısında 1 olanda olabilir bu durumda çıkmaz sokak
- bundan sonra devreye regex giriyor tam bu sorunu çözmek için ` | grep -E '^ *1 '` kullanman lazım bu şu anlama geliyor şapka: satırın başından bak arana ifade satırın başında olmalı. * : knk bu işaret kendinden önceki karakterin sıfır ya da daha fazla kez tekrarlanmış olabileceğini söyler mesela bu durumda ondan önce space var yani satırın başında boşluk olada bilir omayada bilir anlımda. 1 : knk bu ise satırda tam 1 rakamını arar. birden sonraki boşluk ise 1 den sonra bir tane boşluk olması demek bunun sayesinde 10 101 sayılarını falan eliyorsun ve sadece 1 adet olan satırı elde ediyorsun

# Bandit Extra:
- ![[Screenshot 2026-07-31 at 17.16.57.png]]
- knk yukarıda sana verdiği pathleri tek tek denemek yerine cat gibi toola direkt verip hepsini ekrana basmasını sağlar.
- bak ben bandit8 çözmek için şöyle yaptım : `find / -type f -name data.txt 2>/dev/null | grep -v "bandit7" | xargs cat` böyle yaptım bu sayede diğer pathlerde yani bandit7 olmayan yerlerdeki dosyaların okunup okunmadığını hemen gördüm baktım sonra bandit8 okunmuş. ` sort /home/bandit8/data.txt | uniq -c | grep -E "^ *1 "`yaptım ve cevabı aldım.


# Strings:
- knk bu adam sayesinde binary dosyada geçen human readable stringleri bulabiliyorsun. ` strings data.txt` yaparsan sana gösterir