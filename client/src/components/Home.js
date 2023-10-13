import React from "react";
import "../CSS/Home.css"; 

const Home = () => {
    const imageSrc = "https://i.scdn.co/image/ab6765630000ba8a9dda9a5a59f2b7df34ab0264";

    return (
        <div className="home-container">
            <h1></h1>
            <img src={imageSrc} alt="Sample Image" />
            
        </div>
    );
};

export default Home;