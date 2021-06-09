import os

dir_root = 'my_project'
dir_name = ['setting', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(dir_root):
    for dir in dir_name:
        path = os.path.join(dir_root, dir)
        os.makedirs(path)