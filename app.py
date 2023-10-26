import cv2
import os
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']

        if file.filename == '':
            return "No selected file"
        
        if file:
            # 저장된 이미지 경로
            file_path = 'static/uploaded_image.jpg'
            file.save(file_path)

            # 이미지 처리 코드
            input_image = cv2.imread(file_path)
            denoised_image = cv2.fastNlMeansDenoisingColored(input_image, None, 10, 10, 7, 21)
            scaling_factor = 2  # 2배 확대
            new_height, new_width = denoised_image.shape[0] * scaling_factor, denoised_image.shape[1] * scaling_factor
            improved_resolution_image = cv2.resize(denoised_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
            cv2.imwrite('static/improved_resolution_image.jpg', improved_resolution_image)

    return render_template('Basic.html')

if __name__ == '__main__':
    app.run()