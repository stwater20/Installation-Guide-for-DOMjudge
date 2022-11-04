# DOMjudge-docker-compose

DOMjudge 安裝流程，踩太多坑...

## 安裝流程

修改 ``` /etc/default/grub ```
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet cgroup_enable=memory swapaccount=1 systemd.unified_cgroup_hierarchy=0"
```
