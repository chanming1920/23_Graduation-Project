import tensorflow as tf
import cv2
import numpy as np

# 모델 파일 경로
model_path = "EDSR_x3.tflite"

# 입력 이미지 경로
image_path = "lenna\lenna\lenna_x3.png"

# TensorFlow Lite 모델 로드
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# 입력 이미지 읽기
image = cv2.imread(image_path)

# 입력 이미지 전처리 (모델에 맞게 조정)
input_details = interpreter.get_input_details()
input_tensor_index = input_details[0]['index']
input_shape = input_details[0]['shape'][1:3]

input_data = cv2.resize(image, (input_shape[1], input_shape[0]))
input_data = input_data.astype(np.float32) / 255.0
input_data = np.expand_dims(input_data, axis=0)

interpreter.set_tensor(input_tensor_index, input_data)

# 모델 실행
interpreter.invoke()

# 결과 처리 (원하는 대로 사용)
# 여기서는 결과를 화면에 표시하고 저장하는 예제를 제공합니다.
output_details = interpreter.get_output_details()
output_tensor_index = output_details[0]['index']
output_data = interpreter.get_tensor(output_tensor_index)

cv2.imshow("Input Image", image)
cv2.imshow("Output Image", (output_data[0] * 255).astype(np.uint8))
cv2.waitKey(0)

# 결과 이미지 저장
cv2.imwrite("output_image.jpg", (output_data[0] * 255).astype(np.uint8))