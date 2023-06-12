import React, { useState } from 'react';
import { FaHome, FaUser, FaCog, FaChartBar, FaSignOutAlt, FaBell, FaEnvelope, FaPhone, FaEnvelopeOpen, FaUserCircle } from 'react-icons/fa';
import { Link, useNavigate } from 'react-router-dom';
import './styles/HomePage.css';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';
import axios from 'axios';

const SearchResultProfile = ({ provider }) => {
  const { avatar, name, phone_number, location, email, category } = provider;

  return (
    <div className="search-result-profile">
      <div className="avatar">
        {avatar ? (
          <img src={avatar} alt={name} />
        ) : (
          <FaUserCircle className="default-avatar" />
        )}
      </div>
      <h3 className="name">{name}</h3>
      <p className="location">{location}</p>
      <p className="category">{category}</p>
      <div className="contact-icons">
        <a href={`tel:${phone_number}`} className="contact-icon">
          <FaPhone />
        </a>
        <a href={`mailto:${email}`} className="contact-icon">
          <FaEnvelopeOpen />
        </a>
        <Link to={`/direct-message/${provider.id}`} className="contact-icon">
          <FaEnvelope />
        </Link>
      </div>
    </div>
  );
};

const HomePage = () => {
  const [category, setCategory] = useState('');
  const [location, setLocation] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [showNoResults, setShowNoResults] = useState(false);
  const itemsPerPage = 4;
  const navigate = useNavigate();

  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };

  const handleLocationChange = (event) => {
    setLocation(event.target.value);
  };

  const handleSearchSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);

    if (!category && !location) {
      setSearchResults([]);
      setLoading(false);
      return;
    }

    try {
      const response = await fetch(`http://100.25.222.45:5000/api/v1/service_providers?category=${category}&location=${location}`);
      const data = await response.json();
      setSearchResults(data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }

    setLoading(false);
    setShowNoResults(true);
  };

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };
  
  const handleLogout = async () => {
    try {
      await axios.post('http://100.25.222.45:5000/api/v1/logout');
      sessionStorage.removeItem('session');
      navigate('/');
    } catch (error) {
      console.log('Error occurred while logging out:', error.message);
    }
  };

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = searchResults.length > 0 ? searchResults.slice(indexOfFirstItem, indexOfLastItem) : [];
  const totalPages = Math.ceil(searchResults.length / itemsPerPage);

  return (
    <div className="homepage">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="nav-container">
          <div className="logo"></div>
          <nav>
            <ul>
              <li>
                <Link to="/">
                  <FaHome className="icon" /> Home
                </Link>
              </li>
              <li>
                <Link to="/profile">
                  <FaUser className="icon" /> My Profile
                </Link>
              </li>
              <li>
                <Link to="/settings">
                  <FaCog className="icon" /> Settings
                </Link>
              </li>
              <li>
                <Link to="/dashboard">
                  <FaChartBar className="icon" /> Dashboard
                </Link>
              </li>
              <li>
                <Link to="/notifications">
                  <FaBell className="icon" /> Notifications
                </Link>
              </li>
              <li>
                <Link to="/messages">
                  <FaEnvelope className="icon" /> Messages
                </Link>
              </li>
              <li>
                <Link onClick={handleLogout}>
                  <FaSignOutAlt className="icon" /> Logout
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </div>

      {/* Content */}
      <div className="content">
        <div className="content-section">
          {/* Search Filter */}
          <section className="search-filter">
            <div className="search-bar">
              <form onSubmit={handleSearchSubmit}>
                <input
                  type="text"
                  placeholder="Category"
                  value={category}
                  onChange={handleCategoryChange}
                />
                <input
                  type="text"
                  placeholder="Location"
                  value={location}
                  onChange={handleLocationChange}
                />
                <button type="submit">Search</button>
              </form>
            </div>
            <div className="search-results">
              {loading ? (
                <p>Loading...</p>
              ) : searchResults.length > 0 ? (
                <>
                  <div className="search-result-profiles">
                    {currentItems.map((provider, index) => (
                      <SearchResultProfile key={provider.id} provider={provider} />
                    ))}
                  </div>
                  <div className="pagination">
                    {Array.from({ length: totalPages }, (_, index) => (
                      <button
                        key={index + 1}
                        onClick={() => handlePageChange(index + 1)}
                        className={currentPage === index + 1 ? "active" : ""}
                      >
                        {index + 1}
                      </button>
                    ))}
                  </div>
                </>
              ) : showNoResults ? (
                <p>No results found.</p>
              ) : null}
            </div>
          </section>

          {/* Featured Category */}
          <section className="featured-category">
            <h2 className="featured-headline">Access a wide range of service providers with a simple search</h2>
            <Carousel showArrows={true} showThumbs={false} autoPlay={true} infiniteLoop={true}>
              <div className="category-container plumber">
                <img src="image1.jpg" alt="" />
              </div>
              <div className="category-container artisan">
                <img src="image2.jpg" alt="" />
              </div>
              <div className="category-container electrician">
                <img src="image3.jpg" alt="" />
              </div>
              <div className="category-container mechanic">
                <img src="image4.jpg" alt="" />
              </div>
              <div className="category-container builder">
                <img src="image5.jpg" alt="" />
              </div>
              <div className="category-container dj">
                <img src="image6.jpg" alt="" />
              </div>
            </Carousel>
          </section>

          {/* Provider Profiles */}
          <section className="provider-profiles">
            {/* Add provider profiles here */}
          </section>
        </div>

        {/* Additional Content Sections */}
        <div className="content-section">
          {/* Add more content sections here */}
        </div>
      </div>
    </div>
  );
};

export default HomePage;
