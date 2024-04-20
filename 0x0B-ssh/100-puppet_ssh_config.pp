# Setting the server using puppet code

include stdlib

file_line { 'Use Private key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off password auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}
