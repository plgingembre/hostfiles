TME_BE_SWITCHES = [
    '10.34.101.1',
    '10.34.102.1',
    '10.34.111.1',
    '10.34.112.1',
    '10.34.113.1',
    '10.34.114.1',
    '10.34.115.1',
    #'10.34.121.1',
    #'10.34.122.1',
    '10.34.123.1',
    #'10.34.124.1',
    '10.34.131.1',
    #'10.34.132.1',
    '10.34.133.1',
    '10.34.134.1'
]
TME_ACCTON_SWITCHES = [
    '10.36.10.11',
    '10.36.10.12',
    '10.36.10.13',
    '10.36.10.14',
    '10.36.10.15',
    '10.36.10.16',
    '10.36.10.17',
    '10.36.10.18',
    '10.36.10.45',
    '10.36.10.46',
    '10.36.10.47',
    '10.36.10.48',
    '10.36.10.20'

]
TME_DELL_SWITCHES = [
    '10.36.10.29',
    '10.36.10.30',
    '10.36.10.31',
    '10.36.10.32',
    '10.36.10.33',
    '10.36.10.34',
    '10.36.10.35',
    '10.36.10.36',
    '10.36.10.37',
    '10.36.10.38',
    '10.36.10.39',
    '10.36.10.40',
    '10.36.10.41',
    '10.36.10.42',
    '10.36.10.43',
    '10.36.10.44'
]
TME_SOLARIS_SWITCHES = [
    '10.36.10.19',
    '10.36.10.21',
    '10.36.10.22',
    '10.36.10.23',
    '10.36.10.24',
    '10.36.10.25',
    '10.36.10.26'
]
TME_CISCO_SWITCHES = [
    #'10.36.10.27',
    #'10.36.10.28'
]
EBC_BE_SWITCHES = [
    '10.38.10.252',
    '10.38.10.253'
]
EBC_ACCTON_SWITCHES = [
    '10.38.10.12',
    '10.38.10.13',
    '10.38.10.14',
    '10.38.10.15',
    '10.38.10.25',
    '10.38.10.26',
    '10.38.10.31',
    '10.38.10.37',
    '10.38.10.38'
]
EBC_ACCTON_SWITCHES_2 = [
    '10.38.10.32',
    '10.38.10.34',
    '10.38.10.35',
    '10.38.10.36'
]
EBC_DELL_SWITCHES = [
    '10.38.10.19',
    '10.38.10.20'
]
EBC_DELL_SWITCHES_2 = [
    '10.38.10.22',
    '10.38.10.23'
]
DISTRI = [
    '10.134.1.23',
    '10.134.1.24'
]
TESTBED = [
    '10.36.10.11',
    '10.36.10.12',
    '10.36.10.13',
    '10.36.10.14',
    '10.36.10.15',
    '10.36.10.16'
]
ALL_SWITCHES = TME_BE_SWITCHES + TME_ACCTON_SWITCHES + TME_DELL_SWITCHES + TME_SOLARIS_SWITCHES + TME_CISCO_SWITCHES + EBC_BE_SWITCHES + EBC_ACCTON_SWITCHES + EBC_DELL_SWITCHES + DISTRI
SHELL_USERNAME = 'pluribus'
SOLARIS_USERNAME = 'admin'
NETVISOR_USERNAME = 'network-admin'
#SHELL_PASSWORD = 'test123'
NETVISOR_DEFAULT_PASSWORD = 'test123'
NETVISOR_TME_BE_PASSWORD = 'N3T@dM-123!'
NETVISOR_EBC_BE_PASSWORD = 'Test123'
TIMEOUT = 60
PKEY = ''
PORT = 22
PLATFORM = 'pluribus'
#PN_COMMANDS = ['switch-local switch-info-show format switch,model,chassis-serial,system-mem,disk-model,disk-type,disk-firmware', 'switch-local switch-setup-show format device-id']
#COMMANDS = ['cat /etc/chassis_info | egrep -E "Product Name|Service Tag|Serial Number"']
#COMMANDS = ['lsblk', 'sudo -S parted /dev/sda print', 'sudo -S parted /dev/sdb print']
