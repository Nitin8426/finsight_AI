import React, { useState, useEffect } from 'react';
import Dashboard from '../components/Dashboard/Dashboard';
import { fetchResults } from '../services/resultsService';

const DashboardPage = () => {
    const [analysisResults, setAnalysisResults] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const results = await fetchResults();
                setAnalysisResults(results);
            } catch (err) {
                setError('Failed to fetch analysis results. Please try again later.');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    return (
        <div className="container">
            <h2>Dashboard</h2>
            {loading && <p>Loading...</p>}
            {error && <p className="error">{error}</p>}
            {!loading && !error && (
                <Dashboard analysisResults={analysisResults} />
            )}
        </div>
    );
};

export default DashboardPage;
