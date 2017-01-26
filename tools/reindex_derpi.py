import dataset
import glob
import json
from tqdm import tqdm

db = dataset.connect('sqlite:///../data/derpi.db')
#db = dataset.connect('sqlite:///:memory:')

table = db['images']

image_num = 1
image_set = glob.glob("../data/derpi_raw/*.json")
image_total = len(image_set)

no_tags = []
invalid = []
for image in tqdm(image_set):
    image_id = image.rsplit("/", 1)[1]
    with open(image) as data_file:
        data = json.load(data_file)
        try:
            table.insert(dict(name=data["id"], imtags=data["tags"], image_url=data["representations"]["full"]))
        except Exception as e:
            try:
                table.insert(dict(name=data["id"], imtags='', image_url=data["representations"]["full"]))
                no_tags.append(data["id"])
            except Exception as e:
                invalid.append(data["id"])
    db.commit()

print("\r\n" + str(len(no_tags)) + " of " + str(image_total) + " images have no tags.")
print("" + str(len(invalid)) + " of " + str(image_total) + " images are damaged.")