import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { IconButton, Drawer, List, ListItem, ListItemText } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import './styles/Header.css';

const Header = () => {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  const handleDrawerToggle = () => {
    setIsDrawerOpen(!isDrawerOpen);
  };

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth <= 1024);
    };

    window.addEventListener('resize', handleResize);
    handleResize();

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <header className="header">
      <nav className="navbar">
        <div className="logo-container">
          <Link to="/" className="logo-link">
            {/* Add your logo here */}
          </Link>
        </div>
        {!isMobile ? (
          <ul className="nav-links">
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/about">About us</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        ) : (
          <div className="hamburger">
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              onClick={handleDrawerToggle}
            >
              <MenuIcon />
            </IconButton>
            <Drawer
              anchor="right"
              open={isDrawerOpen}
              onClose={handleDrawerToggle}
            >
              <List>
                <ListItem button component={Link} to="/home" onClick={handleDrawerToggle}>
                  <ListItemText primary="Home" />
                </ListItem>
                <ListItem button component={Link} to="/about" onClick={handleDrawerToggle}>
                  <ListItemText primary="About Us" />
                </ListItem>
                <ListItem button component={Link} to="/contact" onClick={handleDrawerToggle}>
                  <ListItemText primary="Contact" />
                </ListItem>
                <ListItem button component={Link} to="/login" onClick={handleDrawerToggle}>
                  <ListItemText primary="Login" />
                </ListItem>
                <ListItem button component={Link} to="/signup" onClick={handleDrawerToggle}>
                  <ListItemText primary="Signup" />
                </ListItem>
              </List>
            </Drawer>
          </div>
        )}
        <div className="auth-buttons">
          <Link to="/login" className="login-link">Login</Link>
          <Link to="/signup" className="signup-button btns btns-secondary">Sign Up</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
