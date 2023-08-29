# nginx_config.pp

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80 default_server;
                server_name _;

                location / {
                    return 301 https://www.example.com$request_uri;
                }

                location /redirect_me {
                    return 301 https://www.youtube.com;
                }
            }",
  require => Package['nginx'],
}

# Ensure Nginx is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [
    Package['nginx'],
    File['/etc/nginx/sites-available/default'],
  ],
}
