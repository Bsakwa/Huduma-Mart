import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div className="landing-page">
      <nav className="navbar">
        <Link to="/" className="logo">Huduma Mart</Link>
        <ul className="nav-links">
          <li><Link to="/signup">Sign Up</Link></li>
          <li><Link to="/login">Login</Link></li>
        </ul>
      </nav>
      <header className="hero-section">
        <h1>Welcome to Huduma Mart</h1>
        <p>Discover and connect with service providers in the informal sector.</p>
        <Link to="/signup" className="btn-signup">Sign Up</Link>
      </header>
      <section className="features">
        <div className="feature">
          <h2>Find Local Services</h2>
          <p>Search and browse through a wide range of service providers in your area.</p>
        </div>
        <div className="feature">
          <h2>Contact Service Providers</h2>
          <p>Connect directly with service providers to inquire about their services.</p>
        </div>
        <div className="feature">
          <h2>Leave Reviews</h2>
          <p>Share your experiences and leave reviews for the service providers you've used.</p>
        </div>
      </section>
      <section className="service-providers">
        {/* Fetch and display service providers */}
        {/* <ServiceProvidersGrid /> */}
      </section>
      <section className="testimonials">
        <h2>What Our Customers Say</h2>
        <div className="testimonial-carousel">
          {/* Display testimonials */}
          {/* <TestimonialCarousel /> */}
        </div>
      </section>
      <section className="contact-form">
        <h2>Contact Us</h2>
        {/* Add contact form */}
        {/* <ContactForm /> */}
      </section>
      <footer>
        <p>&copy; 2023 Huduma Mart. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default LandingPage;
