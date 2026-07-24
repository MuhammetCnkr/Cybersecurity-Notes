**Topic:**  

# Main Directories:
- Linux'ta her şey file haldedir. Mesela ls'in kendisi bir filedır.
- bin : bu ana dizinde olan binary'e stand eden. İçinde sistem tool dosyalarını barından bir dosya. i.e. ls, cp, rm
- sbin : Bu da ana dizinde olan bin'e benzeyen ama superbin olduğu için adminlerin kullandığı komutları barındırır. i.e. adduser
- usr: İçinde bin sbin vs çoğu şeyi ana dizinde olduğu gibi bulundurur. Sebebi     .
- boot: İçinde boot dosyaları var.
- tmp: Temprorary dosyalar var içinde.
- var: log files and also web application related files
- lib: more shared library files your system needs to boot
- home: where we live users live
- root: 
- dev: stands for devices. İçinde senin driverların disklerin falan olabilir. Vda or Vda1 stands for virtual disk, Sda or Sda1 stands for fiziksel disk. ve bu arada bunlar da file şeklinde 
- etc: stands for etcetera, etsy. içinde senin sistem ayarların netweok ayarların  falan bulunur.

# Commands:
```js
`whoami`: tell us who we are logged in as

`\`: The root of file system

`clear`: Cleans your currently terminal windows. Aynı zamanda control+l yaparak da silebilirisin.

`cat`: Stands for Concatenate. Dosyalardakileri okumanı falan sağlar. Usage: cat *nameoffile* 

`cp`: Copy command. Usage: cp *eskidosya yenidosya* 

`sudo`: Root veya admin olarak işlem yapmanı sağlar.

`rm`: Stands for remove. Usage: rm *filename*

`adduser`: Bu komut sayesinde yeni user eklersin. Usage: adduser supermc. Since it is in sbin, you have to be admin. Btw users which you added are in the /home directory.
`which`: Kullandığın komuttun kime ait olduğunu söyler /usr/bin or /bin gibi. Usage: which ls
``` 
