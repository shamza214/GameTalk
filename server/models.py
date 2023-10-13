from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from config import db


class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    ratings = db.relationship( 'Rating', back_populates = 'game', cascade = 'all, delete-orphan' )
    users = association_proxy( 'ratings', 'user' )
    
    # game_review_association = db.relationship('GameReviewAssociation', cascade='all,delete', back_populates='game')
    reviews = relationship('GameReviewAssociation', back_populates='game')


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    # Add serialization rules
    #  serialize_rules = ( '-reviews.user', '-reviews.game.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    
    ratings = db.relationship( 'Rating', back_populates = 'user' )
    games = association_proxy( 'ratings', 'games' )
    
    
    @property 
    def password_hash (self):
        return self._password_hash
    @password_hash.setter
    def password_hash (self, value):
        plain_byte_obj=value.encode('utf-8')
        encrypted_hash_obj= bcrypt.generate_password_hash(plain_byte_obj)
        hash_obj_as_string = encrypted_hash_obj.decode('utf-8')
        self._password_hash = hash_obj_as_string
    
    def authenticate (self, password_string):
        return bcrypt.check_password_hash(self.password_hash, password_string.encode('utf-8'))

class Rating(db.Model, SerializerMixin):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    game = db.relationship('Game', back_populates='ratings')
    user = db.relationship('User', back_populates='ratings')

    # serialize_rules = ('-user.ratings',)


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    
    # serialize_rules = ('id', 'rating')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    text = db.Column(db.String)

    # review_game_association = db.relationship('GameReviewAssociation', cascade= 'all, delete', back_populates='review')
    games = relationship('GameReviewAssociation', back_populates='review')
    
    def __repr__(self):
        return f'<Review id={self.id} name={self.name}>'
    
    

class GameReviewAssociation(db.Model, SerializerMixin):
    __tablename__ = 'game_review_associations'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    # game = db.relationship('Game', back_populates='reviews')
    # review = db.relationship('Review', back_populates='games')
    
    game = db.relationship('Game')
    review = db.relationship('Review')