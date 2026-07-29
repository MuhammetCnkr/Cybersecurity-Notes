---
Date: 2026-07-27 12:04
category:
tags:
Tools:
---
# What is package:
- Packages are archives that contain binaries of software, configuration files, information about dependencies and keep track of updates and upgrades. The features that most package management systems provide are:
1. Package downloading
2. Dependency resolution
3. A standard binary package format
4. Common installation and configuration locations
5. Additional system-related configuration and functionality
6. Quality control

| **Command** | **Description**                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dpkg`      | The `dpkg` is a tool to install, build, remove, and manage Debian packages. The primary and more user-friendly front-end for `dpkg` is aptitude.                                                                                                                                                                                                        |
| `apt`       | Apt provides a high-level command-line interface for the package management system.                                                                                                                                                                                                                                                                     |
| `aptitude`  | Aptitude is an alternative to apt and is a high-level interface to the package manager.                                                                                                                                                                                                                                                                 |
| `snap`      | Install, configure, refresh, and remove snap packages. Snaps enable the secure distribution of the latest apps and utilities for the cloud, servers, desktops, and the internet of things.                                                                                                                                                              |
| `gem`       | Gem is the front-end to RubyGems, the standard package manager for Ruby.                                                                                                                                                                                                                                                                                |
| `pip`       | Pip is a Python package installer recommended for installing Python packages that are not available in the Debian archive. It can work with version control repositories (currently only Git, Mercurial, and Bazaar repositories), logs output extensively, and prevents partial installs by downloading all requirements before starting installation. |
| `git`       | Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.                                                                                                                                                                                  |


# Advanced Package Manager (APT):
- Debian tabanlı linuxlar apt package manage kullanır. knk bir paket aslında bir dosya arşivi ve bu dosya baya .deb uzantılı dosyalar içeriyor. Normalde dpkg ile bunları indirebilirsin. Ama bazı programlar bazen başka programların olmasını grektiridiği için baya bir meşekat var dpkg ile indirmekt etam bu sırada bizim apt devreye giriyor ve hangi paketi indireceksen onun iççin lazım olan diğer paketleri de (dependencies) indiriyor.
- Knk her bir linux distrosu software repositories kullanıyorlar ve bunları sıklıkla güncelliyorlar. Bazı şeyleri stable, testing, unstable olarak etiketlemesini yapıyorlar. Çoğu linux distrosu bu stable repositoryleri kullanıyorlar.` /etc/apt/sources.list`  adressine gideren burada göreceksin tavsiye ederim.
- APT uses a database called the APT cache. This is used to provide information about packages installed on our system offline. We can search the APT cache, for example, to find all `Impacket`related packages. Usage: `apt-cache search impacket`
- Daha fazla şeyler görmek istersen : ` apt-cache show impacket-scripts` 
- Ve ayrıca tüm installed packages listeleyebilirsin: ` apt list --installed` 
- If we are missing some packages, we can search for it and install it using the following command: `sudo apt install impacket-scripts -y` 

# Git:
- Knk githubtan yararlı tooları kullanmak için bunu kullanıyorsun. Bunun için ise ilk önce kullanmak istediğin toolun repositorisnin linkini kopyala. Sonra ve bir particular folder aç bunun için bu önerilir i.e `mkdir /root/nishang`. Sonra ise `git clone <link>` yap ve iş bitti

# DPKG:
- We can also download the programs and tools from the repositories separately. In this example, we download 'strace' for Ubuntu 18.04 LTS.
- knk adam bunun için ilk önce sadece `wget`yapmış sonrasında ise strace inmiş tam anlamadım bu nasıl oldu.
- Knk dpkg ile strace kurma işi şöyle : `sudo dpkg -i strace_xxx.deb`bunu yapıyorsun bu arkadaş sana kurup veriyor.

# Starce:
- bu arkadaş güçlü bir linux diagnostic tool knk. eğerki bir uygulama debugging yaşıyorsan bunun sayesinde program donmuş mu çökmüş mü anlıyorsun. kaynak koda sahip olup olmadı falan işte.
