const API_URL = process.env.REACT_APP_API_URL;

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(`${API_URL}/upload`, {
        method: 'POST',
        body: formData,
    });
    return response.json();
};
