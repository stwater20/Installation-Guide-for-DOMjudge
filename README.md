# DOMjudge-docker-compose

DOMjudge 安裝流程，踩太多坑...

## 安裝流程

修改 ``` /etc/default/grub ```
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet cgroup_enable=memory swapaccount=1 systemd.unified_cgroup_hierarchy=0"
```
然後更新
```
sudo update-grub
```
記得重開機
```
sudo reboot
```

然後執行我的 docker-compose.yml

```
sudo docker-compose up -d
```

帳號是 admin
密碼要打
```
sudo docker exec -it domserver_container_name cat /opt/domjudge/domserver/etc/initial_admin_password.secret
```
container name can use ```sudo docker ps``` to check

hece, 

if the output is ```[unknown]``` ... just like me

then type

```
sudo docker exec -it domserver_container_name /opt/domjudge/domserver/webapp/bin/console domjudge:reset-user-password admin
```


