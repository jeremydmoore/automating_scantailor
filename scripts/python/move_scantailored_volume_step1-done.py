# ============ imports ============ #
# standard library
from pathlib import Path
from shutil import copy2


# 3rd party modules
from PIL import Image

# my modules (located next to this script)
import applescript
import config

# ============ lookup_dicts ============ #
compression_lookup_dict = {1: 'uncompressed',
                           4: 'group4',
                           5: 'LZW',
                           6: 'JPEG',
                          }

# ============ functions ============ #
def get_compression(image):
    compression = image.tag_v2[259]
    compression = compression_lookup_dict[compression]
    return compression

def decompress_continuous_tone(image, image_path):
    compression = get_compression(image)
    if compression != 'group4':  # save image uncompressed
            image.save(image_path, tiffinfo=image.tag, compression=None, dpi=image.info['dpi'])
    else:
        image.save(image_path, tiffinfo=image.tag, compression=compression, dpi=image.info['dpi'])

def move_dir(to_dir_path):
    
    new_dir_path = config.step2_dir_path.joinpath(to_dir_path.name)

    # move directory with rename
    to_dir_path.rename(new_dir_path)

    if new_dir_path.is_dir():
        volume_dir_path = new_dir_path
    else:
        raise ValueError(f'{new_dir_path} is not a directory')

    # get list of images in out directory
    tif_path_list = sorted(volume_dir_path.joinpath('out').glob('*.tif'))

    new_dir_path = config.step3_dir_path.joinpath(volume_dir_path.name)
    new_dir_path.mkdir()

    # copy out tifs into new directory in step3_dir_path
    for tif_path in tif_path_list:
        new_tif_path = new_dir_path.joinpath(tif_path.name)
        copy2(tif_path, new_tif_path)

    cmd = f'{to_dir_path.name} \
            ---> \
            {new_dir_path}'
    applescript.display_notification(cmd)

def copy_scantailor_images(from_dir_path, to_dir_path, decompress=True):
    
    # create new directory in to_dir_path
    new_dir_path = to_dir_path.joinpath(from_dir_path.name)
    new_dir_path.mkdir()
    
    # get list of images in out directory and copy to new_dir_path
    tif_path_list = list(from_dir_path.joinpath('out').glob('*.tif'))
    for tif_path in tif_path_list:
        new_tif_path = new_dir_path.joinpath(tif_path.name)
        if decompress:  # then we check for compression
            image = Image(tif_path)
            decompress_continuous_tone(image, new_tif_path)
        else:
            copy2(tif_path, new_tif_path)
            
    cmd = f'{to_dir_path.name} \
            ---> \
            {new_dir_path}'
    applescript.display_notification(cmd)


if __name__ == '__main__':
    
    # verify config file
    config.verify()
    
    # get list of volumes in directory
    volume_dir_path_list = sorted([x for x in config.step1_dir_path.iterdir() if x.is_dir()])

    # grab 1 volume, which is the first 1 and move it
    step1_dir_path = volume_dir_path_list[0]
    step2_dir_path = config.step2_dir_path.joinpath(step1_dir_path.name)
    step1_dir_path.rename(step2_dir_path)
    
    step3_dir_path = config.step3_dir_path.joinpath(step2_dir_path.name)
    copy_scantailor_images(step_2_dir_path, step3_dir_path)

    # for batch processing
    # for volume_dir_path in volume_dir_path_list:
    #     print(f'{volume_dir_path.name}')
    #     move_dir(volume_dir_path)