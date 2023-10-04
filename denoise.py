import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('input_image.jpg')

# 가우시안 노이즈 추가
noise = np.random.normal(0, 25, image.shape).astype('uint8')
noisy_image = cv2.add(image, noise)

# 노이즈 제거 (미디언 필터 사용)
denoised_image = cv2.medianBlur(noisy_image, 5)

# 결과 이미지 저장
cv2.imwrite('denoised_image_python.jpg', denoised_image)
