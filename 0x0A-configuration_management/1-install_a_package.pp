# install flask -v 2.1.0 via pip3

exec { 'flask':
  command => '/usr/bin/pip3 install Flask -v 2.1.0',
}
