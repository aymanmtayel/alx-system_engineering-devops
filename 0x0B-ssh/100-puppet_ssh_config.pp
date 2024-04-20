include stdlib

file_line { 'Use Private key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentifyFile ~/.ssh/school',
  replace => true,
}

file_line { 'Turn off password auth':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}
