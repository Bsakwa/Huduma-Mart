import React, { useState } from 'react';
import { FaHome, FaUser, FaCog, FaChartBar, FaSignOutAlt, FaBell, FaEnvelope } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import './styles/HomePage.css'; // Import the CSS file
import "react-responsive-carousel/lib/styles/carousel.min.css"; // Import the Carousel styles
import { Carousel } from 'react-responsive-carousel';

const SearchResultProfile = ({ provider }) => {
  return (
    <div className="search-result-profile">
      <img src={provider.avatar} alt={provider.name} className="avatar" />
      <h3 className="name">{provider.name}</h3>
      <p className="phone-number">{provider.phone_number}</p>
      <p className="location">{provider.location}</p>
      <p className="category">{provider.category}</p>
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
  const itemsPerPage = 6;

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
      const response = await fetch(`http://localhost:5000/api/v1/service_providers?category=${category}&location=${location}`);
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

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = searchResults.length > 0 ? searchResults.slice(indexOfFirstItem, indexOfLastItem) : [];

  const totalPages = Math.ceil(searchResults.length / itemsPerPage);

  return (
    <div className="homepage">
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
                <Link to="/logout">
                  <FaSignOutAlt className="icon" /> Logout
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <div className="content">
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
        <div className="content-section">
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
          <section className="provider-profiles">
            {/* Add provider profiles here */}
          </section>
        </div>
        <div className="content-section">
          {/* Add more content sections here */}
        </div>
      </div>
    </div>
  );
};

export default HomePage;
