import re

def ls_handler(ls_output):
    file_list = ls_output.decode('utf-8').split('\n')
    file_list = file_list[:-1]
    return file_list

def validate_port(port):
    try:
        int_port = int(port)
    except ValueError:
        return False
    return 0 < int_port < 65535

def find_port(cat_output):
    proxy_entry = re.search(r"(?<=\/\/)([^:]+):?(.*)", cat_output.decode('utf-8'))
    if proxy_entry == None:
       return None
    else:
        proxy_entry = proxy_entry.group(2)
    port = re.search(r'[0-9]+', proxy_entry)
    if port == None:
       return None
    else:
        port = port.group(0)
    if validate_port(port):
        return port
    else:
        return None