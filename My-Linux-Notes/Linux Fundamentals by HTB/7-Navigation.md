
**Date:** 25-07-2026
**Tags:** 

**pwd:** Print Working Directory. It shows which directory you are

# ls:
## `-l`:
- Using it without any additional options will display the directories and files only. However, we can also add the `-l` option to display more information on those directories and files.
- İlk görüdüğün şey total 32 mesela 32 Kb yer kaplıyor oradaki tüm dosyalar. Aslında bu 32 blocks demek her block ise 1024 bytes
- |`drwxr-xr-x`|Type and permissions|
- |`2`|Number of hard links to the file/directory|
- |`cry0l1t3`|Owner of the file/directory|
- |`htbacademy`|Group owner of the file/directory|
- |`4096`|Size of the file or the number of blocks used to store the directory information|
- |`Nov 13 17:37`|Date and time|
- |`Desktop`|Directory name|
## `-la`:
- However, we will not see everything that is in this folder. A directory can also have hidden files that start with a dot at the beginning of its name (e.g., `.bashrc` or `.bash_history`). Therefore, we need to use the command `ls -la` to `list all` files of a directory:
- bu ls toolunda sen ls /var/mail yazarsan oraya navigate etmene gerek kalmadan oradakileri show edersin
- 