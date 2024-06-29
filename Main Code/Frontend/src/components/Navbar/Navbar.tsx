import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.scss';
import logo from '../../assets/logo.png';

const Navbar: React.FC = () => {
  return (
    <nav className="navbar">
      <div className="navbar__logo">
        <Link to="/">
          <img src={logo} alt="SummaryFlow Logo" className="navbar__logo-image" />
        </Link>
      </div>
      <ul className="navbar__menu">
        <li className="navbar__item">
          <Link to="/" className="navbar__link">Home</Link>
        </li>
        <li className="navbar__item">
          <Link to="/about" className="navbar__link">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;