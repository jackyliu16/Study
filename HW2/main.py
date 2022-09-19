"""
@Target : 
@Annotation : 
@Author : JackyLiu
@Date   : 2022/9/19 16:10
@Reference  : 
    1.
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

# TODO using *args to cut down the number of arguments and using one function constant for zero and low value
def range_even_change(image: np.ndarray, multiple: float, left: int, right: int, func) -> np.ndarray:
    tmp = np.zeros(image.shape)
    for dim in range(0, image.shape[2]):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j][dim] >= left and image[i][j][dim] < right:
                    tmp[i][j][dim] = func(image[i][j][dim], multiple)
                else:
                    tmp[i][j][dim] = image[i][j][dim]
    return tmp

# implement of func
def even(num: int, multiple: int) -> int:
    return num * multiple

def zero(num: int, multiple:int ) -> int:
    return 0

def constant(num: int, multiple: int) -> int:
    return 50

if __name__ == "__main__":
    plt = plt.imread("OIP-C.jpg")

    # using gray image here for easy look
    plt_gray = get_gray_image(plt)
    show_original_image(plt_gray)

    # even light
    # lighted_img = even_change(plt_gray, 1.1)
    # show_original_image(lighted_img)

    # even dark
    # darked_img = even_change(plt_gray, 0.9)
    # show_original_image(darked_img)

    # Even brighter [100, 150)
    range_brighter = range_even_change(plt_gray, 1.1, 100, 150, even)
    show_original_image(range_brighter)

    # for [0, 80) and [150, 255) low grey value
    tmp_a = range_even_change(plt_gray, 0, 0, 80, constant)
    low_grey = range_even_change(tmp_a, 0, 150, 255, constant)
    show_original_image(low_grey)
    # 0 value
    tmp_b = range_even_change(plt_gray, 0, 0, 80, zero)
    zero_graph = range_even_change(tmp_a, 0, 150, 255, zero)
    show_original_image(zero_graph)

    print("end")


