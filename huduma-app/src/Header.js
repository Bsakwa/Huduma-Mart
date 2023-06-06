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
          <li><Link to="/home">Home</Link></li>
	  <li><Link to="/about">About</Link></li>
	  <li><Link to="/services">Services</Link></li>
	  <li><Link to="/contact">Contact</Link></li>
	  <li><Link to="/register">Register</Link></li>
          <li><Link to="/login">Login</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
