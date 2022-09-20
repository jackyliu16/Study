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

# reference: https://www.cnblogs.com/dpy-study/p/15602974.html#:~:text=1.%E7%9B%B4%E6%96%B9%E5%9B%BE%E5%9D%87%E8%A1%A1%E5%8C%96%EF%BC%88%E4%BD%BF%E7%94%A8python%E5%AE%8C%E6%88%90%EF%BC%89%EF%BC%9A%20%E2%91%A0%EF%BC%9A%E8%AE%A1%E7%AE%97%E5%9B%BE%E7%89%87%E5%8E%9F%E5%A7%8B%E7%9A%84%E7%81%B0%E5%BA%A6%E5%88%86%E5%B8%83%EF%BC%9A%20def%20Grayscale_Probability%20%28img%29%3A%20%23%20%E8%BE%93%E5%85%A5,img%20%E6%98%AF%E8%AF%BB%E5%8F%96%E5%90%8E%E7%9A%84%E7%81%B0%E5%BA%A6%E5%9B%BE%20%E6%95%B0%E6%8D%AE%20prob%20%3D%20torch.zeros%20%28256%29
# https://blog.csdn.net/qq_40344307/article/details/93578188

if __name__ == "__main__":
    plt = plt.imread("OIP-C.jpg")

    # using gray image here for easy look
    plt_gray = get_gray_image(plt)
    show_original_image(plt_gray)

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




    print("end")


