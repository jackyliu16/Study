"""
@author: jackyLiu
@email:  18922251299@163.com
@Lab Report Address: https://e3vqhv9jh5.feishu.cn/docx/doxcnAr018n4zQPnfXtojLzTcsh
"""
# Lib
from matplotlib import pyplot as plt
import numpy as np

def show_original_image(image: np.ndarray) -> None:
    plt.imshow(image.astype('int'))
    # plt.suptitle('original image')
    plt.show()

def show_gray_image(image: np.ndarray) -> None:
    gray = get_gray_image(image)
    plt.imshow(gray.astype('int'))
    plt.show()

def show_binary_image(image: np.ndarray) -> None:
    bin = get_binary_image(image)
    plt.imshow(bin.astype('int'))
    plt.show()

def add_and_show_two_image(image_a: np.ndarray, image_b: np.ndarray) -> None:
    plt.imshow(image_a.astype('int'), alpha=0.5)
    plt.imshow(image_b.astype('int'), alpha=0.5)
    plt.show()
    # add_image = image_a + image_b
    # add_image = normalization(add_image, left=0, right=255)
    # plt.imshow(add_image.astype('int'))
    # plt.show()

# Method of image convert

def get_gray_image(image: np.ndarray) -> np.ndarray :
    Y = image[:,:,0] * 0.299 + image[:,:,1] * 0.587 + image[:, :, 2] * 0.114
    gray = np.zeros((Y.shape[0], Y.shape[1], 3))
    gray[:,:,0] = gray[:,:,1] = gray[:, :, 2] = Y                               # create a image with same value 
    return gray

def get_binary_image(image: np.ndarray) -> np.ndarray:
    # convert to grey
    Y = image[:,:,0] * 0.299 + image[:,:,1] * 0.587 + image[:, :, 2] * 0.114
    # binaryzation
    Y[Y<=128] = 0
    Y[Y>128] = 255
    # putting it back into a image to show 
    gray = np.zeros((Y.shape[0], Y.shape[1], 3))
    gray[:,:,0] = gray[:,:,1] = gray[:, :, 2] = Y                               # create a image with same value 
    return gray

# Method about statistics

def get_grey_level_histogram(image: np.ndarray) -> None:
    plt.hist(image.ravel(), bins=256, fc='k', ec='k')
    plt.show()

def get_hist_normalization_image(image: np.ndarray) -> np.ndarray:
    normalizaiton_hist: np.ndarray = normalization(image)
    plt.hist(normalizaiton_hist.ravel(), bins=256, fc='k', ec='k')
    plt.show()

#[deprecated]
def normalize(_d, to_sum=True, copy=True):
    # d is a (n x dimension) np array
    d = _d if not copy else np.copy(_d)
    d -= np.min(d, axis=0)
    d /= (np.sum(d, axis=0) if to_sum else np.ptp(d, axis=0))
    return d 


def normalization(img: np.ndarray, left=0, right=1) -> np.ndarray:
    """
    convert img[min, max] to [left, right]

    min                                                     ( if   x < c )
    ( right - left ) / ( max - min ) * ( x - min ) + left   ( elif min <= x < max)
    max                                                     ( else )
    """
    # init
    min, max = img.min(), img.max()
    out = img.copy()

    # normalization
    out = ( right - left ) / ( max - min ) * ( out - min ) + left
    out[out < left] = left
    out[out > right] = right

    return out

if __name__ == "__main__":
    path = "./HW1./OIP-C.jpg"
    x = plt.imread(path)
    plt.imshow(x.astype('int'))
    plt.show()

    # # Question 1
    show_gray_image(x)
    show_binary_image(x)

    # # Question 2
    get_grey_level_histogram(x)
    get_hist_normalization_image(x)

    # # Question 3
    background  = plt.imread("./HW1./background.jpg")
    chicken     = plt.imread("./HW1./chicken.jpg")
    add_and_show_two_image(background, chicken)


