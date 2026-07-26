
**Date:** 26-07-2026
**Tags:** 

# Definition:
- A file descriptor (`FD`) in Unix/Linux operating systems is a reference, maintained by the kernel, that allows the system to manage Input/Output (`I/O`) operations. It acts as a unique identifier for an open file, socket, or any other I/O resource. In Windows-based operating systems, this is known as a file handle. Essentially, the file descriptor is the system's way of keeping track of active `I/O` connections, such as reading from or writing to a file.
- By default, the first three file descriptors in Linux are:
1. Data Stream for Input `STDIN - 0` 
2. Data Stream for Output `STDOUT - 1` 
3. Data Stream for Output that relates to an error occurring `STDERR - 2` 

# Redirect STDOUT to a File
- Now we can see that all errors (`STDERR`) previously presented with "`Permission denied`" are no longer displayed. The only result we see now is the standard output (`STDOUT`), which we can also redirect to a file with the name `results.txt` that will only contain standard output without the standard errors.
- `find /etc/ -name shadow 2>/dev/null > results.txt` knk böyle yaptığın zaman senin aldığın permission denied hatası karşına çıkmayacak sen onu redirect etmiş oldun ve onu /dev/null'a yolladın ve geriye kalanları ise yani temiz çıktıyı ise results.txt'ye yolladın.
- We should have noticed that we did not use a number before the greater-than sign (`>`) in the last example. That is because we redirected all the standard errors to the "`null device`" before, and the only output we get is the standard output (`FD 1 - STDOUT`). To make this more precise, we will redirect standard error (`FD 2 - STDERR`) and standard output (`FD 1 - STDOUT`) to different files.
- `find /etc/ -name shadow 2> stderr.txt 1> stdout.txt` knk böyle yaparsan senin hataların yani ikilerin stderr.txt'ye gider geri kalanlar ise yani birler ise stdout.txt'ye gider. Cat ile bunları okuyabilirsin
- **Redirect STDIN:** As we have already seen, in combination with the file descriptors, we can redirect errors and output with greater-than character (`>`). This also works with the lower-than sign (`<`). However, the lower-than sign serves as standard input (`FD 0 - STDIN`). These characters can be seen as "`direction`" in the form of an arrow that tells us "`from where`" and "`where to`" the data should be redirected. We use the `cat` command to use the contents of the file "`stdout.txt`" as `STDIN`.
- `cat < stdout.txt` 
- **Redirect STDOUT and Append to a File:** When we use the greater-than sign (`>`) to redirect our `STDOUT`, a new file is automatically created if it does not already exist. If this file exists, it will be overwritten without asking for confirmation. If we want to append `STDOUT` to our existing file, we can use the double greater-than sign (`>>`).
- `find /etc/ -name passwd >> stdout.txt 2>/dev/null` 
- **Redirect STDIN Stream to a File:** We can also use the double lower-than characters (`<<`) to add our standard input through a stream. We can use the so-called `End-Of-File` (`EOF`) function of a Linux system file, which defines the input's end. In the next example, we will use the `cat` command to read our streaming input through the stream and direct it to a file called "`stream.txt`."
- `cat << EOF > stream.txt` knk galiba burada senin stream de birkaç yazı var sen bunu okumak istiyorsun ama okurken birkaç şey daha eklemek istiyorsun burada senin eklediğin şey EOF bu en sona ekleniyor sen bu komutu bastığın zaman

# Pipes:
- Another way to redirect `STDOUT` is to use pipes (`|`). These are useful when we want to use the `STDOUT` from one program to be processed by another. One of the most commonly used tools is `grep`, which we will use in the next example. Grep is used to filter `STDOUT` according to the pattern we define. In the next example, we use the `find` command to search for all files in the "`/etc/`" directory with a "`.conf`" extension. Any errors are redirected to the "`null device`" (`/dev/null`). Using `grep`, we filter out the results and specify that only the lines containing the pattern "`systemd`" should be displayed.
- `find /etc/ -name *.conf 2>/dev/null | grep systemd` knk buradan çıkan sonucu grep'e veriyor o ise çıkan sonuçta systemd var mı diye bakıyor var olanları ekrana basıyor
- **ANOTHER:** The redirections work, not only once. We can use the obtained results to redirect them to another program. For the next example, we will use the tool called `wc`, which should count the total number of obtained results.
- `find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l` knk burada grep'ten çıkan sonucun kaç satır olduğunu ekrana basar.