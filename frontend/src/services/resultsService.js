const API_URL = process.env.REACT_APP_API_URL;

export const fetchResults = async () => {
    const response = await fetch(`${API_URL}/fetch_results`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    });
    return response.json();
};

export const fetchAnalysisResults = async () => {
    const response = await fetch(`${API_URL}/results`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    });
    return response.json();
};
