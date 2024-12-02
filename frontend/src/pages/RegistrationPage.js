import React, { useState } from 'react';
import { register } from '../services/authService';

const RegistrationPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [success, setSuccess] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await register(username, password);
        if (response.error) setError(response.error);
        else setSuccess('Registration successful. Please log in.');
    };

    return (
        <div className="container mt-5">
            <h2>Register</h2>
            {success && <p className="text-success">{success}</p>}
            {error && <p className="text-danger">{error}</p>}
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label>Username</label>
                    <input type="text" className="form-control" value={username} onChange={(e) => setUsername(e.target.value)} required />
                </div>
                <div className="mb-3">
                    <label>Password</label>
                    <input type="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>
                <button type="submit" className="btn btn-primary">Register</button>
            </form>
        </div>
    );
};

export default RegistrationPage;
