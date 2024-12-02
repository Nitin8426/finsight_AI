import React, { useState } from 'react';

const FileUpload = () => {
    const [file, setFile] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("file", file);

        fetch('/upload', { method: "POST", body: formData })
            .then((response) => response.json())
            .then((data) => console.log(data))
            .catch((error) => console.error("Error:", error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" onChange={(e) => setFile(e.target.files[0])} />
            <button type="submit">Upload</button>
        </form>
    );
};

export default FileUpload;
