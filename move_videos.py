import shutil, os   
from pathlib import Path

p = Path.home()


source = '/mnt/c/Users/punkr/Documents/My Videos/Test/'
destination = '/mnt/g/Videos/EFT'

files = os.listdir(source)

for file in files:
    print(f'Moving your files to {destination}, this may take some time.')
    new_path = shutil.move(f"{source}/{file}", destination)
    print(f"{file} moved to : {new_path}")
                           









