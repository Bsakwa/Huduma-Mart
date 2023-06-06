import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, TextField } from '@mui/material';
import axios from 'axios';
import './styles/LoginPage.css';

// Import your custom icon images
import googleIcon from './assets/google.png';
import microsoftIcon from './assets/microsoft.png';
import appleIcon from './assets/apple.png';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const navigate = useNavigate();

  const handleChange = (event) => {
    setEmail(event.target.value);
    setEmailError('');
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
      // Get all user emails
      const usersResponse = await axios.get('http://localhost:5000/api/v1/users');
      console.log('Users Response:', usersResponse);

      // Get all service provider emails
      const providersResponse = await axios.get('http://localhost:5000/api/v1/service_providers');
      console.log('Service Providers Response:', providersResponse);

      if (usersResponse.status === 200 && providersResponse.status === 200) {
        const userEmails = usersResponse.data.map((user) => user.email);
        const providerEmails = providersResponse.data.map((provider) => provider.email);
        const allEmails = [...userEmails, ...providerEmails];

        if (allEmails.includes(email)) {
          // Email exists in either users or service providers
          console.log('Email exists in the database');

          // Determine the userType based on the email match
          const userType = userEmails.includes(email) ? 'user' : 'serviceProvider';

          navigate('/home', { state: { email: email, userType: userType } });
          return;
        }

        // Email does not exist in the database
        console.log('Email does not exist in the database');
        setEmailError('Invalid password entered. Please try again.');
	// Add your logic to display an error message or handle the case accordingly
      } else {
        console.log('Error occurred while retrieving emails:', usersResponse.status, providersResponse.status);
        // Add your logic to display an error message or handle the error accordingly
      }
    } catch (error) {
      console.log('Error occurred while validating email:', error.message);
      // Add your logic to display an error message or handle the error accordingly
    }
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
            error={!!emailError}
            helperText={emailError}
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
