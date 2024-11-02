import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    diametro = Column(Integer, nullable=False)
    clima = Column(String(80), nullable=False)
    poblacion = Column(String(80), nullable=False)
    url = Column(String(250), nullable=False)
    planetas_favoritos = relationship('PlanetaFavorito', back_populates='planeta')

class PlanetaFavorito(Base):
    __tablename__ = 'planeta_favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='planetas_favoritos')
    planeta = relationship('Planeta', back_populates='planetas_favoritos')

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(80), nullable=False, unique=True)
    personajes_favoritos = relationship('PersonajeFavorito', back_populates='usuario')
    planetas_favoritos = relationship('PlanetaFavorito', back_populates='usuario')


class PersonajeFavorito(Base):
    __tablename__ = 'personaje_favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='personajes_favoritos')
    personaje = relationship('Personaje', back_populates='personajes_favoritos')


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    altura = Column(Integer, nullable=False)
    genero = Column(String(80), nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    url = Column(String(250), nullable=False)
    personajes_favoritos = relationship('PersonajeFavorito', back_populates='personaje')
## Dibujar desde la base de SQLAlchemy
render_er(Base, 'diagram.png')