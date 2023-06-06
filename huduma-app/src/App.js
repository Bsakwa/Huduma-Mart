import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ServiceProviderRegistrationForm from './sp_regist';
import LoginPage from './LoginPage';
import Footer from './Footer';
import Header from './Header';
import LandingPage from './LandingPage';
import HomePage from './HomePage';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
	<Route path="/home" element={<HomePage />} />
        <Route path="/" element={<LandingPage />} />
        <Route path="/register/" element={<SignupPage />} />
        <Route path="/login/" element={<LoginPage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

function SignupPage() {
  return (
    <div className="app-container">
      <div className="signup-container">
        <h2>Register</h2>
        <ServiceProviderRegistrationForm />
        <div className="privacy-policy"></div>
      </div>
    </div>
  );
}

export default App;
