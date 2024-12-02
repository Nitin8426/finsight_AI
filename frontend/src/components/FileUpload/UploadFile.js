import React, { useState } from 'react';
import { uploadFile } from '../../services/fileService';

const UploadFile = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState('');
    const [error, setError] = useState('');

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
        setUploadStatus('');
        setError('');
    };

    const handleUpload = async (event) => {
        event.preventDefault();

        if (!selectedFile) {
            setError('Please select a file before uploading.');
            return;
        }

        try {
            const response = await uploadFile(selectedFile);
            if (response.success) {
                setUploadStatus('File uploaded successfully!');
            } else {
                setError(response.message || 'Failed to upload the file.');
            }
        } catch (err) {
            setError('An error occurred while uploading the file. Please try again.');
        }
    };

    return (
        <div className="upload-container">
            <form onSubmit={handleUpload}>
                <div className="form-group">
                    <label htmlFor="file">Upload Financial Data (CSV):</label>
                    <input
                        type="file"
                        id="file"
                        className="form-control"
                        accept=".csv"
                        onChange={handleFileChange}
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    Upload and Analyze
                </button>
            </form>
            {uploadStatus && <p className="success">{uploadStatus}</p>}
            {error && <p className="error">{error}</p>}
        </div>
    );
};

export default UploadFile;
