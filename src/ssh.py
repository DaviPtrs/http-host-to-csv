from paramiko import SSHClient, AutoAddPolicy
 
class SSH:
    def __init__(self, host, user, key_path=None):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=host,username=user,key_filename=key_path)
 
    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            return stderr.read()
        else:
            return stdout.read()
    def __del__(self): 
        if self.ssh:
            self.ssh.close