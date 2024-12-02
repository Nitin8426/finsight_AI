import React, { useState, useEffect } from 'react';
import BarChart from '../components/Results/BarChart';
import LineChart from '../components/Results/LineChart';
import PieChart from '../components/Results/PieChart';
import { fetchAnalysisResults } from '../services/resultsService';

const ResultsPage = () => {
    const [analysis, setAnalysis] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchResults = async () => {
            const response = await fetchAnalysisResults();
            if (response.error) setError(response.error);
            else setAnalysis(response.data);
        };

        fetchResults();
    }, []);

    return (
        <div className="container mt-5">
            <h2>Financial Analysis Results</h2>
            {error && <p className="text-danger">{error}</p>}
            {analysis ? (
                <div>
                    <p><strong>Revenue:</strong> {analysis.revenue}</p>
                    <p><strong>Expenses:</strong> {analysis.expenses}</p>
                    <p><strong>Profit:</strong> {analysis.profit}</p>

                    <div className="chart-section">
                        <BarChart src="/assets/charts/bar_chart.png" />
                        <LineChart src="/assets/charts/line_chart.png" />
                        <PieChart src="/assets/charts/pie_chart.png" />
                    </div>
                </div>
            ) : (
                <p>Loading analysis...</p>
            )}
        </div>
    );
};

export default ResultsPage;
