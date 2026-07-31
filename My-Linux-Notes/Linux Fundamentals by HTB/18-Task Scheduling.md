---
Date: 2026-07-31 13:37
category:
tags:
Tools:
---
- Task scheduling is a critical feature in Linux systems that allows users and administrators to automate tasks by running them at specific times or regular intervals, eliminating the need for manual initiation

# Systemd:
- Systemd is a service used in Linux systems such as Ubuntu, Redhat Linux, and Solaris to start processes and scripts at a specific time. With it, we can set up processes and scripts to run at a specific time or time interval and can also specify specific events and triggers that will trigger a specific task. To do this, we need to take some steps and precautions before our scripts or processes are automatically executed by the system.
1. Create a timer (schedules when your `mytimer.service` should run)
2. Create a service (executes the commands or script)
3. Activate the timer
- **Create a Timer:** To create a timer for systemd, we need to create a directory where the timer script will be stored. Bunun için ` mkdir /etc/systemd/system/mytimer.timer.d` ve ` vim /etc/systemd/system/mytimer.timer` lazım. Next, we need to create a script that configures the timer. The script must contain the following options: "Unit", "Timer" and "Install". The "Unit" option specifies a description for the timer. The "Timer" option specifies when to start the timer and when to activate it. Finally, the "Install" option specifies where to install the timer. VIM üzerinden bu ayarları sağlayabilirsin. Here it depends on how we want to use our script. For example, if we want to run our script only once after the system boot, we should use `OnBootSec` setting in `Timer`. However, if we want our script to run regularly, then we should use the `OnUnitActiveSec` to have the system run the script at regular intervals. Next, we need to create our `service`.
- **Create a Service:** `vim /etc/systemd/system/mytimer.service`  Here we set a description and specify the full path to the script we want to run. The "multi-user.target" is the unit system that is activated when starting a normal multi-user mode. It defines the services that should be started on a normal system startup.![[Screenshot 2026-07-31 at 13.55.41.png]]
- **Reload Systemd:** `sudo systemctl daemon-reload` after that, we can use ` systemctl` to ` start` the service manually and ` enable` the autostart.
- **Start the Timer & Service:** ` systemctl start mytimer.timer && systemctl enable mytimer.timer` this way, `mytimer.service` will be launched automatically according to the intervals (or delays) you set in ` mtimer.timer` 

# Cron:
- ![[Screenshot 2026-07-31 at 14.00.01.png]]
- knk burada her şey yazıyor.

**Systemd vs Corn:** The key difference between these two tools is how they are configured. With Systemd, you need to create a timer and services script that tells the operating system when to run the tasks. On the other hand, with Cron, you need to create a `crontab` file that tells the cron daemon when to run the tasks.