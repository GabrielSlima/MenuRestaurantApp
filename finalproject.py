from flask import Flask, render_template
app = Flask(__name__)

restaurant = {'name': 'Restaurant legal', 'id':'1'}

#MOCK
restaurants = [{'name': 'Restaurant legal', 'id':'1'}, {'name': 'Feijao com pelo', 'id': 2}, {'name': 'Bico sujo', 'id':'1'}]

#MOCK
menuItems = [{"name":"File de merlusa", "id":"1", "descr":"Filezim", "price": "19.31"},
                {"name":"File de frango", "id": "2", "descr":"Filezim de frango humilde", "price": "11.31"},
                {"name":"File mignon ", "id": "3", "descr":"Filezim mignon", "price": "19.31"}]
#MOCK
menuItem = {"name":"File de merlusa", "id":"1", "descr":"Filezim", "price": "19.31"}

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
        return render_template('restaurants.html', all_restaurants=restaurants)

@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newRestaurant.html')

@app.route('/restaurant/<int:id_restaurant>/edit')
def editRestaurant(id_restaurant):
    return render_template('editRestaurant.html', restaurant_obj = restaurant)

@app.route('/restaurant/<int:id_restaurant>/delete')
def deleteRestaurant(id_restaurant):
    return render_template('deleteRestaurant.html', restaurant_obj=restaurant)

@app.route('/restaurant/<int:id_restaurant>/menu')
def showMenu(id_restaurant):
    return render_template('menu.html', all_menu_items=menuItems)

@app.route('/restaurant/<int:id_restaurant>/menu/new')
def newMenuItem(id_restaurant):
        return render_template('newMenuItem.html', restaurant_obj=restaurant)

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/edit')
def editMenuItem(id_restaurant,id_menu):
    return render_template('editMenuItem.html', menu_item=menuItem)

@app.route('/restaurant/<int:id_restaurant>/menu/<int:id_menu>/delete')
def deleteMenuItem(id_restaurant,id_menu):
    return render_template('deleteMenuItem.html', menu_item=menuItem)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5001)