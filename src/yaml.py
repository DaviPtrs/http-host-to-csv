from yaml import load, dump, FullLoader


def yaml_load(path: str):
    try:
        with open(r'{}'.format(path)) as file:
            data = load(file, Loader=FullLoader)
            return data
    except Exception as error:
        print(error)
        return None

def get_target_servers(yaml_path):
    yaml_data = yaml_load(yaml_path)
    hosts = yaml_data.get('hosts')
    return hosts
