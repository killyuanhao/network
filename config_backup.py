import paramiko

device_list = ['10.88.200.250', '10.88.200.241']
device_username = 'rfadmin'
device_password = '5hR-f1@3'

command = 'show run'

for each_device in device_list:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(each_device,
                   port=22,
                   username=device_username,
                   password=device_password,
                   allow_agent=False,
                   look_for_keys=False)
    stdin, stdout, stderr = client.exec_command(command)
    my_file = open(each_device, 'w')
    for each_line in stdout.readlines():
        my_file.write(each_line)
    my_file.close()