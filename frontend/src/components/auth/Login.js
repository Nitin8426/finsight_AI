import React, { useState } from 'react';
import { login } from '../../services/authService';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (event) => {
        event.preventDefault();
        setError('');

        try {
            const response = await login({ username, password });
            if (response.success) {
                localStorage.setItem('token', response.token); // Save token for authentication
                navigate('/dashboard'); // Redirect to the dashboard on successful login
            } else {
                setError(response.message || 'Invalid username or password.');
            }
        } catch (err) {
            setError('An error occurred during login. Please try again later.');
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
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
                <button type="submit" className="btn btn-primary">
                    Login
                </button>
            </form>
            {error && <p className="error">{error}</p>}
            <p>
                Don't have an account? <a href="/register">Register here</a>
            </p>
        </div>
    );
};

export default Login;
