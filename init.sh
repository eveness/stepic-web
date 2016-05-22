#!/usr/bin/bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo pip install --upgrade django

#sudo gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon --access-logfile a.log --error-logfile e.log