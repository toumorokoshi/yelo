# this is an example provisioning script
# for example to add this to an nginx configuration.

$service_root = "/home/services/yelo/"

file { "/etc/nginx/sites-enabled/yelo.conf":
  ensure  => "file",
  source  => "${service_root}/host_config/yelo.conf",
}

exec { "uranium":
    command => "/usr/bin/python uranium",
    path => $service_root,
    logoutput => 'true',
    user => 'behonest',
}

exec { "nginx-reload":
    command => "/usr/bin/nginx -s reload"
}