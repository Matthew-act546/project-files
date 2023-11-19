import sys, os, random, argparse
from PIL import Image
import imghdr
import numpy as np

def getAverageRGB(image):
    """
    return the average color value as (r, g, b) for each input image
    """
    # get each tile image as a numpy array
    im = np.array(image)
    # get the shape of each input image
    w,h,d = im.shape
    # get the average RGB value
    return tuple(np.average(im.reshape(w*h, d), axis=0))

def splitImage(image, size):
    """
    given the image and dimensions (rows, cols), returns an m*n list of images
     """
    W, H = image.size[0], image.size[1]
    m, n = size
    w, h = int(W/n), int(H/m)
    # image list
    imgs = []
 # generate a list of dimensions
    for j in range(m):
        for i in range(n):
            # append cropped image
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs

def getImages(imageDir):
    """
    given a directory of images, return a list of Images
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            # explicit load so we don't run into a resource crunch
            fp = open(filePath, "rb")
            im = Image.open(fp)
            images.append(im)
            # force loading image data from file
            im.load()
            # close the file
            fp.close()
        except:
            print("Invalid image: %s" % (filePath,))
    return images

def getImageFilenames(imageDir):
    """
    given a directory of images, return a list of image filenames
    """
    files = os.listdir(imageDir)
    filenames = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            imgType = imghdr.what(filePath)
            if imgType:
                filenames.append(filePath)
        except:
            # skip
            print("Invalid image: %s" % (filePath,))
    return filenames

def getBestMatchIndex(input_avg, avgs):
    """
    return index of the best image match based on average RGB value distance
    """
    # input image average
    avg = input_avg

    # get the closest RGB value to input, based on RGB distance
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0])*(val[0] - avg[0]) +
            (val[1] - avg[1])*(val[1] - avg[1]) +
            (val[2] - avg[2])*(val[2] - avg[2]))
        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1
    return min_index

def createImageGrid(images, dims):
    """
    given a list of images and a grid size (m, n), create a grid of images
    """
    m, n = dims

    # sanity check
    assert m*n == len(images)

    # get the maximum height and width of the images
    # don't assume they're all equal
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    # create the target image
    grid_img = Image.new('RGB', (n*width, m*height))

 # paste the tile images into the image grid
    for index in range(len(images)):
        row = int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))
    return grid_img

def createPhotomosaic(target_image, input_images, grid_size, reuse_images=True):
    """
    creates photomosaic given target and input images
    """
    print('splitting input image...')
    # split the target image into tiles
    target_images = splitImage(target_image, grid_size)
    print('finding image matches...')
    # for each tile, pick one matching input image
    output_images = []
    # for user feedback
    count = 0
    batch_size = int(len(target_images)/10)
    # calculate the average of the input image
    avgs = []
    for img in input_images:
        avgs.append(getAverageRGB(img))
    for img in target_images:
        # compute the average RGB value of the image
        avg = getAverageRGB(img)
        # find the matching index of closest RGB value
        # from a list of average RGB values
        match_index = getBestMatchIndex(avg, avgs)
        output_images.append(input_images[match_index])
 # user feedback
        if count > 0 and batch_size > 10 and count % batch_size is 0:
            print('processed %d of %d...' %(count, len(target_images)))
        count += 1
 # remove the selected image from input if flag set
        if not reuse_images:
            input_images.remove(match)
        
    print('creating mosaic...')
    # create photomosaic image from tiles
    mosaic_image = createImageGrid(output_images, grid_size)
    # display the mosaic
    return mosaic_image
# gather our code in a main() function
def main():
    # command line arguments are in sys.argv[1], sys.argv[2], ...
    # sys.argv[0] is the script name itself and can be ignored

    # parse arguments
    parser = argparse.ArgumentParser(description='Creates a photomosaic from input images')
    # add arguments
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)
    args = parser.parse_args()
    ###### INPUTS ######
    # target image
    target_image = Image.open(args.target_image)
     # input images
    print('reading input folder...')
    input_images = getImages(args.input_folder)
    # check if any valid input images found
    if input_images == []:
        print('No input images found in %s. Exiting.' % (args.input_folder, ))
        exit()
 # shuffle list to get a more varied output?
    random.shuffle(input_images)
 # size of the grid
    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))
    # output
    output_filename = 'mosaic.png'
    if args.outfile:
        output_filename = args.outfile

    # reuse any image in input
    reuse_images = True
    # resize the input to fit the original image size?
    resize_input = True
    ##### END INPUTS #####
    print('starting photomosaic creation...')

    # if images can't be reused, ensure m*n <= num_of_images
    if not reuse_images:
        if grid_size[0]*grid_size[1] > len(input_images):
            print('grid size less than number of images')
            exit()

    # resizing input
    if resize_input:
        print('resizing images...')
    # for given grid size, compute the maximum width and height of tiles
    dims = (int(target_image.size[0]/grid_size[1]),
    int(target_image.size[1]/grid_size[0]))
    print("max tile dims: %s" % (dims,))
    # resize
    for img in input_images:
        img.thumbnail(dims)
    # create photomosaic
    mosaic_image = createPhotomosaic(target_image, input_images, grid_size, reuse_images)
    # write out mosaic
    mosaic_image.save(output_filename, 'PNG')
    print("saved output to %s" % (output_filename,))
    print('done.')

# standard boilerplate to call the main() function
# to begin the program
if __name__ == '__main__':
    main()