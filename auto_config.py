import paramiko
import time

ssh_host = ["10.88.200.190", "10.88.200.241"]
ssh_port = 22
ssh_user = "cisco"
ssh_passwd = "cisco"

commands = ["config t",
            "ntp server 10.88.200.254",
            "do write",
            "exit"]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_user, password=ssh_passwd, look_for_keys=False)

terminal = ssh_client.invoke_shell()

for each_command in commands:
    terminal.send(each_command + "\n")
    time.sleep(1)
    std_out = terminal.recv(65535)
    print(std_out.decode("utf-8"))

print("Awesome! SSH disconnected.")
terminal.close()
ssh_client.close()
