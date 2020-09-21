from src.ssh import SSH
from src.aux import *
from src.yaml import get_target_servers
import pathlib

def get_host_port_list(target_host: dict):
    print(f"\033[95m{target_host['ip']}:\033[0m")
    ssh = SSH(target_host['ip'], target_host['user'], target_host['key_path'])

    if target_host['http_server'] == 'apache':
        hosts_path = '/etc/apache2/sites-enabled'
    elif target_host['http_server'] == 'nginx':
        hosts_path = '/etc/nginx/sites-enabled'

    ls_output = ssh.exec_cmd(f'ls {hosts_path}')

    HOST_LIST = ls_handler(ls_output)

    for host in HOST_LIST:
        cat_output = ssh.exec_cmd(f'cat {hosts_path}/{host}')
        port = find_port(cat_output)
        if port != None:
            host = host.replace('.conf', '')
            print(f"Host: {host} Port: {port}")

DEFAULT_PATH = pathlib.Path(__file__).parent.absolute()
TARGET_SERVER_LIST = get_target_servers(str(DEFAULT_PATH) + '/config.yaml')

for target_server in TARGET_SERVER_LIST:
    get_host_port_list(target_server)

