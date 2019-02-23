from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "This route will show all my restaurants"

@app.route('/restaurant/new')
def newRestaurant():
    return "This route will add a new restaurant"

@app.route('/restaurant/<int:id_restaurant>/edit')
def editRestaurant(id_restaurant):
    return "This route will edit a existing restaurant, this " + str(id_restaurant)

@app.route('/restaurant/<int:id_restaurant>/delete')
def deleteRestaurant(id_restaurant):
    return "This route will delete a existing restaurant, this: " + str(id_restaurant)


@app.route('/restaurant/<int:id_restaurant>/menu')
def showMenu(id_restaurant):
    return "This route will show all items's menu from a specified restaurant"

@app.route('/restaurant/<int:id_restaurant>/menu/new')
def newMenuItem():
        return "This page will add a new menu item to a specific restaurant's menu"

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/edit')
def editMenuItem(id_restaurant,id_menu):
    return "This page will edit a existing menu item"

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/delete')
def deleteMenuItem(id_restaurant,id_menu):
    return "This page will delete a existing menu item"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5001)