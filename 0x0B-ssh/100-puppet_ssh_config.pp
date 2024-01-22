# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => 'IdentityFile ~/.ssh/school',
  replace            => true,
  append_on_no_match => true
}

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => 'PasswordAuthentication no',
  replace            => true,
  append_on_no_match => true
}
