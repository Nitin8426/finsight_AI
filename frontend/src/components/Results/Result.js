import React, { useEffect, useState } from 'react';
import BarChart from './BarChart';
import LineChart from './LineChart';
import PieChart from './PieChart';
import { fetchResults } from '../../services/resultsService';

const Results = () => {
    const [analysisResults, setAnalysisResults] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const getResults = async () => {
            try {
                const response = await fetchResults();
                if (response.success) {
                    setAnalysisResults(response.data);
                } else {
                    setError(response.message || 'Failed to fetch results.');
                }
            } catch (err) {
                setError('An error occurred while fetching the results.');
            }
        };

        getResults();
    }, []);

    if (error) {
        return <div className="error-container">{error}</div>;
    }

    if (!analysisResults) {
        return <div className="loading-container">Loading results...</div>;
    }

    return (
        <div className="results-container">
            <h2>Financial Analysis Results</h2>
            <div className="results-summary">
                <h3>Summary</h3>
                <p><strong>Total Revenue:</strong> {analysisResults.totalRevenue}</p>
                <p><strong>Total Expenses:</strong> {analysisResults.totalExpenses}</p>
                <p><strong>Net Profit:</strong> {analysisResults.netProfit}</p>
            </div>

            <div className="charts-container">
                <h3>Visualizations</h3>
                <div className="chart">
                    <BarChart data={analysisResults.barChartData} />
                </div>
                <div className="chart">
                    <LineChart data={analysisResults.lineChartData} />
                </div>
                <div className="chart">
                    <PieChart data={analysisResults.pieChartData} />
                </div>
            </div>
        </div>
    );
};

export default Results;
