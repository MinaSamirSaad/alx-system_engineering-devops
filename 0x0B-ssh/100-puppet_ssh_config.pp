# make changes to our configuration file

exec { 'Add new lines':
command => '/bin/echo "    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    BatchMode yes" >> /etc/ssh/ssh_config',
}
