import React from 'react';
import { Line } from 'react-chartjs-2';

const Dashboard = ({ data }) => {
    const chartData = {
        labels: ['Revenue', 'Expenses', 'Profit'],
        datasets: [
            {
                label: 'Financial Metrics',
                data: [data.revenue, data.expenses, data.profit],
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)'],
            },
        ],
    };

    return (
        <div>
            <h2>Financial Dashboard</h2>
            <Line data={chartData} />
        </div>
    );
};

export default Dashboard;
