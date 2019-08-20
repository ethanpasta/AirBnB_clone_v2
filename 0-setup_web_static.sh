#!/usr/bin/env bash
# Script sets up your web server for the deployment of web_static
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/root \/var\/www\/html;/a location \/hbnb_static\/ { alias \/data\/web_static\/current\/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
