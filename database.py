from connection import banco
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

base = declarative_base()

class Restaurant(base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class MenuItem(base):
    __tablename__= 'menuItem'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    description = Column(String(250), nullable = False)
    price = Column(String(250), nullable = False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

base.metadata.create_all(banco)