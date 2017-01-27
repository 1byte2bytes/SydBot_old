import glob
from random import randint
import os.path
import urllib

def do_task():
    derpi_files = glob.glob("./data/derpi_raw/*.json")
    ids = []
    for file in derpi_files:
        ids.append(int(file.rsplit("/", 1)[1][:-5]))
    rand_ids = []
    while len(rand_ids) < 10:
        randnum = randint(0,max(ids))
        if(os.path.isfile("./data/derpi_raw/{}.json".format(randnum))):
            pass
        else:
            rand_ids.append(randnum)
    for id in rand_ids:
        print("[DEBUG  ] Downloading Derpibooru JSON file {}.json".format(id))
        urllib.request.urlretrieve("https://derpibooru.org/{}.json".format(id),
                                   "./data/derpi_raw/{}.json".format(id))