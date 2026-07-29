---
Date: 2026-07-27 11:39
category:
tags:
Tools:
---
- The `/etc/shadow` file is a critical system file that stores encrypted password information for all user accounts. For security reasons, it is readable and writable only by the root user to prevent unauthorized access to sensitive authentication data.
# Sudo:
- To perform tasks that require elevated privileges, users can utilize the `sudo` command. The `sudo` command, short for "superuser do," allows permitted users to execute commands with the security privileges of another user, typically the superuser or root. This enables users to perform administrative tasks without logging in as the root user, which is a best practice for maintaining system security. We will explore sudo permissions in greater detail in the `Linux Security`section.

|**Command**|**Description**|
|---|---|
|`sudo`|Execute command as a different user.|
|`su`|The `su` utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser). A shell is then executed.|
|`useradd`|Creates a new user or update default new user information.|
|`userdel`|Deletes a user account and related files.|
|`usermod`|Modifies a user account.|
|`addgroup`|Adds a group to the system.|
|`delgroup`|Removes a group from the system.|
|`passwd`|Changes user password.|

# Su:
- To run a command as the target user without starting an interactive shell, use the `-c`, `--command` option. For example, to invoke the [`ps`](https://linuxize.com/post/ps-command-in-linux/) command as root: `su -c "whoami" tyrion` `su -c "ps aux"` 