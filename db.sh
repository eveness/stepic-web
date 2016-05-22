#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE django;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY '12345';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"