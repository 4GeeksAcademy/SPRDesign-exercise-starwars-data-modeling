import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable = False, unique = True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(80), nullable = False, unique = True)
    password = Column(String(80), nullable = False)
    subscription_date = Column(String(50))
    favorites = relationship('Favorites')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    birth_year = Column(String(50))
    gender = Column(Enum('male', 'female', 'other', name = 'gender'))
    height = Column(Integer)
    weight = Column(Integer)
    eye_color = Column(Enum('blue', 'brown', 'green', 'black', 'other', name='eyes'))
    hair_color = Column(Enum('blond', 'brown', 'ginger', 'black', 'other', name = 'hair'))
    planet_id= Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer)
    climate = Column(Enum('temperate', 'tropical', 'arid', 'frozen', 'murky', name = 'climate'))
    terrain = Column(Enum('jungle, rainforests', 'grasslands, mountains', 'ocean', 'desert', 'tundra', 'ice caves, mountain ranges', 'forests, mountains, lakes', ' swamp, jungles', 'terrain'))
    surface_water = Column(Integer)
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(String(50))
    character_id = Column(Integer, ForeignKey('character.id')) 
    character = relationship(Character)
   
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))
    length = Column(Integer)
    cargo = Column(Integer)
    speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    manufacturer = Column(Enum('Corellia Mining Corporation', 'SoroSuub Corporation', 'Incom Corporation', 'Sienar Fleet Systems', ' Ubrikkian Industries', name='manufacturer'))
    character_id = Column(Integer, ForeignKey('character.id')) 
    character = relationship(Character)
  
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    vehicle_id =  Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')