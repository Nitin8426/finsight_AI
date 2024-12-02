import React, { useState } from 'react';
import { uploadFile } from '../services/fileService';

const UploadPage = () => {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState('');

    const handleFileChange = (e) => setFile(e.target.files[0]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;
        const response = await uploadFile(file);
        if (response.error) setMessage(response.error);
        else setMessage('File uploaded successfully. Processing...');
    };

    return (
        <div className="container mt-5">
            <h2>Upload Financial Data</h2>
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} required />
                <button type="submit" className="btn btn-primary mt-2">Upload</button>
            </form>
        </div>
    );
};

export default UploadPage;
