# Kill a process

exec { 'killmenow' :
    path    => '/usr/bin/',
    command => 'pkill killmenow',
}
