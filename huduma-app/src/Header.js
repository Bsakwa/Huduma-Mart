import React from 'react';
import { Link } from 'react-router-dom';
import './styles/Header.css';

const Header = () => {
  return (
    <header className="headr">
      <nav className="navbar">
        <div className="logo-container">
          <Link to="/" className="logo-link">
          </Link>
        </div>
        <ul className="nav-links">
          <li><Link to="/home">Home</Link></li>
          <li><Link to="/about">About us</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
        <div className="auth-buttons">
          <Link to="/login" className="btn">Login</Link>
          <Link to="/signup" className="btns btns-secondary">Sign Up</Link>
        </div>
      </nav>
    </header>
  );
}

export default Header;
