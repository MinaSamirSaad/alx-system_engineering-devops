# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => "sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
  provider => 'shell',
  require  => Package['nginx'],
}

file { '/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page",
}

exec { 'custom_404':
  command  => "sed -i '/server_name _;/a error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /var/www/html;\ninternal;\n}' /etc/nginx/sites-available/default",
  provider => 'shell',
  require  => Package['nginx'],
}

exec { 'HTTP header':
  command  => 'sed -i "/index index.html index.htm index.nginx-debian.html;/a add_header X-Served-By $(cat /etc/hostname);" /etc/nginx/sites-enabled/default',
  provider => 'shell',
  require  => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
