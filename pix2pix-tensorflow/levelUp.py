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
    img_dir = os.path.dirname(os.path.abspath(__file__)) + "/pixelart"

    # delete directory
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)

    # make directories
    os.makedirs(img_dir)

    workdir = os.getcwd()+"/"+sys.argv[1]
    images = glob.glob(workdir+'/*.jpg')
    images += glob.glob(workdir+'/*.png')
    images += glob.glob(workdir+'/*.bmp')

    workdir2 = os.getcwd()+"/"+sys.argv[2]
    images2 = glob.glob(workdir2+'/*.jpg')
    images2 += glob.glob(workdir2+'/*.png')
    images2 += glob.glob(workdir2+'/*.bmp')

    cnt = 0

    for image in images:
        imagepath = img_dir+"/image%07d" %cnt +".png"
        print(imagepath)

        # input image
        input_img = Image.open(image)
        # resize for pix2pix format
        input_img = input_img.resize((256, 256))

        for image2 in images2:
            width, height = input_img.size
            dst_img = Image.new('RGB', (width*2, height))
            # 元画像と同じファイル名を探す
            if os.path.basename(image) == os.path.basename(image2):
                output_img = Image.open(image2)
                output_img = output_img.resize((256, 256))
                #output_img = make_pixelart(input_img, 32)
                #output_img.save(imagepath)
                dst_img.paste(input_img, (0, 0))
                dst_img.paste(output_img, (width, 0))
                dst_img.save(imagepath)
        cnt += 1
