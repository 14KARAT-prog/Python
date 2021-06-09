import yaml
import os

with open('config.yaml') as conf:
    content = yaml.safe_load(conf)

def create(values, prefix=""):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass


create(content)