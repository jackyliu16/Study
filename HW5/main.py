# PyWavelets - Wavelet Transforms in Python — PyWavelets Documentation
 
import cv2
import numpy as np
from pywt import dwt2, idwt2, cwt
import matplotlib.pyplot as plt#用于显示图片

##################################################################################
############################遍历图像，将高频点置0#################################
##################################################################################
def tool_Denoising(inputGrayPic,value):
    result = inputGrayPic

    height = result.shape[0]
    weight = result.shape[1]

    for row in range(height):
        for col in range(weight):
            result[row, col]
            if (abs(result[row, col]) > value):
                print(abs(result[row, col]))
                result[row, col] = 0#频率的数值0为低频
    return result


#读取灰度图
img = cv2.imread('../images/arnold-b-cklin_fighting-on-a-bridge.jpg',0)

#cA，cH,cV,cD 分别为近似分量(低频分量)、水平细节分量、垂直细节分量和对角细节分量
cA,(cH,cV,cD)=dwt2(img,'haar')#dwt2函数第二个参数指定小波基

#打印语句
#plt.subplot(232), plt.imshow(cA, 'gray'), plt.title('cA')
#plt.subplot(233), plt.imshow(cH, 'gray'), plt.title('cH')
#plt.subplot(234), plt.imshow(cV, 'gray'), plt.title('cV')
#plt.subplot(235), plt.imshow(cD, 'gray'), plt.title('cD')

#设置去噪阈值。因为噪音一般都是高频信息，遍历像素，将VALUE的像素点置0
VALUE = 60
#处理低频
#cA = tool_Denoising(cA,100)
#处理水平高频
cH = tool_Denoising(cH,VALUE)
#处理垂直高频
cV = tool_Denoising(cV,VALUE)
#处理对角线高频
cD = tool_Denoising(cD,VALUE)
#重构图像
rebuild = idwt2((cA,(cH,cV,cD)), 'haar')

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('img')
plt.subplot(232), plt.imshow(cA, 'gray'), plt.title('cA')
plt.subplot(233), plt.imshow(cH, 'gray'), plt.title('cH')
plt.subplot(234), plt.imshow(cV, 'gray'), plt.title('cV')
plt.subplot(235), plt.imshow(cD, 'gray'), plt.title('cD')
plt.subplot(236), plt.imshow(rebuild, 'gray'), plt.title('rebuild')
plt.show()


