import React, { useEffect, useState, useRef } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { IconButton, InputAdornment, TextField } from '@mui/material';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import './styles/sp.css';

function ServiceProviderRegistrationForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [password, setPassword] = useState('');
  const [categories, setCategories] = useState([]);
  const [locations, setLocations] = useState([]);
  const [location, setLocation] = useState('');
  const [town, setTown] = useState('');
  const [estate, setEstate] = useState('');
  const [category, setCategory] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [description] = useState('');

  const dropdownRef = useRef(null);
  const [isDropdownOpen, setDropdownOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch categories from the API
    axios
      .get('http://localhost:5000/api/v1/categories')
      .then(response => {
        // Set the categories in state
        setCategories(response.data);
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });

    // Fetch locations from the API
    axios
      .get('http://localhost:5000/api/v1/locations')
      .then(response => {
        // Set the locations in state
        setLocations(response.data);
      })
      .catch(error => {
        console.error('Error fetching locations:', error);
      });

    // Add scroll event listener to handle dropdown position
    window.addEventListener('scroll', handleScroll);

    // Cleanup event listener on component unmount
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const handleScroll = () => {
    const dropdownContainer = dropdownRef.current;

    if (dropdownContainer) {
      const { top } = dropdownContainer.getBoundingClientRect();
      const isBelowViewport = top + dropdownContainer.offsetHeight > window.innerHeight;

      setDropdownOpen(!isBelowViewport);
    }
  };
  const handleSubmit = e => {
  e.preventDefault();
  
  // Find the selected location object
  const selectedLocation = locations.find(loc => loc.name === location);

  if (selectedLocation) {
    // Extract the county from the selected location
    const { county } = selectedLocation;

    // Create the location with the matched name, county, town, and estate
    const newLocation = {
      name: location,
      county,
      town,
      estate,
    };

    // Make a POST request to create the new location
    axios
      .post('http://localhost:5000/api/v1/locations', newLocation)
      .then(response => {
        // Get the created location ID from the response
        const locationId = response.data.id;

        // Use the locationId as needed in your application

        // Fetch the category ID based on the entered category name
        const selectedCategory = categories.find(cat => cat.name === category);

        if (selectedCategory) {
          const categoryId = selectedCategory.id;
          // Use the categoryId as needed in your application

          // Create the new service provider
          const newServiceProvider = {
            name,
            email,
            phone_number: phoneNumber,
            password,
            category_id: categoryId,
            location_id: locationId,
	    description,
          };

          // Make a POST request to create the new service provider
          axios
            .post('http://localhost:5000/api/v1/service_providers', newServiceProvider)
            .then(response => {
              // Handle the success response
              console.log('Service provider created successfully:', response.data);
              // Reset the form or perform any other necessary actions
	      setName('');
              setEmail('');
              setPhoneNumber('');
              setPassword('');
              setCategory('');
              setLocation('');
              setTown('');
              setEstate('');
	      navigate('/home');
            })
            .catch(error => {
              console.error('Error creating service provider:', error);
            });
        } else {
          console.error('Invalid category selected');
        }
      })
      .catch(error => {
        console.error('Error creating location:', error);
      });
  } else {
    console.error('Invalid location selected');
  }
};


  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        type="text"
        placeholder="Name"
        value={name}
        className="custom-name"
        style={{ marginBottom: '10px', marginTop: '10px', width: '100%' }}
        onChange={e => setName(e.target.value)}
        required
      />
      <br />
      <TextField
        type="email"
        placeholder="Email"
        value={email}
        className="custom-email"
        style={{ marginBottom: '10px', width: '100%' }}
        onChange={e => setEmail(e.target.value)}
        required
	error={Boolean(email) && !/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email)}
        helperText={Boolean(email) && !/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email) ? 'Invalid email format' : ''}
      />
      <br />
      <TextField
        type="tel"
        placeholder="Phone Number"
        value={phoneNumber}
        className="custom-phone-number"
        style={{ marginBottom: '10px', width: '100%' }}
        onChange={e => setPhoneNumber(e.target.value)}
        required
      />
      <br />
      <TextField
        type={showPassword ? 'text' : 'password'}
        placeholder="Password"
        value={password}
        className="custom-password"
        style={{ marginBottom: '10px', width: '100%' }}
        onChange={e => setPassword(e.target.value)}
        required
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <IconButton onClick={togglePasswordVisibility}>
                {showPassword ? <VisibilityIcon /> : <VisibilityOffIcon />}
              </IconButton>
            </InputAdornment>
          ),
        }}
      />
      <br />
      <div className={`dropdown ${isDropdownOpen ? 'dropdown-open' : ''}`} ref={dropdownRef}>
        <select value={location} onChange={e => setLocation(e.target.value)}>
          <option value="">Select a location</option>
          {locations.map(location => (
            <option key={location.id} value={location.name}>
              {location.name}
            </option>
          ))}
        </select>
      </div>
      <div className="town-estate">
        <input type="text" placeholder="Town" value={town} onChange={e => setTown(e.target.value)} required />
        <input type="text" placeholder="Estate" value={estate} onChange={e => setEstate(e.target.value)} required />
      </div>
      <div className="dropdown">
        <select value={category} onChange={e => setCategory(e.target.value)}>
          <option value="">Select a category</option>
          {categories.map(category => (
            <option key={category.id} value={category.name}>
              {category.name}
            </option>
          ))}
        </select>
      </div>
      <br />
      <div className="privacy-policy">
        <p>
          By clicking the submit button, you are agreeing to and acknowledging our&nbsp;
          <a href="/privacy-policy" target="_blank" rel="noopener noreferrer">
            Privacy Policy
          </a>
          .
        </p>
      </div>
      <button type="submit" className="submit-button">
        Submit
      </button>
      <div className="signup-footer">
        <p>
          Already have an account? <a href="/login">Login</a>
        </p>
      </div>
    </form>
  );
}

export default ServiceProviderRegistrationForm;
