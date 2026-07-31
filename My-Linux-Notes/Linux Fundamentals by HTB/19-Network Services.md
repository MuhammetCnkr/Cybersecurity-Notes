---
Date: 2026-07-31 15:20
category:
tags:
Tools:
---
- While it is not feasible to cover every network service, we will focus on the most important ones. This approach is beneficial not only for administrators and users, but also for penetration testers who need to understand the interactions between different hosts and their own systems.

# SSH:
- Secure Shell (`SSH`) is a network protocol that allows the secure transmission of data and commands over a network. It is widely used to securely manage remote systems and securely access remote systems to execute commands or transfer files. In order to connect to our or a remote Linux host via SSH, a corresponding SSH server must be available and running.
- knk en fazla kullanılan ssh server openssh hem ücretsiz hem açık kaynak kodlu
- Administrators use OpenSSH to securely manage remote systems by establishing an encrypted connection to a remote host. With OpenSSH, administrators can execute commands on remote systems, securely transfer files, and establish a secure remote connection without the transmission of data and commands being intercepted by third parties.
- **Install OpenSSH:** `apt install openssh-server -y` knk bunun sayesinde indirmeyi yaparsın
- **Server Status:** bu serverın çalışıp çalışmadığını `systemctl status ssh` ile kontrol edebilirsin
- **SSH - Logging In:** `ssh username@ip_address` 
- OpenSSH can be configured and customized by editing the file `/etc/ssh/sshd_config` with a text editor. Here we can adjust settings such as the maximum number of concurrent connections, the use of passwords or keys for logins, host key checking, and more. However, it is important for us to note that changes to the OpenSSH configuration file must be done carefully.

# NFS:
- Network File System (`NFS`) is a network protocol that allows us to store and manage files on remote systems as if they were stored on the local system. It enables easy and efficient management of files across networks. For example, administrators use NFS to store and manage files centrally (for Linux and Windows systems) to enable easy collaboration and management of data. For Linux, there are several NFS servers, including NFS-UTILS (`Ubuntu`), NFS-Ganesha (`Solaris`), and OpenNFS (`Redhat Linux`).
- It can also be used to share and manage resources efficiently, e.g., to replicate file systems between servers. It also offers features such as access controls, real-time file transfer, and support for multiple users accessing data simultaneously. We can use this service just like FTP in case there is no FTP client installed on the target system, or NFS is running instead of FTP.
- **Install NFS:** `apt install nfs-kernel-server -y` ardından check için `systemctl status nfs-kernel-server` 
- ![[Screenshot 2026-07-31 at 15.30.10.png]]
- **Create NFS Share:** ![[Screenshot 2026-07-31 at 15.31.12.png]]


# Web Server:
-  What is? Understanding the operation of web servers is essential for penetration testers, as these servers are integral to web applications and frequently serve as primary targets during security assessments. A web server is software that delivers data, documents, applications, and various functions over the Internet. It utilizes the Hypertext Transfer Protocol (`HTTP`) to transmit data to clients such as web browsers and to receive requests from these clients. The received data is then rendered as Hypertext Markup Language (`HTML`) within the client's browser, facilitating the creation of dynamic web pages that respond interactively to user requests. Consequently, a thorough comprehension of web server functionalities is vital for developing secure and efficient web applications and for maintaining overall system security. Among the most widely used web servers on Linux platforms are Apache, Nginx, Lighttpd, and Caddy, with Apache being particularly popular due to its broad compatibility with operating systems including Ubuntu, Solaris, and Red Hat Linux. For penetration testers, web servers offer various utilities. They can be employed to facilitate file transfers, enabling testers to log in and interact with target systems through HTTP or HTTPS ports. Additionally, web servers can be leveraged to conduct phishing attacks by hosting replicas of target pages, thereby attempting to capture user credentials. Beyond these applications, web servers provide numerous other opportunities for testing and exploiting vulnerabilities within a network. Apache web server has a variety of features that allow us to host a secure and efficient web application. Moreover, we can also configure logging to get information about the traffic on our server, which helps us analyze attacks. We can install Apache using the following command:
- ![[Screenshot 2026-07-31 at 15.35.14.png]]
- ![[Screenshot 2026-07-31 at 15.35.34.png]]
# VPN:
- ![[Screenshot 2026-07-31 at 15.37.19.png]]

