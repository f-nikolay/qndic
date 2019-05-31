from PIL import Image, ImageFilter
import numpy as np
import glob, argparse, os, time
# import multiprocessing as mp # sometime somewhere somehow not now ;)

"""

Quick&Dirty JPEG Image Similarity Checker v0.0.0.0 Alpha

 LANCZOS + MSE = 14.4 Sec
*BICUBIC + MSE = 12.2 Sec
 BICUBIC + ABS = 12.2 Sec
 LANCZOS + ABS = 14.4 Sec

 DIFF W/O GB < 128 - Basic
*DIFF W/O GB < 256 - Accurate
 DIFF With GB < 16 - Basic
 DIFF With GB < 32 - Accurate

Deeply inpired by:

https://www.raspberrypi.org/forums/viewtopic.php?t=195181#p1221857
https://www.pyimagesearch.com/2014/09/15/python-compare-two-images
https://www.quora.com/How-does-the-perceptual-image-hashing-work-and-how-do-you-implement-it
etc.

For complicated things, or if you want to do more general image processing OpenCV is a must.

NF, no (c) ;)

"""


def diff(image1, image2):
    image = [None, None]
    for im1, im2 in enumerate([image1, image2]):
        image[im1] = (np.array(im2
                       .convert('L')  # convert to grayscale
                       .resize((4, 4), resample=Image.BICUBIC)  # reduce size and smooth a bit
                       # .resize((4, 4), resample=Image.LANCZOS) # reduce size and smooth a bit
                       # .filter(ImageFilter.GaussianBlur(radius=2)) # optional GB filter
                       )).astype(np.int)  # convert from unsigned bytes to signed int using numpy
    # return np.abs(image[0] - image[1]).sum()
    return mse(image[0], image[1])


def mse(image0, image1):
    err = np.sum((image0.astype("float") - image1.astype("float")) ** 2)
    err /= float(image0.shape[0] * image0.shape[1])
    return err


def main():
    ProfilingStart = time.process_time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='folder with JPEG images')
    args = vars(parser.parse_args())
    img_format = '/*.jp*'

    images = []
    for file in glob.glob(args['path'] + img_format):
        path, name = os.path.split(file)
        im = Image.open(file)
        im.filename = name
        images.append(im)

    print('Process started! Please, wait ... ')

    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            if i == j:
                continue
            if 0 <= diff(images[i], images[j]) < 256:
                print(images[i].filename, images[j].filename)
                # print(diff(images[i], images[j]))

    print('Done! Time taken - ', time.process_time() - ProfilingStart, ' seconds')


if __name__ == '__main__':
    main()
