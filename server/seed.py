from app import app
from models import Game, Review, Rating, User
from config import db
from random import randint, choice as rc
from app import app
from models import db
import bcrypt


def games():
    with app.app_context():
        G1 = Game(name='Valorant')
        G2 = Game(name='League of Legends')
        G3 = Game(name='Teamfight Tactics')
        G4 = Game(name='Apex Legends')
        G5 = Game(name='Counter Strike Global Offensive')
        G6 = Game(name='Counter Strike 2')
        G7 = Game(name='Brawlhalla')
        G8 = Game(name='Super Smash Bros')
        G9 = Game(name='Mario Kart 8')
        G10 = Game(name='Sekiro: Shadows Die Twice')
        G11 = Game(name='Elden Ring')
        G12 = Game(name='Hades')

        allgames = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12]

        return allgames


def create_users():
    users = []

    user_data = [
        {"name": "Syed Hamza", "username": "admin", "password_hash": "admin"},
        {"name": "Jane Smith", "username": "user2", "password_hash": "password2"},
        {"name": "Alice Johnson", "username": "user3", "password_hash": "password3"},
    ]

    for data in user_data:
        hashed = bcrypt.hashpw(data["password_hash"].encode('utf-8'), bcrypt.gensalt(rounds=12))
        u = User(
            name=data["name"],
            username=data["username"],
            password_hash=hashed.decode('utf-8')  # Store hashed password as string
        )
        users.append(u)

    return users


def create_ratings(games, users):
    ratings = []
    for _ in range(20):
        r = Rating(
            user_id=rc([user.id for user in users]),
            game_id=rc([game.id for game in games]),
            rating=randint(1, 5)
        )
        ratings.append(r)

    return ratings

def reviews():
    with app.app_context():
        V1 = Review(text = 'A thrilling adventure! This game kept me on the edge of my seat from start to finish.')
        V2 = Review(text = 'A masterpiece of storytelling and gameplay. It`s a must-play for any gamer.')
        V3 = Review(text = 'Fun and addictive, but it could use some improvements in graphics and performance.')
        V4 = Review(text = 'An immersive gaming experience. I couldn`t put it down once I started playing.')
        V5 = Review(text = 'Mixed feelings about this one. Some aspects are great, while others fall short.')
        V6 = Review(text = 'A nostalgic trip down memory lane. It captures the essence of classic gaming.')
        V7 = Review(text = 'Perfect for gamers and foodies alike. This game combines two worlds seamlessly.')
        V8 = Review(text = 'A diverse gaming menu with a cozy atmosphere. It`s a journey you won`t forget.')
        V9 = Review(text = 'Not worth the hype. I expected more from this game.')
        V10 = Review(text = 'A haven for gaming enthusiasts. The attention to detail is impressive.')
        V11 = Review(text = 'A hidden gem for fans of this genre. It`s a delightful escape from the ordinary.')
        V12 = Review(text = 'Underwhelmed by the gameplay, but the atmosphere is cozy and inviting.')
        V13 = Review(text = 'Affordable gaming fix. It gets the job done without breaking the bank.')
        V14 = Review(text = 'Pleasantly surprised by the graphics and gameplay. However, the load times were a bit slow.')
        V15 = Review(text = 'Creative theme, hit-or-miss gameplay. Execution varies, but the experience is enjoyable.')
        V16 = Review(text = 'Quick and convenient gaming at its best. A go-to spot for fast entertainment.')
        V17 = Review(text = 'Disappointing gameplay. It wasn`t worth the long wait.')
        V18 = Review(text = 'A gamer`s paradise! The attention to quality is evident in every aspect.')
        V19 = Review(text = 'Outstanding! This game is a symphony of gaming excellence, crafted with passion and skill.')
        V20 = Review(text = 'Gaming paradise! The variety is impressive, and the gameplay is top-notch.')
        V21 = Review(text = 'A gamer`s dream come true. It`s a gaming gem that you won`t want to miss.')
        V22 = Review(text = 'Surprisingly enjoyable. An entertaining treat when you`re on the go.')
        V23 = Review(text = 'Gameplay was underwhelming, but the ambiance is pleasant.')
        V24 = Review(text = 'A coastal gaming experience that`s second to none. The gameplay is on point.')
        V25 = Review(text = 'Reliable gaming experience. Quick and no surprises.')
        V26 = Review(text = 'Setting the bar high for gaming excellence. A must-visit for true gamers.')
        V27 = Review(text = 'A gaming haven worth visiting. The dedication to quality shines through.')
        V28 = Review(text = 'A mixed bag of gaming experiences. Some aspects were a delight, while others left me questioning the choices.')
        V29 = Review(text = 'Amusing gaming atmosphere, moderate gameplay. Relies on its theme to stand out.')
        V30 = Review(text = 'A decent gaming experience overall. The ambiance was lovely, but the gameplay didn`t match the high expectations set by the aesthetics.')


        allreviews = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30]
        return allreviews


if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Game.query.delete()
        Rating.query.delete()
        User.query.delete()
        Review.query.delete()

        print("Seeding games...")
        games_list = games()
        db.session.add_all(games_list)
        db.session.commit()

        print("Seeding users...")
        users_list = create_users()
        db.session.add_all(users_list)
        db.session.commit()

        print("Seeding ratings...")
        ratings_list = create_ratings(games_list, users_list)
        db.session.add_all(ratings_list)
        db.session.commit()

        print("Seeding reviews...")
        reviews_list = reviews()
        db.session.add_all(reviews_list)
        db.session.commit()

        print("Done seeding!")
