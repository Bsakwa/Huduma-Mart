import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './landingpage';
import ServiceProviderRegistrationForm from './sp_regist';
import Footer from './Footer';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/register/*" element={<SignupPage />} />
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
