import React from 'react';
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
          <li><a href="#register">Register</a></li>
          <li><a href="#login">Login</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
