import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import "../CSS/Navbar.css";

const Navbar = ({ isAuthenticated, onLogout }) => {
    return (
        <nav className="navbar">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <NavLink exact to="/" className="nav-link">
                        Home
                    </NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to="/games" className="nav-link">
                        Games
                    </NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to="/reviews" className="nav-link">
                        Reviews
                    </NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to="/walkthroughs" className="nav-link">
                        Walkthrough
                    </NavLink>
                </li>
                <li className="nav-item">
                    {isAuthenticated ? (
                        <button className="logout-button" onClick={onLogout}>
                            Sign Out
                        </button>
                    ) : (
                        <Link to="/ratings" className="nav-link">
                            Ratings
                        </Link>
                    )}
                </li>
                <li className="nav-item">
                    <NavLink to="/login" className="nav-link">
                        Login
                    </NavLink>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;