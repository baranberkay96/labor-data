from os import listdir
from os.path import isfile, join

from mq import Queue

mypath = 'parts_draft'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

queue = Queue()

for f in onlyfiles:
    queue.lpush('files', f)

