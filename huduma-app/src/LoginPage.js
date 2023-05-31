import React from 'react';
import { Button, TextField } from '@mui/material';
import './styles/LoginPage.css';

// Import your custom icon images
import googleIcon from './assets/google.png';
import microsoftIcon from './assets/microsoft.png';
import appleIcon from './assets/apple.png';

const LoginPage = () => {
  const handleFormSubmit = (provider) => {
    // Handle form submission for different providers
    console.log(`Continue with ${provider}`);
  };

  return (
    <div className="login-container">
      <div className="login-page">
        <h2>Login</h2>

        <form className="login-form">
          <TextField id="email" type="email" label="Email" required fullWidth />

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
              <img src={appleIcon}  alt="Apple" className="continue-icon" />
              Continue with Apple
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
