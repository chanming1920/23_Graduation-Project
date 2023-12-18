import cv2
from PIL import Image
import numpy as np
import math

def psnr(ori_img, con_img):

  
  
  # 해당 이미지의 최대값 (채널 최대값 - 최솟값)
  max_pixel = 255.0

  # MSE 계산
  mse = np.mean((ori_img - con_img)**2)

  if mse ==0:
    return 100
  
  # PSNR 계산
  psnr = 20* math.log10(max_pixel / math.sqrt(mse))
  
  return psnr

ori_img = cv2.imread('lenna\lenna\lenna.png')
con_img = cv2.imread('Upscaled_Test.png')

print("Up : ",psnr(ori_img,con_img))