import React, { useState } from 'react';


const App = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);
  const [upscaledImage, setUpscaledImage] = useState(null);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(file);
        setPreviewImage(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleUpscale = async () => {
    const formData = new FormData();
    formData.append('image', selectedImage);
  
    try {
      const response = await fetch('http://localhost:5000/upscale', {
        method: 'POST',
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const result = await response.json();
  
      // Base64로 인코딩된 이미지를 화면에 표시
      setUpscaledImage(result.upscaled_image_url);
      
    } catch (error) {
      console.error('Error during upscale:', error);
    }
  };

  return (
    <div>
        <div>
            <h1 align="center">UPSCALE && FIXED IMAGE</h1>
            <hr />
            <p align="center">원하는 이미지를 선택해서 업스케일을 진행해보세요.</p>
            <p />
        </div>
        
        <div align="center">
          <input type="file" accept="image/*" onChange={handleImageChange} />
          {previewImage && <img src={previewImage} alt="Preview" style={{ maxWidth: '100px' }} />}
        </div>
        <div align="center">
          <button onClick={handleUpscale} >업스케일</button>
        </div>
        
        <div align="center"> 
          <hr />
          <p align="center">결과가 곧 출력됩니다....</p>
          {upscaledImage && <img src={upscaledImage} alt="Upscaled" style={{ maxWidth: '50%', width: '50%'}}/>}
        </div>
        
    </div>
  );
};

export default App;