import dataset
import glob
import json
from tqdm import tqdm

db = dataset.connect('sqlite:///../data/derpi.db')

image_num = 1
image_set = glob.glob("../data/derpi_raw/*.json")
image_total = len(image_set)
for image in tqdm(image_set):
    #print(str(image_num) + " of " + str(image_total))
    image_id = image.rsplit("/", 1)[1]
    #print(image_id)
    with open(image) as data_file:
        data = json.load(data_file)
        table = db['image_{}'.format(image_id[:-5])]
        for item in data:
            #print(item)
            #print(data[item])
            table.insert(dict(name='{}'.format(item), data='{}'.format(data[item])))