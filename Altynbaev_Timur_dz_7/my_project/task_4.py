import os
from collections import defaultdict


def dir_info():
    dir_root = 'my_project'
    files_project = defaultdict(int)
    for root, dirs, files in os.walk(dir_root):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            files_project[size] += 1

    for size, nums in sorted(files_project.items()):
        print(f'{size}: {nums}')
