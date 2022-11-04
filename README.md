# DOMjudge-docker-compose

DOMjudge 安裝流程

DOMjudge是一個競賽評量程式，
感覺拿來當CPE或程式類技藝競賽的模擬平台都不錯

## 安裝環境

Debian


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

then login the dashboard, click user
change "judgeaemons" password to ```9NQLNMcLCr8zu0gB```

![image](https://user-images.githubusercontent.com/50062014/199965217-f47463a5-aa03-4bf8-acbc-eaec38260889.png)


如果 Judgehosts 有多的　Judgehosts　那就是成功了，不然用　docker container logs 也可以看出來

這邊可能有幾個問題

1. grub 設定沒設
2. 401 驗證過不去
3. url 打不到 server

上面多的步驟就是避免上面三個問題

然後再打一次

```
sudo docker-compose up -d
```


![image](https://user-images.githubusercontent.com/50062014/199961181-061f0dd3-b430-49fe-b1e9-22c668091110.png)

最後上傳題目，開個使用者測試一下

![image](https://user-images.githubusercontent.com/50062014/199961702-cc908315-803d-409f-9238-9aac9da00806.png)


Done!

## note

docker-compose.yml 裡面有幾個要注意的
第八行的:前面要是自己有的路徑，我是放在用戶目錄底下
```
- /home/iming/backup:/var/lib/mysql
```
每個 dj-judgehost 的密碼可以改 但每個都要一樣
但記得改的跟我不一樣的話 user 那邊的密碼也要改的跟你設的一樣
```
- JUDGEDAEMON_PASSWORD=9NQLNMcLCr8zu0gB
```

本文同步發至 https://sectools.tw/domjudge/


