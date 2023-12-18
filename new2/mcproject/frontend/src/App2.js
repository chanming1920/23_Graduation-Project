import React, { useState } from 'react';
//import App from './App';

const App2 = () =>{
    const [noisedImage, setNoisedImage] = useState(null);
    
    const handleDenoise = async () => {
        const formData = new FormData();
        formData.append('image', noisedImage);
      
        try {
          const response = await fetch('http://localhost:5000/denoise', {
            method: 'POST',
            body: formData,
          });
      
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
      
          const result = await response.json();
      
          // Base64로 인코딩된 이미지를 화면에 표시
          setNoisedImage(result.denoised_img_url);
          
        } catch (error) {
          console.error('Error during upscale:', error);
        }
      };
    
    return (
        <div>
            <hr />
            <div align="center">
                <button onClick={handleDenoise}>디노이징</button>
            </div>
        </div>
    );
};

export default App2;
