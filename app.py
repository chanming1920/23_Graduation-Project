from flask import Flask, request, render_template, send_from_directory
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/denoised_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def denoise_image(image_path):
    # 이미지 로드 및 디노이징 처리
    image = cv2.imread(image_path)
    # 여기서 이미지 디노이징 작업을 수행하세요 (예: 미디언 필터 사용)
    denoised_image = cv2.medianBlur(image, 5)
    return denoised_image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file part'
        image_file = request.files['image']
        if image_file.filename == '':
            return 'No selected file'
        if image_file:
            # 업로드된 이미지를 저장
            filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(filename)

            # 디노이징한 이미지 생성
            denoised_image = denoise_image(filename)
            denoised_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'denoised_' + image_file.filename)
            cv2.imwrite(denoised_filename, denoised_image)

            return render_template('index.html', original_image=image_file.filename, denoised_image='denoised_' + image_file.filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)