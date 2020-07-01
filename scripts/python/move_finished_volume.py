# ============ imports ============ #
from pathlib import Path
import applescript

root_dir_path = Path('/Users/dlisla/shared_with_docker')
input_dir = 'agrtfhs'
input_dir_path = root_dir_path.joinpath(input_dir)
output_dir_path = root_dir_path.joinpath(f'{input_dir}_toQC')

volume_dir_path_list = sorted([x for x in input_dir_path.iterdir() if x.is_dir()])

current_volume_path = volume_dir_path_list[0]
current_volume_output_path = output_dir_path.joinpath(current_volume_path.name)

cmd = f'{current_volume_path}\n -- will become -->\n{current_volume_output_path}'

applescript.display_notification(cmd)

current_volume_path.rename(current_volume_output_path)
