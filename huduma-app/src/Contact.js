import React from 'react';
import { TextField, Button } from '@mui/material';
import { Send, LocationOn, Phone, Email, Schedule } from '@mui/icons-material';
import './styles/Contact.css';

const ContactPage = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform form submission logic here
  };

  return (
    <div className="contact-page">
      <div className="background-image" />
      <div className="content-container">
        <h2>Contact Us</h2>
        <form id="contact-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <TextField type="text" label="Name" required />
          </div>
          <div className="form-group">
            <TextField type="email" label="Email" required />
          </div>
          <div className="form-group">
            <TextField type="tel" label="Phone Number" required />
          </div>
          <div className="form-group">
            <TextField multiline rows={4} label="Message" required />
          </div>
          <Button variant="contained" type="submit" endIcon={<Send />}>
            Submit
          </Button>
        </form>
        <div className="info-container">
          <div className="info-item">
            <LocationOn />
            <span>Nairobi City, Kenya</span>
          </div>
          <div className="info-item">
            <Phone />
            <span>+1234567890</span>
          </div>
          <div className="info-item">
            <Email />
            <span>hudumamart@gmail.com</span>
          </div>
          <div className="info-item">
            <Schedule />
            <span>Mon-Fri: 9am-5pm</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContactPage;
