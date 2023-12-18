import cv2
from cv2 import dnn_superres

option = 1
target_image=cv2.imread('./lenna/lenna/lenna_x3.png',option)
resize_image=cv2.imread('./lenna/lenna/lenna_x3.png',option)
resize_image=cv2.resize(resize_image,dsize=(0,0),fx=3,fy=3,interpolation=cv2.INTER_CUBIC)

cv2.imwrite('./Resized_Test.png',resize_image)
sr=dnn_superres.DnnSuperResImpl_create()

path='EDSR_x3.pb'
sr.readModel(path)
sr.setModel('edsr',3)
upscaled = sr.upsample(target_image)
cv2.imwrite('./Upscaled_Test.png',upscaled)


