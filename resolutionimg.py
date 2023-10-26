import cv2

# 이미지를 불러옵니다.
input_image = cv2.imread('dog2.jpg')

# fastNlMeansDenoisingColored 함수를 사용하여 노이즈 제거
denoised_image = cv2.fastNlMeansDenoisingColored(input_image, None, 10, 10, 7, 21)

# 이미지 해상도를 높이기 위해 이미지를 복제하고 확대
scaling_factor = 2  # 2배 확대
height, width, _ = denoised_image.shape
new_height, new_width = height * scaling_factor, width * scaling_factor

# cv2.INTER_LINEAR 보간 알고리즘을 사용하여 이미지를 확대
improved_resolution_image = cv2.resize(denoised_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# 결과 이미지의 크기 가져오기
result_height, result_width, _ = improved_resolution_image.shape

# 화면 크기 얻기
screen_width = 1280  # 화면 가로 해상도
screen_height = 720  # 화면 세로 해상도

# 이미지가 화면에 맞도록 크기 조정
if result_height > screen_height or result_width > screen_width:
    scale = min(screen_width / result_width, screen_height / result_height)
    new_width = int(result_width * scale)
    new_height = int(result_height * scale)
    improved_resolution_image = cv2.resize(improved_resolution_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# 이미지를 화면에 표시
cv2.imshow('Improved Resolution Image', improved_resolution_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과 이미지를 저장
#cv2.imwrite('improved_resolution_image.jpg', improved_resolution_image)