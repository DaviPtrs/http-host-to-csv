from src.ssh import SSH
from src.aux import *
from src.yaml import get_target_servers
import collections
import pathlib
from src.spreadsheets import *

def generate_csv(name, data: list):
    print(f"Generating CSV to file {name}")
    with open(name + '.csv', 'w') as file:
        file.write(f'containers\n')
        for container in data:
            file.write(f'{container}\n')

    print(f"CSV to {name} generated!")


def get_host_port_list(target_host: dict):
    print(f"\033[95m{target_host['ip']}:\033[0m")
    ssh = SSH(target_host['ip'], target_host['user'], target_host.get('key_path'))

    server = target_host['http_server']
    if server == 'apache':
        hosts_path = '/etc/apache2/sites-enabled'
    elif server == 'nginx':
        hosts_path = '/etc/nginx/sites-enabled'

    ls_output = ssh.exec_cmd("docker ps --format '{{.Names}}'")

    CONFIG_LIST = ls_handler(ls_output)

    return CONFIG_LIST


DEFAULT_PATH = pathlib.Path(__file__).parent.absolute()
TARGET_SERVER_LIST = get_target_servers(str(DEFAULT_PATH) + '/config.yaml')

for target_server in TARGET_SERVER_LIST:
    output = get_host_port_list(target_server)
    print(output)
    generate_csv('out/' + target_server['ip'], output)
    
join_csvs('./out/')

