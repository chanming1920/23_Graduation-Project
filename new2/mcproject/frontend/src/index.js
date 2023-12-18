import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
//import App2 from './App2';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// const root1 = ReactDOM.createRoot(document.getElementById('root1'));
// root1.render(
//   <React.StrictMode>
//     <App2 />
//   </React.StrictMode>
// );

reportWebVitals();
