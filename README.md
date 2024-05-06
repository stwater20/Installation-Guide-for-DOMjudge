# DOMjudge-docker-compose

 ![sample-2](/sample-2.jpg)
 ![sample-1](/sample-1.jpg)

## Installation Guide for DOMjudge

DOMjudge is a contest adjudication program that works well as a simulation platform for CPE or programming competitions.

### Installation Environment

- Debian

### Installation Process

1. Modify `/etc/default/grub`:
   ```
   GRUB_CMDLINE_LINUX_DEFAULT="quiet cgroup_enable=memory swapaccount=1 systemd.unified_cgroup_hierarchy=0"
   ```

2. Update Grub:
   ```
   sudo update-grub
   ```

3. Reboot:
   ```
   sudo reboot
   ```

4. Execute docker-compose.yml:
   ```
   sudo docker-compose up -d
   ```

5. Obtain admin password:
   ```
   sudo docker exec -it domserver_container_name cat /opt/domjudge/domserver/etc/initial_admin_password.secret
   ```
   Note: Use `sudo docker ps` to check the container name.

6. If the output is `[unknown]`, reset admin password:
   ```
   sudo docker exec -it domserver_container_name /opt/domjudge/domserver/webapp/bin/console domjudge:reset-user-password admin
   ```

7. Log in to the dashboard, click on user, and change the password for "judgeaemons" to `9NQLNMcLCr8zu0gB`.
   

   ![Dashboard](https://user-images.githubusercontent.com/50062014/199965217-f47463a5-aa03-4bf8-acbc-eaec38260889.png)


8. Check for additional Judgehosts; use `docker container logs` if necessary.

### Troubleshooting

If encountering issues such as:
- Grub settings not configured
- Unable to pass 401 authentication
- URL cannot reach the server

Follow the additional steps provided in the installation process to address these issues.

### Additional Notes

- Update paths and passwords in docker-compose.yml as needed.
- Ensure consistency in passwords across all Judgehosts and user sections.
- If the log displays an error, obtain a new restAPI password:
  ```
  docker exec -it domserver cat /opt/domjudge/domserver/etc/restapi.secret
  ```
  Replace `JUDGEDAEMON_PASSWORD` in docker-compose.yml with the new password and restart:
  ```
  docker-compose up -d
  ```

This installation guide is also available at [https://sectools.tw/domjudge/](https://sectools.tw/domjudge/).
