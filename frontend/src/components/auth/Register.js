import React, { useState } from 'react';
import { register } from '../../services/authService';
import { useNavigate } from 'react-router-dom';

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const navigate = useNavigate();

    const handleRegister = async (event) => {
        event.preventDefault();
        setError('');
        setSuccessMessage('');

        if (password !== confirmPassword) {
            setError('Passwords do not match.');
            return;
        }

        try {
            const response = await register({ username, password });
            if (response.success) {
                setSuccessMessage('Registration successful! Redirecting to login...');
                setTimeout(() => navigate('/login'), 3000); // Redirect after 3 seconds
            } else {
                setError(response.message || 'Registration failed. Please try again.');
            }
        } catch (err) {
            setError('An error occurred during registration. Please try again later.');
        }
    };

    return (
        <div className="register-container">
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <div className="form-group">
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        className="form-control"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        className="form-control"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="confirmPassword">Confirm Password:</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        className="form-control"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    Register
                </button>
            </form>
            {error && <p className="error">{error}</p>}
            {successMessage && <p className="success">{successMessage}</p>}
            <p>
                Already have an account? <a href="/login">Login here</a>
            </p>
        </div>
    );
};

export default Register;
