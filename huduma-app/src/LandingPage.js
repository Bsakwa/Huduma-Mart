import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './styles/LandingPage.css';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <section className="hero">
        <div className="hero-content">
          <h1>Connect with the Informal Sector</h1>
          <p>Discover local services near you and support your community.</p>
          <a href="#signup" className="btn btn-primary">Sign Up</a>
        </div>
      </section>

      <section className="features">
        {/* Existing feature cards */}
        <div className="feature-card">
          <img src="icon1.png" alt="Feature 1" />
          <h3>Increased Visibility</h3>
          <p>Showcase your skills and services to potential customers in your area.</p>
        </div>
        <div className="feature-card">
          <img src="icon2.png" alt="Feature 2" />
          <h3>Accessibility</h3>
          <p>Reach a wide range of customers anytime, anywhere, with our user-friendly app.</p>
        </div>
        <div className="feature-card">
          <img src="icon3.png" alt="Feature 3" />
          <h3>Community Support</h3>
          <p>Connect with your local community and contribute to its growth and development.</p>
        </div>
      </section>

      <section className="testimonials">
        {/* Existing testimonials */}
        <div className="testimonial">
          <div className="testimonial-image">
            <img className="john-doe" src="./assets/aiman.png" alt=""/>
          </div>
          <div className="testimonial-content">
            <h4>John Doe</h4>
            <p>Electrician</p>
            <blockquote>
              "Huduma Mart has transformed my business. I now have a steady stream of clients and my income has doubled!"
            </blockquote>
          </div>
        </div>
        <div className="testimonial">
          <div className="testimonial-image">
            <img className="jane-smith" alt=""/>
          </div>
          <div className="testimonial-content">
            <h4>Jane Smith</h4>
            <p>Plumber</p>
            <blockquote>
              "Thanks to Huduma Mart, I can easily find plumbing jobs in my area. It's convenient and saves me a lot of time."
            </blockquote>
          </div>
        </div>
      </section>

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
    </div>
  );
};

export default LandingPage;
