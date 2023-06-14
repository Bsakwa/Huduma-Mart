import React from 'react';
import { Link } from 'react-router-dom';
import './styles/Header.css';

const Header = () => {
  return (
    <header>
      <nav>
        <div className="header-container">
          <div className="logo-container">
            <img src="./assets/huduma.png" alt="" className="logo" />
          </div>
          <ul className="nav-links">
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/services">Services</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
          <a href="/login" className="btn btn-primary">Login</a>
        </div>
      </nav>
    </header>
  );
}

export default Header;
