#!/usr/bin/env python

import requests
import subprocess
import sys
import os

import lxml.html as lh

from PIL import Image


def get_filename(url):
    splits = url.split("/")
    return splits[-1][:splits[-1].index(".jpg")] + ".jpg"

def main(url, dir_dest):
    print("## Start ##")

    if not os.path.isdir(dir_dest):
        print("Creating %s" % dir_dest)
        os.mkdir(dir_dest)
    os.chdir(dir_dest)

    page = requests.get(url)
    doc = lh.fromstring(page.content)

    img_elements = doc.xpath('//*[@id="svPlayerId"]/div[1]/div[2]/section[*]/img')
    images = []

    for img in range(0, len(img_elements)):
        file_url = img_elements[img].get("src")
        try:
            print("=====")
            file_name = get_filename(file_url)
            print("file_name:", file_name)
            print("file_url:", file_url)
            
            # Downloading
            file_req = requests.get(file_url)
            file_cont = file_req.content
            #print(file_cont)
            open(file_name, 'wb').write(file_cont)

            # Append
            images.append(file_name)

        except Exception as e:
            print("File %s downloading error: %s" % (file_name, str(e)))

    # Saving pdf
    image1 = Image.open(images.pop(0))
    im1 = image1.convert('RGB')
    images_im = []
    for img in images:
        im = Image.open(img)
        images_im.append(im)
    im1.save('anew.pdf', save_all=True, append_images=images_im)
        


if __name__=="__main__":
    if len(sys.argv)!=3:
        print("usage:\n./main.py https://es.slideshare.net/ernestoq1973/dba-postgresql-desde-bsico-a-avanzado-parte1-36210081 $PWD/tmp")
        exit(1)
    main(sys.argv[1], sys.argv[2])

