# ============ imports ============ #
from pathlib import Path
from shutil import copy2

import applescript
import config

def move_dir(volume_dir_path):
    volume_new_dir_path = config.step2_dir_path.joinpath(volume_dir_path.name)

    cmd = f'{volume_dir_path.name}\n -- will become --> \n{volume_new_dir_path}'
    applescript.display_notification(cmd)

    # move directory with rename
    volume_dir_path.rename(volume_new_dir_path)

    if volume_new_dir_path.is_dir():
        volume_dir_path = volume_new_dir_path
    else:
        raise ValueError(f'{volume_new_dir_path} is not a directory')

    # get list of images in out directory
    tif_path_list = sorted(volume_dir_path.joinpath('out').glob('*.tif'))

    volume_new_dir_path = config.step3_dir_path.joinpath(volume_dir_path.name)
    volume_new_dir_path.mkdir()

    # copy out tifs into new directory in step3_dir_path
    for tif_path in tif_path_list:
        new_tif_path = volume_new_dir_path.joinpath(tif_path.name)
        copy2(tif_path, new_tif_path)

# get list of volumes in directory
volume_dir_path_list = sorted([x for x in config.step1_dir_path.iterdir() if x.is_dir()])

# grab current volume, which is currently the first volume
# volume_dir_path = volume_dir_path_list[0]

for volume_dir_path in volume_dir_path_list:
    print(f'{volume_dir_path.name}')
    move_dir(volume_dir_path)
