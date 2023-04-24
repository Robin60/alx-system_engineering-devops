# install flask -v 2.1.0 via pip3

exec { 'flask':
     command => '/usr/bin/pip3 install Flask==2.1.0',
       creates => '/usr/local/lib/python3.8/dist-packages/flask',
}
