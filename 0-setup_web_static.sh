#!/usr/bin/env bash
# setup web static
mkdir -p /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/ 2>/dev/null
echo "<h1>wow this is a test</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
config="
server {
	listen 80 default_server;

	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
	}


	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
		try_files \$uri \$uri /hbnb_static/index.html;
	}
}
"
echo -e "$config" > /etc/nginx/sites-available/default

service nginx restart
