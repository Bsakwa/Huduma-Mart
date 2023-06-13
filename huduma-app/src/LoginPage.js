import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, TextField, InputAdornment, IconButton } from '@mui/material';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import axios from 'axios';
import './styles/LoginPage.css';

// Import your custom icon images
import googleIcon from './assets/google.png';
import microsoftIcon from './assets/microsoft.png';
import appleIcon from './assets/apple.png';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const handleChange = (event) => {
    if (event.target.name === 'email') {
      setEmail(event.target.value);
      setEmailError('');
    } else if (event.target.name === 'password') {
      setPassword(event.target.value);
      setPasswordError('');
    }
  };

  const validateEmail = () => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(email)) {
      setEmailError('Please enter a valid email address');
      return false;
    }
    return true;
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault(); // Prevent form submission

    if (!validateEmail()) {
      return;
    }

    try {
      const response = await axios.post('http://100.25.222.45/api/v1/login', { email, password });
      console.log('Login Response:', response);

      if (response.status === 200) {
        // Login successful, redirect to the home page
        navigate('/home');
      } else {
        console.log('Login failed: Invalid email or password');
        setPasswordError('Invalid email or password');
	
        // Add your logic to display an error message or handle the error accordingly
      }
    } catch (error) {
      console.log('Error occurred while logging in:', error.message);
      setPasswordError('Invalid email or password');
      // Add your logic to display an error message or handle the error accordingly
    }
  };

  const handleTogglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="login-container">
      <div className="login-page">
        <h2>Login</h2>

        <form className="login-form" onSubmit={handleFormSubmit}>
          <TextField
            name="email"
            type="email"
            label="Email"
            required
            fullWidth
            value={email}
            onChange={handleChange}
            style={{ marginBottom: '20px', width: '100%' }}
            error={Boolean(email) && !/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email)}
            helperText={emailError}
          />

          <TextField
            name="password"
            type={showPassword ? 'text' : 'password'}
            label="Password"
            required
            fullWidth
            value={password}
            onChange={handleChange}
            style={{ marginBottom: '10px', width: '100%' }}
            error={Boolean(passwordError)}
            helperText={passwordError}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton onClick={handleTogglePasswordVisibility} edge="end">
                    {showPassword ? <VisibilityIcon /> : <VisibilityOffIcon />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />

          <div className="button-container">
            <Button type="submit" variant="contained" className="login-button">
              Login
            </Button>
          </div>
        </form>

        <div className="continue-container">
          <p>OR</p>

          <form onSubmit={() => handleFormSubmit('Google')}>
            <Button type="submit" variant="contained" className="continue-button">
              <img src={googleIcon} alt="Google" className="continue-icon" />
              Continue with Google
            </Button>
          </form>

          <form onSubmit={() => handleFormSubmit('Microsoft')}>
            <Button type="submit" variant="contained" className="continue-button">
              <img src={microsoftIcon} alt="Microsoft" className="continue-icon" />
              Continue with Microsoft
            </Button>
          </form>

          <form onSubmit={() => handleFormSubmit('Apple')}>
            <Button type="submit" variant="contained" className="continue-button">
              <img src={appleIcon} alt="Apple" className="continue-icon" />
              Continue with Apple
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
