#Increase the amount of trafic for nginx to handle

exec {'update-config':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx'
}

exec {'restart-nginx':
  command => '/usr/sbin/service nginx restart'
}

