from config import app, db, api
# Add your model imports
from models import Game, User, Review, Rating,db, GameReviewAssociation
from flask_restful import Resource
from flask import make_response, jsonify, request, session, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
import bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
CORS(app, origins="https://example.com")


migrate = Migrate(app, db)

db.init_app(app)

from flask import request
from flask_restful import Resource
from config import app, db, api


@app.route('/')
def index():
    return '<h1>GameTalk</h1>'

class Games(Resource):
    def get(self):
        games = Game.query.all()
        games_dict_list = []

        for game in games:
            game_dict = {
                'id': game.id,
                'name': game.name,
                
            }
            games_dict_list.append(game_dict)

        return make_response(games_dict_list)

api.add_resource(Games, '/games')


class GamesByID(Resource):
    def get(self,id):
        game = Game.query.filter_by(id=id).first()
        if not game:
            return make_response({"error": "Game not found"}, 404)
        return (game.to_dict())
    
api.add_resource(GamesByID, '/game/<int:id>')


class Users(Resource):
    def get(self):
        users = User.query.all()
        users_dict_list = []
        
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                
            }
            
            
            if hasattr(user, 'ratings'):
                user_dict['ratings'] = [rating.to_dict() for rating in user.ratings]
            
            users_dict_list.append(user_dict)
        
        if len(users_dict_list) == 0:
            return make_response({'error': 'no Users'}, 404)
        
        return make_response(jsonify(users_dict_list), 200)
    
    
    def post (self):
        data = request.get_json()
        newUser = User(
            username= data["username"],
            password = data["password"],
            )
        try:
            db.session.add(newUser)
            db.session.commit()
            return make_response (newUser.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
    
api.add_resource(Users, '/users')


class Ratings(Resource):
    def get(self):
        try:
            ratings_with_names = []

            
            ratings = Rating.query.join(User, User.id == Rating.user_id).join(Game, Game.id == Rating.game_id).all()

            for rating in ratings:
                rating_data = {
                    "id": rating.id,
                    "rating": rating.rating,
                    "user_name": rating.user.username,
                    "game_name": rating.game.name
                }
                ratings_with_names.append(rating_data)

            return make_response(jsonify(ratings_with_names), 200)

        except Exception as e:
            
            return make_response(jsonify({"error": str(e)}), 500)
        
from flask import request, make_response
from flask_restful import Resource

class RatingById(Resource):
    def get(self, id):
        rating = Rating.query.get(id)
        if not rating:
            return make_response({'message': 'not found'}, 404)

    def delete(self, id):
        rating = Rating.query.get_or_404(id)

        db.session.delete(rating)
        db.session.commit()

        return make_response({'message': 'Rating deleted successfully'}, 204)

api.add_resource (Ratings, '/ratings')
api.add_resource(RatingById, '/ratings/<int:id>')

class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        reviews_dict_list = [review.to_dict(only=('text', 'id',)) for review in reviews]
        return jsonify (reviews_dict_list)

    def post(self):
        data = request.get_json()
        game_text = data.get('game')
        user_id = data.get('user_id')

        try:
            
            review_text = data.get('review')
            review = Review(text=review_text)  
            db.session.add(review)
            db.session.commit()

            
            game = Game.query.filter_by(name=game_text).first()

            if game:
                
                association = GameReviewAssociation(game_id=game.id, review_id=review.id)
                db.session.add(association)
                db.session.commit()
                return jsonify({"message": "Review posted and associated with the game successfully"})
            else:
                
                db.session.rollback()
                return jsonify({"error": "Game not found"}), 404

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "An error occurred while posting the review.", "details": str(e)}), 500
        
api.add_resource (Reviews, '/reviews')


class ReviewsById(Resource):
    def get(self, review_id):
        review = Review.query.get(review_id)
        if review:
            return review.to_dict(), 200
        else:
            return make_response({'error': 'Review not found'}, 404)
        
    def patch(self, review_id):
        data = request.get_json()
        new_review_text = data.get('review')

        try:
            
            review = Review.query.get(review_id)

            if review:
                
                review.text = new_review_text
                db.session.commit()
                return jsonify({"message": "Review updated successfully"}), 200
            else:
                return jsonify({"error": "Review not found"}), 404

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "An error occurred while updating the review.", "details": str(e)}), 500


api.add_resource(ReviewsById, '/reviews/<int:review_id>')


# class Login(Resource):
#     def post(self):
#         # data = request.get_json()
#         username = request.json.get('name', None)
#         password = request.json.get('password', None)
#         if not username:
#             return make_response(jsonify(success=False, message='Missing Username'), 400)
#         if not password:
#             return make_response(jsonify(success=False, message='Missing Password!'), 400)
#         user = User.query.filter_by(username=username).first()
#         if not user:
#             return make_response(jsonify(success=False, message='User Not Found!'), 404)
#         if bcrypt.check_password_hash(password.encode('utf-8'), user._password_hash):
#             # Store user.id in the session
#             # session['logged_in_user_id'] = user.id

#             return make_response(jsonify(success=True, message=f'Welcome back {username}'), 201)
#         else:
#             return make_response(jsonify(success=False, message='Wrong Password!'), 200) 

class Login(Resource):
    def post(self):
        username = request.json.get('name', None)
        password = request.json.get('password', None)
        if not username:
            return make_response(jsonify(success=False, message='Missing Username'), 400)
        if not password:
            return make_response(jsonify(success=False, message='Missing Password!'), 400)
        
        user = User.query.filter_by(username=username).first()
        if not user:
            return make_response(jsonify(success=False, message='User Not Found!'), 404)
        
        if bcrypt.checkpw(password.encode('utf-8'), user._password_hash.encode('utf-8')):
            return make_response(jsonify(success=True, message=f'Welcome back {username}'), 201)
        else:
            return make_response(jsonify(success=False, message='Wrong Password!'), 200)

        
        
        # user = User.query.filter_by(name=name).first()
        # if user and user.authenticate(password): 
        #     session['user_id'] = user.id 
        #     return {'user_id': user.id}, 200
        # else:
        #     return {'message': 'Invalid username or password'}, 401
        
        
        


# class Signup (Resource):
#     def post ( self ):
#         data = request.json
#         username = data['name']
#         password = data['password']

#         user = User.query.filter_by(name=username).first()
#         if user: 
#             return make_response({'error': 'username taken be original'}, 404)

#         new_user = User(username=username,password_hash=password)
#         db.session.add(new_user)
#         db.session.commit()
#         session ['user_id'] = new_user.id
#         return make_response({'message': 'user created successfully'}, 200)

class Logout (Resource):
    def delete (self):
        session['user_id'] = None
        return make_response ({'message': 'User logged out'},204)

class Authenticate (Resource):
    def get (self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user: 
            return make_response(user.to_dict(),200)
        else:
            return make_response({'error': 'no active user found in database'},401)


api.add_resource(Login, '/login')
# api.add_resource(Signup, '/signup')
api.add_resource(Authenticate,'/authenticate')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
