from flask import Flask, render_template, request, url_for, redirect, jsonify
import operations
app = Flask(__name__)

@app.route('/restaurants/JSON')
def showRestaurantsAPI():
        restaurants = operations.showRestaurants()
        return jsonify(Restaurants=[i.serialize for i in restaurants])

@app.route('/restaurant/<int:id_restaurant>/menu/JSON')
def showMenuAPI(id_restaurant):
        menus = operations.showMenu(id_restaurant)
        return jsonify(MenuItems=[menuitem.serialize for menuitem in menus])

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/JSON')
def showSpecificMenuItemAPI(id_restaurant,id_menu):
        menu = operations.getSpecificMenuItem(id_menu)
        return jsonify(Item=[menu.serialize])
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
        restaurants = operations.showRestaurants()
        print(restaurants)
        return render_template('restaurants.html', all_restaurants=restaurants)

@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
        name = ''
        method = request.method
        print('Chegou aqui')
        if method == 'POST':
                name = request.form['restaurantName']
                print(name)
                if name != "": 
                        print('Chegou aqui')
                        operations.insertNewRestaurant(name)
                        print('Added')
                return redirect(url_for('showRestaurants'))
        return render_template('newRestaurant.html')

@app.route('/restaurant/<int:id_restaurant>/edit', methods=['GET','POST'])
def editRestaurant(id_restaurant):
        if request.method == 'POST':
                restaurant_name = None
                restaurant_name = request.form['restaurantName']
                print(restaurant_name)
                if restaurant_name != "":
                        operations.updateRestaurant(id_restaurant, restaurant_name)
                return redirect(url_for('showRestaurants'))
        restaurant = operations.getSpecificRestaurant(id_restaurant)
        return render_template('editRestaurant.html', restaurant_obj=restaurant)

@app.route('/restaurant/<int:id_restaurant>/delete', methods=['GET', 'POST'])
def deleteRestaurant(id_restaurant):
        if request.method == 'POST':
                operations.deleteRestaurant(id_restaurant)
                return redirect(url_for('showRestaurants'))
        restaurant = operations.getSpecificRestaurant(id_restaurant)
        return render_template('deleteRestaurant.html', restaurant_obj=restaurant)

@app.route('/restaurant/<int:id_restaurant>/menu')
def showMenu(id_restaurant):
        menuItems = operations.showMenu(id_restaurant)
        return render_template('menu.html', all_menu_items=menuItems, restaurant_id=id_restaurant)

@app.route('/restaurant/<int:id_restaurant>/menu/new', methods=['GET','POST'])
def newMenuItem(id_restaurant):
        if request.method == 'POST':
                itemName = None
                itemDescription = None
                itemPrice = None
                itemName = request.form['menuItemName']
                itemDescription = request.form['description']
                itemPrice = request.form['price']
                print(itemName)
                print(itemDescription)
                print(itemPrice)
                operations.insertMenuItem(id_restaurant,itemName,itemDescription,itemPrice)
                return redirect(url_for('showMenu',id_restaurant=id_restaurant))
        restaurant = operations.getSpecificRestaurant(id_restaurant)
        return render_template('newMenuItem.html', restaurant_obj=restaurant)

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menuItem>/edit', methods=['GET','POST'])
def editMenuItem(id_restaurant,id_menuItem):
        if request.method == 'POST':
                itemName = None
                itemDescription = None
                itemPrice = None
                itemName = request.form['menuItemName']
                itemDescription = request.form['description']
                itemPrice = request.form['price']
                operations.updateMenuItem(id_restaurant,id_menuItem,itemName,itemDescription,itemPrice)
                return redirect(url_for('showMenu',id_restaurant=id_restaurant))
        menuItem=operations.getSpecificMenuItem(id_menuItem)
        return render_template('editMenuItem.html', menu_item=menuItem)

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/delete', methods=['GET', 'POST'])
def deleteMenuItem(id_restaurant,id_menu):
        if request.method == 'POST':
                operations.deleteMenuItem(id_menu)
                return redirect(url_for('showMenu',id_restaurant=id_restaurant))
        menuItem = operations.getSpecificMenuItem(id_menu)
        return render_template('deleteMenuItem.html', menu_item=menuItem)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5001)