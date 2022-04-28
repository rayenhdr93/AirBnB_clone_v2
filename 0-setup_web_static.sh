#!/usr/bin/env bash
mkdir -p /data/web_static/releases/ 2>/dev/null
mkdir -p /data/web_static/shared/ 2>/dev/null
mkdir -p /data/web_static/releases/test/ 2>/dev/null
echo "<h1>wow this is a test</h1>" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
config="
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	location /hbnb_static {
		alias /data/web_static/current;
	}
}
"
echo -e "$config" > /etc/nginx/sites-available/default
systemctl restart nginx
