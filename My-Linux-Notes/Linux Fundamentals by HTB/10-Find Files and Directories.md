---
Date: 2026-07-26 11:58
category:
tags:
Tools:
---
# Which:
- This tool returns the path to the file or link that should be executed. This allows us to determine if specific programs, like cURL, netcat, wget, python, gcc, are available on the operating system. knk bunun sayesinde bir program ya da dosya eğer varsa onun path'ini öğrenirsin eğer yoksa no results will be displayed
# Find:
 - **Syntax:** `find <location> <options>`
## Options:
| Opions                | Description                                                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-type f`             | Hereby, we define the type of the searched object. In this case, '`f`' stands for '`file`'.                                                                                                                                                                                    |
| `-name *.conf`        | With '`-name`', we indicate the name of the file we are looking for. The asterisk (`*`) stands for 'all' files with the '`.conf`' extension.                                                                                                                                   |
| `-user root`          | This option filters all files whose owner is the root user.                                                                                                                                                                                                                    |
| `-size +20k`          | We can then filter all the located files and specify that we only want to see the files that are larger than 20 KiB.                                                                                                                                                           |
| `-newermt 2020-03-03` | With this option, we set the date. Only files newer than the specified date will be presented.                                                                                                                                                                                 |
| `-exec ls -al {} \;`  | This option executes the specified command, using the curly brackets as placeholders for each result. The backslash escapes the next character from being interpreted by the shell because otherwise, the semicolon would terminate the command and not reach the redirection. |
| `2>/dev/null`         | This is a `STDERR` redirection to the '`null device`', which we will come back to in the next section. This redirection ensures that no errors are displayed in the terminal. This redirection must `not` be an option of the 'find' command.                                  |
- knk bu 2>/dev/null ifadesi sayesinde sana permission denield diyen şeyleri göstermesini engellersin ekran temiz kalır
- ```find / -type f -name "*.conf" -size +25k -size -28k -newermt 2020-03-03 2>/dev/null```  Bu komut için aşağıda açıklaması var
- - **`find /`**: Searches the entire file system starting from the root directory.
- **`-type f`**: Specifies that you are looking for files, not directories.
- **`-name "*.conf"`**: Filters for configuration files ending with the `.conf` extension.
- **`-size +25k -size -28k`**: Filters for files larger than 25 KB but smaller than 28 KB.
- **`-newermt 2020-03-03`**: Filters for files modified or created after March 3, 2020.
- **`2>/dev/null`**: Mutes any "Permission Denied" errors to keep your terminal output clean

# Locate:
- The command `locate` offers us a quicker way to search through the system. In contrast to the `find` command, `locate` works with a local database that contains all information about existing files and folders. We can update this database with the following command.  `sudo updatedb` 
- Eğer sadece sonu .conf ile biten bir şey arayacaksan find daha hızlı şekilde bu komutu kullanarak `locate *.conf` çok daha hızlı bir şekilde bulabilirsin. buradaki * all anlamına geliyor
- However, bu tool find kadar filter options'a sahip değil
- Find ya da Locate kullanam durumu ne aradığına göre değişir locate için sadece bulursun ama find ile tarih size her şeyi ayarlayabilirsin
