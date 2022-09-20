"""
@Target : image processing lab 2
@Author : JackyLiu
@Email  : 18922251299@163.com
@github :
@Date   : 2022/9/19 16:10
@Reference  : 
    1. show to using cv2 to operate image: https://blog.csdn.net/qq_40344307/article/details/93578188
    2.
@Source :
    
"""
from matplotlib import pyplot as plt
import numpy as np
from HW1.main import show_gray_image, show_original_image, get_gray_image


def even_change(image: np.ndarray, multiple: float) ->  np.ndarray:
    """
    input a image to return a image is even dark or even light
    """
    tmp_image = image * multiple
    print(tmp_image.shape)
    tmp_image[tmp_image < 0 ] = 0
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

def show_cdf(img: np.ndarray) -> None:
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    # Calculate the cumulative distribution map
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()


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
    img = cv2.imread("OIP-C.jpg", 0)
    print(img.shape)
    show_cdf(img)
    # gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    show_original_image(img)
    # cv2.imshow('img', img)

    # show cdf after equalizeHist
    equ = cv2.equalizeHist(img)
    show_cdf(equ)
    show_original_image(equ)



    # using cv2.equalizeHist to equalization




