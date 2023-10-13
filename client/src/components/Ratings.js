import React, { useEffect, useState } from "react";
import "../CSS/Ratings.css"; 

const Ratings = () => {
    const [ratings, setRatings] = useState([]);
    const [error, setError] = useState(null);
    const [ratingId, setRatingId] = useState("")

    useEffect(() => {
    fetch('/ratings')
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            
            setRatings(data);
        })
        .catch((err) => {
            console.error("Error fetching ratings data:", err);
            setError(err);
        });
}, []);

    const deleteRating = async (ratingId) => {

        try {
            const response = await fetch(`/ratings/${ratingId}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
            });
            if (response.ok) {
                console.log("Review deleted successfully");
                setRatings(ratings.filter(rating => rating.id !== ratingId))
            } else {
                console.log(ratingId)
                console.error("Failed to delete review");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    };
    return (
        <div className="ratings-container">
            <h1>Ratings</h1>
            {error ? (
                <p className="error-message">Error loading ratings data. Please try again later.</p>
            ) : (
                <div className="ratings-list">
                    {ratings.map((rating, index) => (
                        <div key={index} className="rating-card">
                            <h3> Game Name: {rating.game_name} </h3>
                            <p>User ID: {rating.user_name}</p>
                            <p>Rating: {rating.rating}</p>
                            <button onClick={() => deleteRating(rating.id)}>Delete Rating</button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default Ratings;