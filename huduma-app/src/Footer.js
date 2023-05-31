import React from 'react';
import { IconButton, TextField, Button } from '@mui/material';
import InstagramIcon from '@mui/icons-material/Instagram';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import './styles/Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="follow-us-container">
        <span className="footer-text">FOLLOW US:</span>
        <div className="social-icons">
          <IconButton
            color="primary"
            aria-label="Instagram"
            href="https://www.instagram.com/your-instagram-profile"
            target="_blank"
            rel="noopener noreferrer"
          >
            <InstagramIcon />
          </IconButton>
          <IconButton
            color="primary"
            aria-label="Facebook"
            href="https://www.facebook.com/your-facebook-profile"
            target="_blank"
            rel="noopener noreferrer"
          >
            <FacebookIcon />
          </IconButton>
          <IconButton
            color="primary"
            aria-label="Twitter"
            href="https://www.twitter.com/your-twitter-profile"
            target="_blank"
            rel="noopener noreferrer"
          >
            <TwitterIcon />
          </IconButton>
        </div>
      </div>
      <div className="footer-content">
        <div className="section-container">
          <h3>Support</h3>
          <div className="support-items">
            <p>Contact us</p>
            <p>FAQ</p>
            <p>Locate a service provider</p>
	    <p>Report a problem</p>
	    <p>Help</p>
          </div>
        </div>
        <div className="section-container">
          <h3>Huduma Mart</h3>
          <div className="huduma-mart-items">
            <p>About us</p>
            <p>Careers</p>
            <p>Team</p>
	    <p>Blog</p>
	    <p>Partners</p>
          </div>
        </div>
        <div className="section-container">
          <h3>Legal</h3>
          <div className="legal-items">
            <p>Privacy Policy</p>
            <p>Terms of Use</p>
            <p>Terms and Conditions</p>
	    <p>Cookie Policy</p>
	    <p>Accessibility</p>
          </div>
        </div>
        <div className="section-container">
          <h3>Subscribe to our Newsletter</h3>
          <div className="newsletter-section">
            <TextField
              id="email-input"
              label="Enter your email"
              variant="outlined"
              size="small"
              fullWidth
              InputProps={{
                style: {
                  borderColor: 'white',
                  color: 'white',
                },
              }}
              InputLabelProps={{
                style: {
                  color: 'white',
                },
              }}
            />
            <Button variant="contained" color="primary">
              Subscribe
            </Button>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; Huduma Mart 2023. All rights reserved</p>
      </div>
    </footer>
  );
}

export default Footer;
