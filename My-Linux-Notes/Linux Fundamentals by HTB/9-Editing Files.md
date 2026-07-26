
**Date:** 26-07-2026
**Tags:** 

# Nano:
- to create and open a new file named `notes.txt` for this `nano notes.txt`
- Nano’s straightforward interface (also called "`pager`")
- Bunun kendi içinde kısayolları var zaten onlarda bunu açınca alt tarafta yazıyor ^ctrl anlamına geliyor
# Cat:
- bu arkadaş sayesinde galiba sadece read yapabiliyoruz.
- **extra:** /etc/passwd burada senin password hashes ve bu hasheslarda genelde /etc/shadow da eğerki bunlara erişebilirsen passwordları kolaylıkla geçersin. (*privilege esclation opportunities*)
# Vim:
- It is open-source editor for all kind off ASCII text, just like Nana.
- When we have the Vim editor open, we can go into command mode by typing "`:`" and then typing "`q`" to close Vim.
- Vim offers an excellent opportunity called `vimtutor` to practice and get familiar with the editor. Bu adam galiba sana vim kullanmayı öğretiyor gibi.
## Modes of Vim:
- |`Normal`|In normal mode, all inputs are considered as editor commands. So there is no insertion of the entered characters into the editor buffer, as is the case with most other editors. After starting the editor, we are usually in the normal mode.|
- |`Insert`|With a few exceptions, all entered characters are inserted into the buffer.|
- |`Visual`|The visual mode is used to mark a contiguous part of the text, which will be visually highlighted. By positioning the cursor, we change the selected area. The highlighted area can then be edited in various ways, such as deleting, copying, or replacing it.|
- |`Command`|It allows us to enter single-line commands at the bottom of the editor. This can be used for sorting, replacing text sections, or deleting them, for example.|
- |`Replace`|In replace mode, the newly entered text will overwrite existing text characters unless there are no more old characters at the current cursor position. Then the newly entered text will be added.|
- |`Ex`|Emulates the behavior of the text editor [Ex](https://man7.org/linux/man-pages/man1/ex.1p.html), one of the predecessors of `Vim`. Provides a mode where we can execute multiple commands sequentially without returning to Normal mode after each command.|
# My Vimtutor Notes: knk baya uzun ben şimdi bunu geçtim yaz bunu aklına
- sağ-sol-yukarı-aşağı için respectively l-h-k-j
- çıkış yapmak için bunu `:q!`yaz ve enter'a bas
- 