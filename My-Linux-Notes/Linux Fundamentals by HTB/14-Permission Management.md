

- Every file and directory has an owner (a user) and is associated with a group. The permissions for these files are defined for both the owner and the group, determining what actions—like reading, writing, or executing—are allowed. When you create a new file or directory, it automatically becomes "yours" and is associated with the group you belong to, similar to how a project within a company might default to your team’s oversight.

# Execute:
- In other words, having `execute` permissions on a directory is like having permission to walk through a hallway to access the rooms inside. It doesn't allow you to see or modify what's inside, but it does grant you the ability to step inside and explore the directory's structure. Without this permission, the user cannot access the directory's contents and will instead be presented with a “`Permission Denied`" error message.
- It is important to note that `execute` permissions are necessary to traverse a directory, no matter the user's level of access. Also, `execute` permissions on a directory do not allow a user to execute or modify any files or contents within the directory, only to traverse and access the content of the directory.
# Write:
- To modify the contents of a directory (create, delete, or rename files and subdirectories), the user needs `write` permissions on the directory.

![[Screenshot 2026-07-27 at 10.49.03.png]]


# Change Permissions:
- knk bunda `chmod`denen tool sayesinde bir dosya link klasör fark etmez permissionları değiştirebiliyorun. Permissions: read-write-execute (r-w-x). Bunlar için ise ilk önce şunları bil u : owner, g : group, o : others, a : all users.  eğer bir şeyin all user'unu değiştirmek istiyorsan `a`+- yaparak değiştrebilirsin. mesela bir klasör olsun sadece owner okusun diğerleri okuyamasın. sen eğer `chmod a+r <name>`yaparsan tüm herkese read verirsin eğer kaldırmak istersen oraya *-* yaz yeter.
- **Octal:** knk bunda ayarlamayı oktal sisteme göre yapıyorsun. mesela 111 7 demek, 110 6 demek, 011 3 demek. eğer sen herkesin permissionunu ayarlamak istiyorsan `chmod xxx <name>`yaparsan verdiğin x değerlerine göre sırasıyla owner group others değişir. mesela 7 yazarsan bir yere o yerdekiler read write execute yapabilirler, 0 yazarsan hiç bir şey yapamazlar, 1 yazarsan sadece execute eder. ![[Screenshot 2026-07-27 at 11.01.25.png]]

# Change Owner:
- To change the owner and/or the group assignments of a file or directory, we can use the `chown`command. The syntax is like following: `chown <user>:<group> <file/directory>`
- mesela `chown root:root <name>`yaparsan dosyanın owner ve grubunu root yaparsın

# SUID & SGID:
- In addition to standard user and group permissions, Linux allows us to configure special permissions on files through the Set User ID (`SUID`) and Set Group ID (`SGID`) bits. These bits function like temporary access passes, enabling users to run certain programs with the privileges of another user or group. For example, administrators can use `SUID` or `SGID` to grant users elevated rights for specific applications, allowing tasks to be performed with the necessary permissions, even if the user themselves doesn’t normally have them.
- The presence of these permissions is indicated by an `s` in place of the usual `x` in the file's permission set. When a program with the SUID or SGID bit set is executed, it runs with the permissions of the file's owner or group, rather than the user who launched it. This can be useful for certain system tasks but also introduces potential security risks if not used carefully.
- One common risk is when administrators, unfamiliar with an application's full functionality, assign `SUID` or `SGID` bits indiscriminately. For example, if the `SUID` bit is applied to a program like `journalctl`, which includes a function to launch a shell from within its interface, any user running this program could execute a shell as root. This grants them complete control over the system, presenting a significant security vulnerability. More information about this and other such applications can be found at [GTFObins](https://gtfobins.github.io/gtfobins/journalctl/).

# Sticky Bit:
- Sticky bits in Linux are like locks on files within shared spaces. When set on a directory, the sticky bit adds an extra layer of security, ensuring that only certain individuals can modify or delete files, even if others have access to the directory.
- Imagine a communal workspace where many people can enter and use the same tools, but each person has their own drawer that only they (or the manager) can open. The sticky bit acts like a lock on these drawers, preventing anyone else from tampering with the contents. In a shared directory, this means only the file's owner, the directory's owner, or the root user (the system administrator) can delete or rename files. Other users can still access the directory but can’t modify files they don’t own.
- This feature is especially useful in shared environments, like public directories, where multiple users are working together. By setting the sticky bit, you ensure that important files aren’t accidentally or maliciously altered by someone who shouldn’t have the authority to do so, adding an important safeguard to collaborative workspaces.
 - ```zsh
drw-rw-r-t 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:30 scripts
drw-rw-r-T 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:32 reports
```
In this example, we see that both directories have the sticky bit set. However, the `reports`folder has an uppercase `T`, and the `scripts` folder has a lowercase `t`. If the sticky bit is capitalized (`T`), then this means that all other users do not have `execute` (`x`) permissions and, therefore, cannot see the contents of the folder nor run any programs from it. The lowercase sticky bit (`t`) is the sticky bit where the `execute` (`x`) permissions have been set.
