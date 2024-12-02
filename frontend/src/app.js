import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home';
import LoginPage from './pages/LoginPage';
import RegistrationPage from './pages/RegistrationPage';
import UploadPage from './pages/UploadPage';
import ResultsPage from './pages/ResultsPage';
import DashboardPage from './pages/DashboardPage';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegistrationPage />} />
                <Route path="/upload" element={<UploadPage />} />
                <Route path="/results" element={<ResultsPage />} />
                <Route path="/dashboard" element={<DashboardPage />} />
            </Routes>
        </Router>
    );
};

export default App;
