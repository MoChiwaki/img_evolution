from PIL import Image
import numpy as np
import sys
import os
import glob
import shutil

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 3):
        print ("Usage: $ python " + param[0] + " /photo_directory")
        quit()

    # pwd = cmd('pwd')
    img_dir = os.path.dirname(os.path.abspath(__file__)) + "/lvUpTestData"

    # delete directory
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)

    # make directories
    os.makedirs(img_dir)

    workdir = os.getcwd()+"/"+sys.argv[1]
    images = glob.glob(workdir+'/*.jpg')
    images += glob.glob(workdir+'/*.png')
    images += glob.glob(workdir+'/*.bmp')

    cnt = 0

    for image in images:
        imagepath = img_dir+"/image%07d" %cnt +".png"
        print(imagepath)

        # input image
        input_img = Image.open(image)
        # resize for pix2pix format
        input_img = input_img.resize((256, 256))

        width, height = input_img.size
        dst_img = Image.new('RGB', (width*2, height))

        dst_img.paste(input_img, (0, 0))
        dst_img.paste(input_img, (width, 0))

        cnt += 1
