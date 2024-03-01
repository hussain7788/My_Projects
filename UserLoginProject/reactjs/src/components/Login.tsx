// src/components/Login.tsx
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Button, Alert } from 'react-bootstrap';
import { post, LOGIN_URL } from '../backendinterface.ts';


const Login: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async () => {
    if (username.trim() && password.trim()) {
      try{
          let formData = new FormData
          formData.append('username', username)
          formData.append('password', password)
          const response = await post(LOGIN_URL, formData);
          console.log(response.data)
          navigate('/addCustomer');
      }catch(error){
        setError(error.response.data.error)
      }
    } else {
      setError('Please fill in all fields');
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center min-vh-100">
      <div className="card p-5" style={{ maxWidth: '400px', width: '100%' }}>
        <h2 className="text-center">Login</h2>
        {error && <Alert variant="danger">{error}</Alert>}
        <div className="mb-3">
          <label htmlFor="username" className="form-label">
            Username
          </label>
          <input
            type="text"
            className="form-control"
            id="username"
            placeholder="Enter username"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setError(null);
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            className="form-control"
            id="password"
            placeholder="Password"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              setError(null);
            }}
          />
        </div>
        <Button variant="primary" onClick={handleLogin} className="w-100">
          Login
        </Button>
        {/* <p className="mt-3 text-center">
          Don't have an account? <Link to="/signup">Sign up</Link>
        </p> */}
      </div>
    </div>
  );
};

export default Login;
