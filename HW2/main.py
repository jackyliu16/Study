"""
@Target : image processing lab 2
@Author : JackyLiu
@Email  : 18922251299@163.com
@github :
@Date   : 2022/9/19 16:10
@Reference  : 
    1. show to using cv2 to operate image:  https://blog.csdn.net/qq_40344307/article/details/93578188
    2. how to histogram specification :     https://blog.csdn.net/qq_38328871/article/details/85056234
@Source :
    https://cn.bing.com/images/
"""
import random
from math import fabs

import numpy as np
from matplotlib import pyplot as plt

from HW1.main import show_original_image


def even_change(image: np.ndarray, multiple: float) -> np.ndarray:
    """
    input a image to return a image is even dark or even light
    """
    tmp_image = image * multiple
    print(tmp_image.shape)
    tmp_image[tmp_image < 0] = 0
    tmp_image[tmp_image > 255] = 255
    return tmp_image


# TODO using List derivation to simplify function
def range_even_change(image: np.ndarray, left: int, right: int, func, *args) -> np.ndarray:
    tmp = np.zeros(image.shape)
    for dim in range(0, image.shape[2]):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j][dim] >= left and image[i][j][dim] < right:
                    tmp[i][j][dim] = func(image[i][j][dim], args[0])
                else:
                    tmp[i][j][dim] = image[i][j][dim]
    return tmp


# implement of func
def even(num: int, multiple: int) -> int:
    return num * multiple


def constant(num: int, constant: int) -> int:
    return constant


# https://blog.csdn.net/qq_40344307/article/details/93578188
# i was boring implement the traditional ways to implement the function, thus using cv2
import cv2

def get_cdf_and_histogram(img: np.ndarray) -> np.ndarray:
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    return cdf_normalized


def show_cdf_and_histogram(img: np.ndarray, title: str = "") -> None:
    cdf_normal = get_cdf_and_histogram(img)
    plt.plot(cdf_normal, color='r')
    plt.hist(img.flatten(), 256, [0, 256], color='b')
    plt.xlim([0, 256])
    plt.title(title)
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


def get_diff_between_two_cdf(img_a: np.ndarray, img_b: np.ndarray) -> list[int]:
    """
    return the different of two cdf_normalized
    reference: https://blog.csdn.net/qq_38328871/article/details/85056234
    """
    """ As same as below
    diff_cdf = [[ 0 for i in range(256)] for j in range(256)]
    for i in range(256):
        for j in range(256):
            diff_cdf[i][j] = fabs(src[i] - normal[j])
    """
    print(f"src.shape:{img_a.shape}, normal.shape:{img_b.shape}")
    # collect the different between two cdf histogram
    diff_cdf = [[fabs(img_a[i] - img_b[j]) for j in range(256)] for i in range(256)]

    # for gery value finding the min value and it's index
    # TODO finish this action with color image but not gery image
    lut = [0 for i in range(256)]
    for i in range(256):
        min = diff_cdf[i][0]
        index = 0
        for j in range(256):
            if min > diff_cdf[i][j]:
                min = diff_cdf[i][j]
                index = j
        lut[i] = ([i, index])
    return lut


def regularization(img_src: np.ndarray, img_normal: np.ndarray):
    lut = get_diff_between_two_cdf(get_cdf_and_histogram(img_src), get_cdf_and_histogram(img_normal))
    print(f"img.src.shape:{img_src.shape}, lut.type{len(lut)}, lut:{lut}")
    for i in range(img_src.shape[0]):
        for j in range(img_src.shape[1]):
            img_src[i][j] = lut[img_src[i][j]][1]
    show_cdf_and_histogram(img_src, title="histogram specification - output")
    show_original_image(img_src, title="histogram specification - output")

# 本来想只做灰度的，但是灰度的话show_origin_image函数没有办法正常运行
def gaussian_noise(img: np.ndarray, mean=0, sigma=0.01):
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, sigma ** 0.5, img.shape)
    out = img + noise
    out[out > 255] = 255
    out[out < 0  ] = 0
    out = np.uint8(out * 255)
    return out


def sp_noise(img: np.ndarray, prob):
    out = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                out[i][j] = 0
            elif rdn > thres:
                out[i][j] = 255
            else:
                out[i][j] = img[i][j]
    return out

def sharpen(img: np.ndarray):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])
    out = cv2.filter2D(img, -1, kernel=kernel)
    return out

if __name__ == "__main__":
    # img_1 = plt.imread("OIP-C.jpg")
    #
    # using gray image here for easy look
    # plt_gray = get_gray_image(img_1)
    # show_original_image(plt_gray)
    #
    # even light
    # lighted_img = even_change(plt_gray, 1.1)
    # show_original_image(lighted_img)
    #
    # even dark
    # darked_img = even_change(plt_gray, 0.9)
    # show_original_image(darked_img)
    #
    # Even brighter [100, 150)
    # range_brighter = range_even_change(plt_gray, 1.1, 100, 150, even)
    # show_original_image(range_brighter)
    #
    # for [0, 80) and [150, 255) low grey value
    # tmp_a = range_even_change(plt_gray, 0, 80, constant, 50)
    # low_grey = range_even_change(tmp_a, 150, 255, constant, 50)
    # show_original_image(low_grey)
    # 0 value
    # tmp_b = range_even_change(plt_gray, 0, 80, constant, 0)
    # zero_graph = range_even_change(tmp_a, 150, 255, constant, 0)
    # show_original_image(zero_graph)

    # TODO haven't functional

    # show original image cdf
    # show cdf right now
    # img = cv2.imread("OIP-C.jpg", 0)
    # show_cdf_and_histogram(img, title="histogram equalization - input")
    # show_original_image(img, title="histogram equalization - input#")
    #
    # equ = cv2.equalizeHist(img)
    # show_cdf_and_histogram(equ, title="histogram equalization - output")
    # show_original_image(equ, title="histogram equalization - output")
    #
    # img2 = cv2.imread("R-C.jfif", 0)
    # show_cdf_and_histogram(img2, title="histogram specification - standard")
    # show_original_image(img2, title="histogram specification - standard")
    # regularization(img, img2)

    # using cv2.equalizeHist to equalization

    ##### 4 #####

    img3 = cv2.imread("R-C.jfif")
    show_original_image(img3, title='no noise')
    img4 = gaussian_noise(img3)
    show_original_image(img4, title='gaussian noise')
    img5 = sp_noise(img3, 0.05)
    show_original_image(img5, title='sp noise')
    img6 = sharpen(img3)
    show_original_image(img6)




# Recode of different ways
"""
图像灰度直方图的呈现
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist_full)
plt.show()
"""
