from os import listdir, getcwd, rename
from os.path import isfile, join


mypath = 'parts'

target_dir = join(getcwd(), mypath)

print(target_dir)

onlyfiles = [rename(join(target_dir, f) , f'{join(target_dir, f)}.csv') for f in listdir(mypath) if isfile(join(mypath, f))]

