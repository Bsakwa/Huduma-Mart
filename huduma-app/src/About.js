import React from 'react';
import { FaEnvelope, FaGithub, FaLinkedin } from 'react-icons/fa';
import './styles/About.css';

const About = () => {
  const creators = [
    {
      name: 'Brian Sakwa',
      avatar: 'brian-sakwa-avatar.jpg',
      description: ' "As the Backend developer, am incredibly honoured to be part of this project and to have worked with such a talented team. I am passionate about using technology to solve real-world problems and create a positive impact. I believe that Huduma-mart has the potential to transform the blue-collar sector and empower individuals in the informal sector. I am excited to see how this project will evolve and grow in the future."',
      email: 'omondisakwa@gmail.com',
      github: 'https://github.com/Bsakwa',
      linkedin: 'https://linkedin.com/in/creator1',
    },
    {
      name: 'Myra Sukantet',
      avatar: 'myra-sukantet-avatar.jpg',
      description: '"As the Frontend Developer of Huduma Mart Application, I have had a delightful time working on this portfolio project alongside Brian and it has been an eye-opener. The Huduma Mart application is needed especially when unemployment is at a record high. I am confident that the application will give workers in the blue collar category a platform where they are able to showcase their skills and connect with customers."',
      email: 'myrasanaa17@gmail.com',
      github: 'https://github.com/myra-suk',
      linkedin: 'https://linkedin.com/in/creator2',
    },
  ];

  return (
    <div className="about-container">
      <div className="about-content">
        <h2>About Us</h2>
        <p>
          At Huduma-mart, we believe in revolutionizing the blue-collar sector by increasing the visibility and accessibility of service providers in this vital industry. The blue-collar sector, often overlooked and underestimated, is a significant contributor to the economy and plays a crucial role in numerous sectors such as construction, maintenance, transportation, and more. However, it has been left largely untouched by technological advancements and innovations, causing it to stagnate without experiencing the benefits of disruption.
        </p>
        <p>
          Our mission is to bridge the gap and empower blue-collar workers by providing them with a platform to showcase their skills, connect with potential clients, and expand their reach. We understand that one of the biggest challenges in Africa is access to income-generating opportunities, especially for individuals in the informal sector. With Huduma-mart, we aim to address this challenge by leveraging technology to create a seamless and efficient marketplace that brings together service providers and customers in a user-friendly manner.
        </p>
        <p>
          By using our app, customers can easily discover and hire skilled professionals for various services, ranging from plumbing and electrical work to gardening and housekeeping. We prioritize quality and reliability, ensuring that all service providers on our platform go through a rigorous vetting process to deliver exceptional services to our users. Additionally, our app offers features such as reviews and ratings, ensuring transparency and accountability within the community.
        </p>
        <p>
          Huduma-mart is committed to promoting entrepreneurship, driving economic growth, and uplifting the blue-collar sector. We believe in the potential of every individual and their ability to contribute to society. Join us in our journey to create a more inclusive and prosperous future, where the informal sector thrives and everyone has equal access to opportunities.
        </p>

        <section className="creators-section">
          <h3>Meet the Creators</h3>
          <div className="creators-wrapper">
            {creators.map((creator, index) => (
              <div key={index} className="creator">
                <div className={`creator-image creator-avatar-${index + 1}`}></div>
                <div className="creator-content">
                  <h4 className="creator-name">{creator.name}</h4>
                  <p className="creator-description">{creator.description}</p>
                  <div className="creator-contact">
                    <a href={`mailto:${creator.email}`} className="creator-icon">
                      <FaEnvelope />
                    </a>
                    <a href={creator.github} target="_blank" rel="noopener noreferrer" className="creator-icon">
                      <FaGithub />
                    </a>
                    <a href={creator.linkedin} target="_blank" rel="noopener noreferrer" className="creator-icon">
                      <FaLinkedin />
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
};

export default About;
