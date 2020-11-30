from src.ssh import SSH
from src.aux import *
from src.yaml import get_target_servers
import collections
import pathlib
from src.spreadsheets import *

def generate_csv(name, data: dict):
    print(f"Generating CSV to file {name}")
    od = collections.OrderedDict(sorted(data.items()))
    with open(name + '.csv', 'w') as file:
        file.write('Porta, Hosts\n')
        for porta, hosts in od.items():
            file.write(f'{porta},{hosts[0]}\n')
            if len(hosts) > 1:
                for host in hosts[1:]:
                    file.write(f',{host}\n')
    print(f"CSV to {name} generated!")


def get_host_port_list(target_host: dict):
    print(f"\033[95m{target_host['ip']}:\033[0m")
    ssh = SSH(target_host['ip'], target_host['user'], target_host['key_path'])

    server = target_host['http_server']
    if server == 'apache':
        hosts_path = '/etc/apache2/sites-enabled'
    elif server == 'nginx':
        hosts_path = '/etc/nginx/sites-enabled'

    ls_output = ssh.exec_cmd(f'ls {hosts_path}')

    CONFIG_LIST = ls_handler(ls_output)

    output = dict()

    for config in CONFIG_LIST:
        cat_output = ssh.exec_cmd(f'cat {hosts_path}/{config}')
        port = find_port(cat_output, server)
        host = find_host_url(cat_output)
        if port != None and host != None:
            port = int(port)
            if not output.get(port):
                output[port] = list()
            output[port].append(host)
            print(f"Config: {host} Port: {port}")
    return output

DEFAULT_PATH = pathlib.Path(__file__).parent.absolute()
TARGET_SERVER_LIST = get_target_servers(str(DEFAULT_PATH) + '/config.yaml')

for target_server in TARGET_SERVER_LIST:
    output = get_host_port_list(target_server)
    print(output)
    generate_csv('out/' + target_server['ip'], output)
    
join_csvs('./out/')

