import React, { useState, useEffect } from 'react';
import { fetchResults } from '../../services/resultsService';

const Dashboard = () => {
    const [results, setResults] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetchResults();
            if (!response.error) setResults(response.data);
        };

        fetchData();
    }, []);

    return (
        <div className="container mt-5">
            <h2>Dashboard</h2>
            {results.length > 0 ? (
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Analysis ID</th>
                            <th>Date</th>
                            <th>Revenue</th>
                            <th>Expenses</th>
                            <th>Profit</th>
                        </tr>
                    </thead>
                    <tbody>
                        {results.map((result) => (
                            <tr key={result.id}>
                                <td>{result.id}</td>
                                <td>{new Date(result.date).toLocaleDateString()}</td>
                                <td>{result.revenue}</td>
                                <td>{result.expenses}</td>
                                <td>{result.profit}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>No results to display. Upload data to get started!</p>
            )}
        </div>
    );
};

export default Dashboard;
