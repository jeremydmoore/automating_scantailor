# config.py
from pathlib import Path

# update this with project identifier
project_identifier = 'agrutesc'

# directory shared with Docker
root_dir_path = Path.home().joinpath('shared_with_docker').resolve()

# project directory
project_dir_path = root_dir_path.joinpath(project_identifier)

# to be ScanTailored
step1_dir_path = project_dir_path.joinpath('1.toScanTailor')

# have been ScanTailored, a holding directory
step2_dir_path = project_dir_path.joinpath('2.ScanTailored-holding')

# need quality control
step3_dir_path = project_dir_path.joinpath('3.toQC')

# dict of dir_paths in config.py
dir_path_dict = {'root': root_dir_path,
                 'project': project_dir_path,
                 'step1': step1_dir_path,
                 'step2': step2_dir_path,
                 'step3': step3_dir_path,
                }

def verify():
    print(f'Verifying {len(dir_path_list)} workflow directories for Project "{project_identifier}" . . .')
    for dir_type, dir_path in dir_path_dict.items():
        if not dir_path.is_dir():
            raise ValueError(f'{dir_path} is not a directory')
        else:
            print(f'\t\t{dir_type}: {dir_path}')
    # add spaces equal to "Verifying " at beginning so # of directories lines up
    print(f'{" " * 10}{len(dir_path_list)} workflow directories verified successfully')