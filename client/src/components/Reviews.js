import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../CSS/Reviews.css";

const Reviews = () => {
    const [gameTitle, setGameTitle] = useState("");
    const [reviewText, setReviewText] = useState("");
    const [reviews, setReviews] = useState([]);
    const [createdReviews, setCreatedReviews] = useState([]);
    const [games, setGames] = useState([]);
    const [gameId, setGameId] = useState(null);
    const [detailId, setDetailId] = useState("");
    const [showForm, setShowForm] = useState(false);
    const [newGameTitle, setNewGameTitle] = useState("");

    const handleDetail = (detailedReview) => {
        setDetailId(detailedReview);
    };

    useEffect(() => {
        fetch("/reviews")
            .then((response) => response.json())
            .then((reviewsData) => {
                console.log(reviewsData);
                setReviews(reviewsData);
            })
            .catch((error) =>
                console.error("Error while fetching game reviews:", error)
            );
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (gameTitle.trim() !== "" && reviewText.trim() !== "") {
            const newReview = {
                game: gameTitle,
                review: reviewText,
            };
            console.log(newReview);
            try {
                const response = await fetch("/reviews", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(newReview),
                });

                if (response.ok) {
                    const createdReview = response.json();
                    setCreatedReviews([...createdReviews, createdReview]);
                    setGameTitle("");
                    setReviewText("");
                } else {
                    console.error("Failed to add the review to the database");
                }
            } catch (error) {
                console.error("Error while adding the review:", error);
            }
        }
    };

    const handleReviewModify = async (review_id) => {
        try {
            const updatedData = {
                review: reviewText, 
            };

            const response = await fetch(`/reviews/${review_id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(updatedData),
            });

            if (response.ok) {
                console.log("Review modified successfully");
                
            } else {
                console.error("Failed to modify review");
            }
        } catch (error) {
            console.error("Error while modifying review:", error);
        }
    };

    return (
        <div className="game-reviews-container">
            <h1>Game Reviews</h1>
            <div className="reviews-list">
                {reviews &&
                    reviews.map((review, index) => (
                        <div key={index} className="review-card">
                            <h3>{review.id}</h3>
                            {detailId === review.id ? (
                                <div>
                                    <textarea
                                        value={reviewText}
                                        onChange={(e) => setReviewText(e.target.value)}
                                    />
                                    <button onClick={() => handleReviewModify(review.id)}>
                                        Save Changes
                                    </button>
                                </div>
                            ) : (
                                <p>{review.text}</p>
                            )}
                            
                            <button onClick={() => handleDetail(review.id)}>Edit Review</button>
                        </div>
                    ))}
            </div>

            <div className="create-review-form">
                <h2>Create a Game Review</h2>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="Game Title"
                        value={gameTitle}
                        onChange={(e) => setGameTitle(e.target.value)}
                    />
                    <textarea
                        placeholder="Your Review"
                        value={reviewText}
                        onChange={(e) => setReviewText(e.target.value)}
                    />
                    <button type="submit">Submit Review</button>
                </form>
            </div>

            <div className="user-games">
                <h2>Your Reviewed Games</h2>
                <ul>
                    {games &&
                        games.map((game, index) => (
                            <li key={index}>
                                {game.name}
                                <ul>
                                    {game.reviews &&
                                        game.reviews.map((review, index) => (
                                            <li key={index}>
                                                {review.username} - {review.text}
                                            </li>
                                        ))}
                                </ul>
                            </li>
                        ))}
                </ul>
            </div>
        </div>
    );
};

export default Reviews;
