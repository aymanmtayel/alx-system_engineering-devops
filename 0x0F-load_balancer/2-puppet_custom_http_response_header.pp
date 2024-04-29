#automate the task of creating a custom HTTP header response, but with Puppet.

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx
}

package {'nginx':
  ensure => 'installed',
}

file_line {'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "    add_header X-Served-By \"$(hostname)\";",
  match => 'http {',
}

exec {'start':
  command => '/usr/sbin/service nginx start',
}
