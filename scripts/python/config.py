# config.py

root_dir_path = Path('/Users/dlisla/shared_with_docker')

# to be ScanTailored
step1_dir_path = root_dir_path.joinpath('1.toScanTailor')

# have been ScanTailored, a holding directory
step2_dir_path = root_dir_path.joinpath('2.ScanTailored')

# need quality control
step3_dir_path = root_dir_path.joinpath('3.toQC')
