#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Target  ：
@Author  ：jackyliu
@Date    ：2021/12/11 13:30 
'''
import cv2

img_gary = cv2.imread("881259.png",cv2.IMREAD_GRAYSCALE)
ret, img = cv2.threshold(img_gary,50,255,cv2.THRESH_BINARY)
cv2.imwrite("output.png",img)