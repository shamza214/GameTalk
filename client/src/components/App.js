


import React, { useState, useContext, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Navbar from "./Navbar";
import Home from "./Home";
import Ratings from "./Ratings";
import Reviews from "./Reviews";
import Walkthroughs from "./Walkthroughs";
import Games from './Games'
import Login from './Login'


function App() {
  document.title = "GameTalk";
  const [loggedIn, setLoggedIn] = useState(false);
  const [user, setUser] = useState(null);

  useEffect(() => {
    const storedUsername = localStorage.getItem("loggedInUser");
    if (storedUsername) {
      setLoggedIn(true);
      fetchUserData(storedUsername)
        .then((fetchedUser) => {
          setUser(fetchedUser);
        })
        .catch((error) => {
          console.error("Error fetching user data:", error);
        });
    }
  }, []);

  const handleLogin = (username) => {
    localStorage.setItem("loggedInUser", username);
    fetchUserData(username)
      .then((fetchedUser) => {
        setUser(fetchedUser);
        setLoggedIn(true);
      })
      .catch((error) => {
        console.error("Error fetching user data:", error);
      });
    setLoggedIn(true);
  };

  const handleLogout = () => {
    localStorage.removeItem("loggedInUser");
    setLoggedIn(false);
    setUser(null);
  };


  const fetchUserData = async (username) => {
    try {
      const response = await fetch(`http://localhost:5558/users/${username}`, {
        credentials: 'include',
      });

      if (!response.ok) {
        throw new Error('Failed to fetch user data');
      }

      const userData = await response.json();
      return userData;
    } catch (error) {
      console.error("Error fetching user data:", error);
      throw error;
    }
  };

  return (
  <div>
    <div>
      

        <Router>
        <Navbar />
          <Routes>
            <Route exact path="/" element={<Navigate to="/home" />} />
            <Route path="/login" element={<Login />}  />
            <Route path="/*" element={<Login />} />
          
          <Route path="/home" element={<Home />} />
          <Route path="/games" element={<Games />} />
          <Route path="/ratings" element={<Ratings />} />
          <Route path="/reviews" element={<Reviews />} />
          <Route path="/walkthroughs" element={<Walkthroughs />} />
          <Route exact path="/" element={<Navigate to="/home" />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
      
      </div>
      <div className='title'>
      <h1>GameTalk</h1>
    </div>
  </div>
  )
}


export default App;