import React from 'react';
import { Link } from 'react-router-dom';
import { FaHome, FaUser, FaCog, FaChartBar, FaSignOutAlt, FaBell, FaEnvelope } from 'react-icons/fa';
import './styles/HomePage.css'; // Import the CSS file

const HomePage = () => {
  return (
    <div className="homepage">
      <div className="sidebar">
        <div className="nav-container">
          <div className="logo">Logo</div>
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
        <section className="search-filter">
          {/* Add search and filter functionality here */}
        </section>
        <section className="provider-profiles">
          {/* Add provider profiles here */}
        </section>
        <section className="service-categories">
          {/* Add service categories here */}
        </section>
        <section className="promotion-section">
          {/* Add promotion section for service providers here */}
        </section>
        {/* Add more content sections as needed */}
      </div>
    </div>
  );
};

export default HomePage;
