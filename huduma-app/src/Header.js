import React from 'react';
import { Link } from 'react-router-dom';
import SearchIcon from '@mui/icons-material/Search';
import './styles/Header.css';

const Header = () => {
  return (
    <header>
      <nav>
        <div className="logo">
        </div>
        <div className="slogan">
         Accessibility. Visibility. Service.
        </div>
        <div className="search-bar">
          <input type="text" placeholder="Search..." />
          <SearchIcon className="search-icon" />
        </div>
        <ul className="nav-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
	  <li><Link to="/register">Register</Link></li>
          <li><Link to="/login">Login</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
