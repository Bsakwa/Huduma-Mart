import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import { FaEye, FaGlobe, FaUsers, FaHandshake } from 'react-icons/fa';
import { IconContext } from 'react-icons';
import './styles/LandingPage.css';

const LandingPage = () => {
  return (
    <div className="landing-page">
      {/* Hero section */}
      <section className="hero">
        <div className="hero-content">
          <img src="logo.png" alt="" className="hm-banner" />
          <div className="hero-buttons">
            <h2>Sign Up to find service providers at your location</h2>
            <a href="/signup" className="btn btn-primary">Sign Up</a>
            <h2>Register as a service provider and be visible and accessible</h2>
            <a href="/register" className="btn btn-secondary">Register</a>
          </div>
        </div>
      </section>

      {/* Featured category section */}
      <section className="featured-category">
        <h2 className="featured-headline">Featured Service Providers</h2>
        <Carousel showArrows={true} showThumbs={false} autoPlay={true} infiniteLoop={true}>
          <div className="category-container plumber"></div>
          <div className="category-container artisan"></div>
          <div className="category-container electrician"></div>
          <div className="category-container mechanic"></div>
          <div className="category-container builder"></div>
          <div className="category-container dj"></div>
        </Carousel>
      </section>

      {/* Features section */}
      <section className="features">
        <h2 className="featured-headline">Why Huduma Mart?</h2>
        <div className="feature-list">
          <div className="feature-card">
            <IconContext.Provider value={{ className: 'feature-icon' }}>
              <FaEye />
            </IconContext.Provider>
            <h3>Increased Visibility</h3>
            <p>Whether it's a gardener, an electrician, a plumber, a masseuse, an errand boy, a tailor, barber, etc., we are giving you a platform to showcase your skills and services to a vast network of potential customers within your location and beyond.</p>
          </div>
          <div className="feature-card">
            <IconContext.Provider value={{ className: 'feature-icon' }}>
              <FaGlobe />
            </IconContext.Provider>
            <h3>Accessibility</h3>
            <p>When you register as a service provider, our users will be able to access and discover your services from wherever you are located, at any time with just a simple search.</p>
          </div>
          <div className="feature-card">
            <IconContext.Provider value={{ className: 'feature-icon' }}>
              <FaUsers />
            </IconContext.Provider>
            <h3>Community Support</h3>
            <p>Support local communities by discovering service providers within your location and help them grow.</p>
          </div>
          <div className="feature-card">
            <IconContext.Provider value={{ className: 'feature-icon' }}>
              <FaHandshake />
            </IconContext.Provider>
            <h3>Convenience</h3>
            <p>Enjoy the convenience of accessing day-to-day services with just a few clicks. With Huduma Mart, life just got a little easier.</p>
          </div>
        </div>
      </section>

      {/* Testimonials section */}
      <section className="testimonials">
        <h2 className="featured-headline">Testimonials</h2>
        <div className="testimonials-wrapper">
          <div className="testimonial">
            <div className="testimonial-image john-doe-avatar"></div>
            <div className="testimonial-content">
              <h4 className="testimonial-name">John James</h4>
              <p className="testimonial-profession">Electrician</p>
              <blockquote className="testimonial-quote">
                "Huduma Mart has transformed my business. I now have a steady stream of clients and my income has doubled!"
              </blockquote>
            </div>
          </div>
          <div className="testimonial">
            <div className="testimonial-image jane-smith-avatar"></div>
            <div className="testimonial-content">
              <h4 className="testimonial-name">Jane Smith</h4>
              <p className="testimonial-profession">Plumber</p>
              <blockquote className="testimonial-quote">
                "Thanks to Huduma Mart, I can easily find plumbing jobs in my area. It's convenient and saves me a lot of time."
              </blockquote>
            </div>
          </div>
          <div className="testimonial">
            <div className="testimonial-image mark-johnson-avatar"></div>
            <div className="testimonial-content">
              <h4 className="testimonial-name">Mark Johnson</h4>
              <p className="testimonial-profession">User</p>
              <blockquote className="testimonial-quote">
                "Huduma Mart has been a game changer. It is easy and convinient to access any service from any location."
              </blockquote>
            </div>
          </div>
          <div className="testimonial">
            <div className="testimonial-image sarah-williams-avatar"></div>
            <div className="testimonial-content">
              <h4 className="testimonial-name">Sarah Williams</h4>
              <p className="testimonial-profession">User</p>
              <blockquote className="testimonial-quote">
                "Huduma mart has made me discover alot of businesses around my location that I didn't know existed."
              </blockquote>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;
