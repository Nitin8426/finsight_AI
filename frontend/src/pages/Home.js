import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div className="container mt-5 text-center">
            <h1>Welcome to MSME Financial Analysis</h1>
            <p>Analyze your financial data and get AI-driven insights.</p>
            <Link to="/login" className="btn btn-primary">Get Started</Link>
        </div>
    );
};

export default HomePage;
