import React from 'react';
import './Footer.scss';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <p>
        &copy; 2024 SummaryFlow. All rights reserved. | 
        <a href="mailto:ahmadhany1060@icloud.com" className="footer__item">Contact Us</a>
      </p>
    </footer>
  );
};

export default Footer;
