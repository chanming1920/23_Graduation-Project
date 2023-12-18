import React, { useState } from 'react';

const Oderimage = () => {
  // 이미지 목록 상태
  const [images, setImages] = useState(['/']);

  // 현재 선택된 이미지 상태
  const [selectedImage, setSelectedImage] = useState(null);

  // 이미지를 클릭했을 때 호출되는 함수
  const handleImageClick = (image) => {
    setSelectedImage(image);
  };

  // 이미지 목록을 렌더링
  const renderImageList = () => {
    return (
      <div>
        {images.map((image, index) => (
          <img
            key={index}
            src={image}
            alt={`Image ${index + 1}`}
            onClick={() => handleImageClick(image)}
            style={{ width: '100px', height: '100px', margin: '5px', cursor: 'pointer' }}
          />
        ))}
      </div>
    );
  };

  // 선택된 이미지를 렌더링
  const renderSelectedImage = () => {
    return selectedImage && (
      <div>
        <img
          src={selectedImage}
          alt="Selected Image"
          style={{ width: '300px', height: '300px' }}
        />
      </div>
    );
  };

  return (
    <div>
      <h1>Google Photo Gallery</h1>
      {renderImageList()}
      {renderSelectedImage()}
    </div>
  );
};

export default Oderimage;