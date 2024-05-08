#Fixing 500 server error
exec {'substitute':
  cwd     => '/var/www/html',
  command => '/bin/sed -i s/phpp/php/g wp-settings.php',
}
