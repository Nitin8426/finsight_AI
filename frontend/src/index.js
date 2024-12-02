import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app'; // Correct if the file is App.js
import './app.css';

// Create the root element and render the application
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
