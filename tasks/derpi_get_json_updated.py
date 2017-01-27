import urllib.request
import json
import os.path

def do_task():
    urllib.request.urlretrieve("https://derpibooru.org/images.json?constraint=updated&order=d", "./data/derpi_updated.json")
    images_to_grab = []
    with open("./data/derpi_updated.json") as data_file:
        data = json.load(data_file)
        for image in data["images"]:
            image_id = image["id"]
            images_to_grab.append(image_id)
    for image in images_to_grab:
        if os.path.isfile("./data/derpi_raw/{}.json".format(image)):
            print("[DEBUG  ] Derpibooru JSON file {}.json is already downloaded".format(image))
            pass
        else:
            print("[DEBUG  ] Downloading Derpibooru JSON file {}.json".format(image))
            urllib.request.urlretrieve("https://derpibooru.org/{}.json".format(image), "./data/derpi_raw/{}.json".format(image))
    #print(images_to_grab)