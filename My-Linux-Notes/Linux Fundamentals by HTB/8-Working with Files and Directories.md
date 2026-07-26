
**Date:** 25-07-2026
**Tags:** 

**regex:** regular expressions. Bu bir komut değil genel bir kısaltma.

# Creating:
- create a file use `touch <name>` i.e touch info.txt it is an empty file btw.
- create a directory use `mkdir <name>` i.e mkdir storage.
- When organizing your system, you may need to create multiple directories within other directories. Manually running the `mkdir` command for each one would be time-consuming. Fortunately, the mkdir command has the `-p` (parents) option, which allows you to create parent directories automatically. Knk bu içi içine aynı matruşkalar gibi klasör yapıyor. i.e. `mkdir -p storage/local/user/documents`
- Bak böyle bir şey yaptın ya sonra eserini görmek istediğin bu katman katman olun için *tree* denen bir tool var. kullanmak için `tree .`yap sana bulunduğun yerden sonraki içindeki yerleri gösterir ve kac direc var kac file var yazar
- Btw you can create a file or directory where you want for this you can use `touch or mkdir /path`işte knk
# move and rename:
- for rename `mv <file/directory> <renamed file/directory>`. mesela if you want info to new_info you use mv info.txt new_info.txt 
- multiple move for this mv things1 things 2 ... where you want for this i.e. mv info.txt readme.txt /etc/aha_burada