import cv2
from cv2 import dnn_superres
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
from PIL import Image
import io
import base64
import numpy as np

app = Flask(__name__)

CORS(app)

# 이미지를 저장할 디렉토리 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# OpenCV의 Super-Resolution 모듈 초기화
sr = dnn_superres.DnnSuperResImpl_create()

@app.route('/denoise', methods=['POST'])
def denoise_image():
    try:
        image = request.files['image']

        chageimage = cv2.imread(image)
        fiximage = cv2.denoise_TVL1(chageimage)
        
        denoised_img = Image.fromarray(fiximage)
        output_buffer2 = io.BytesIO()
        denoised_img.save(output_buffer2, format='JPEG')
        output_buffer2.seek(0)

        result = {'denoised_img_url': 'data:image/jpeg;base64,' + base64.b64encode(output_buffer2.read()).decode('utf-8')}
        print('Success')
        return jsonify(result)
    except Exception as e:
        print('denising failed:', str(e))
        return jsonify({'error': str(e)})

    
@app.route('/upscale', methods=['POST'])
def upscale_image():
    try:
        # 요청에서 이미지 파일 받기
        if 'image' not in request.files:
            return jsonify({'error': '이미지가 제공되지 않았습니다'})

        image = request.files['image']

        if image.filename == '':
            return jsonify({'error': '선택된 이미지가 없습니다'})
        
        # 이미지 파일에 안전한 이름으로 저장
        filename = secure_filename(image.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # 'uploads' 디렉토리 생성
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        image.save(save_path)

        # 이미지 업스케일
        path = './EDSR_x3.pb'  # 모델 파일의 경로를 업데이트하세요
        print(f'Model loading: {path}')
        sr.readModel(path)
        print('Model reading complete')
        sr.setModel('edsr', 3)  
        print('Model loading done')
       
        
        # 저장된 이미지를 읽기 위해 전체 경로 사용
        option = 1
        target_image = cv2.imread(save_path,option)
        target = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)
        
        # 이미지 업스케일 수행
        print('Upscaleing')
        upscaled = sr.upsample(target)

        # 업스케일된 이미지를 클라이언트에게 전송
        upscaled_img = Image.fromarray(upscaled)
        output_buffer = io.BytesIO()
        upscaled_img.save(output_buffer, format='JPEG')
        output_buffer.seek(0)

        result = {'upscaled_image_url': 'data:image/jpeg;base64,' + base64.b64encode(output_buffer.read()).decode('utf-8')}
        print('Success')
        return jsonify(result)
    except Exception as e:
        print('업스케일 실패:', str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)