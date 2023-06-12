import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, TextField, InputAdornment, IconButton } from '@mui/material';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import axios from 'axios';
import './styles/SignupPage.css';

// Import your custom icon images
import googleIcon from './assets/google.png';
import microsoftIcon from './assets/microsoft.png';
import appleIcon from './assets/apple.png';

const SignupUserPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
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
    } else if (event.target.name === 'firstName') {
      setFirstName(event.target.value);
    } else if (event.target.name === 'lastName') {
      setLastName(event.target.value);
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
      // Make a POST request to the register endpoint
      const response = await axios.post('http://100.25.222.45:5000/api/v1/register', {
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      });
      console.log('Register Response:', response);

      if (response.status === 201) {
        // Registration successful, redirect to the login page
        navigate('/home');
      } else {
        console.log('Registration failed:', response.data.message);
        // Add your logic to display an error message or handle the error accordingly
      }
    } catch (error) {
      console.log('Error occurred while registering:', error.message);
      // Add your logic to display an error message or handle the error accordingly
    }
  };

  const handleTogglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div className="signin-container">
      <div className="signup-page">
        <h2>Sign Up</h2>

        <form className="signup-form" onSubmit={handleFormSubmit}>
          <TextField
            name="email"
            type="email"
            label="Email"
            required
            fullWidth
            value={email}
            onChange={handleChange}
            style={{ marginBottom: '10px', width: '100%' }}
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

          <TextField
            name="firstName"
            label="First Name"
            required
            fullWidth
            value={firstName}
            onChange={handleChange}
            style={{ marginBottom: '10px', width: '100%' }}
          />

          <TextField
            name="lastName"
            label="Last Name"
            required
            fullWidth
            value={lastName}
            onChange={handleChange}
            style={{ marginBottom: '10px', width: '100%' }}
          />

          <div className="button-container">
            <Button type="submit" variant="contained" className="signup-button">
              Sign Up
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

export default SignupUserPage;
