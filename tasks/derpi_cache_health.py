import glob
import json
import os.path

derpiDamageCount = 0
derpiTotalCount = 0
derpiHealthPercent = 0
depriCacheFileCount = 0

def get_task_data():
    if os.path.isfile("./data/derpi_cache.txt"):
        with open("./data/derpi_cache.txt") as f:
            contents = f.read()
        if len(contents.split(";")) == 4:
            return contents.split(";")
    return [0,0,0,0]

def do_task():
    global derpiDamageCount
    global derpiTotalCount
    global derpiHealthPercent
    global depriCacheFileCount
    depriCacheFiles = glob.glob("./data/derpi_raw/*.json")
    depriCacheFileCount = len(depriCacheFiles)
    derpiDamageCount = 0
    derpiTotalCount = 0
    for filename in depriCacheFiles:
        with open(filename) as data_file:
            data = json.load(data_file)
            derpiTotalCount += 1
            try:
                temp2084 = data["tags"]
            except Exception as e:
                derpiDamageCount += 1
    derpiHealthPercent = int(round(100 - (100 * int(derpiDamageCount) / int(derpiTotalCount)), 1))
    f = open("./data/derpi_cache.txt", 'w')
    f.write("{};{};{};{}".format(derpiDamageCount, derpiTotalCount, derpiHealthPercent, depriCacheFileCount))
    f.close()