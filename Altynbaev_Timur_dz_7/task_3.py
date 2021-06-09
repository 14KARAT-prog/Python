from os import path, walk, listdir
import shutil

dir_name = 'my_project'

try:
    for root, dirs, files in walk(dir_name):
        if 'templates' in dirs and root != dir_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(dir_name, 'templates', path.basename(root)))
except FileExistsError:
    print("Уже есть")
