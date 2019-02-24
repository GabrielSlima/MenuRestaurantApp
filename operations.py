from connection import banco
from sqlalchemy.orm import sessionmaker
from database import Restaurant, MenuItem

dbsession = sessionmaker(bind = banco)
session = dbsession()

def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return restaurants

def insertNewRestaurant(restaurantName):
    restaurante = Restaurant(name = restaurantName)
    session.add(restaurante)
    session.commit()

def updateRestaurant(id_restaurant, name_restaurant):
    restaurant = session.query(Restaurant).filter_by(id=id_restaurant).first()
    restaurant.name = name_restaurant
    session.add(restaurant)
    session.commit()

def deleteRestaurant(id_restaurant):
    restaurant = session.query(Restaurant).filter_by(id=id_restaurant).first()
    session.delete(restaurant)
    session.commit()

def getSpecificRestaurant(id_restaurant):
    restaurant = session.query(Restaurant).filter_by(id=id_restaurant).first()
    return restaurant

def showMenu(id_restaurant):
    menu = session.query(MenuItem).filter_by(restaurant_id=id_restaurant).all()
    return menu

def getSpecificMenuItem(id_menuItem):
    menuitem = session.query(MenuItem).filter_by(id=id_menuItem).first()
    print('----------------')
    print(menuitem)
    return menuitem

def insertMenuItem(id_restaurant,item_name, item_description, item_price):
    menu = MenuItem(name=item_name,description=item_description, price=item_price,restaurant_id=id_restaurant)
    session.add(menu)
    session.commit()
    
def updateMenuItem(id_restaurant, id_menuItem, item_name,item_description, item_price):
    menuItem = session.query(MenuItem).filter_by(id = id_menuItem).first()
    menuItem.name = item_name
    menuItem.description = item_description
    menuItem.price = item_price
    menuItem.restaurant_id = id_restaurant
    session.add(menuItem)
    session.commit()
    return True

def deleteMenuItem(id_menuItem):
    menuItem = session.query(MenuItem).filter_by(id = id_menuItem).first()
    session.delete(menuItem)
    session.commit()

if __name__ == '__main__':
   print('No tests here')