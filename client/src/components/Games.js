import React, { useEffect, useState } from "react";
import "../CSS/Games.css";


const Games = () => {
    const [games, setGames] = useState([]);
    const [error, setError] = useState(null); 

    useEffect(() => {
        fetch('/games')
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => setGames(data))
            .catch((err) => {
                console.error("Error fetching data:", err);
                setError(err); 
            });
    }, []);

    return (
        <div className="games-container">
            <h1>Games</h1>
            {error ? (
                <div className="error-message">Error: {error.message}</div>
            ) : (
                <div className="games-list">
                    {games.map((card, index) => (
                        <div key={index} className="game-card">
                            <h3>{card.name}</h3>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default Games;