from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return("<html> <h1> Welcome To Our Gallery Website!!</h1><h3>Press the links at the bottom and take a look at our AMAZING gallerys:) </h3><br><a href='/food'>Food Gallery Here!!</a><br><a href='/pets'>Pets Galary Here!!</ak><br><a href='/outerspace'>OuterSpace Here!!</a></html>")

@app.route('/food')  
def food():
    return ("<html><h1>Food's Gallery:)</h1><img src='https://media.istockphoto.com/id/1175505781/photo/arabic-and-middle-eastern-dinner-table-hummus-tabbouleh-salad-fattoush-salad-pita-meat-kebab.jpg?s=612x612&w=0&k=20&c=N4PkdbA7Bf-WNKf2VRNz9mtZP4sxrdcsMwZ7P981ZIY='><br><h3>You Can Also Go And Take A Look At Our Different Kinds Of Food's Gallery:)</h3><br><a href='arabicfood'>For Arabic Food Press Here!</a><br><a href='fastfood'>For Fast Food Press Here!</a><br><a href='/dessert'>For Desserts Press Here</a><br><a href='/'>Go Back To The Main Page</a><br><a href='/pets'>For The Next Page Press Here</a> </html>")   
      
@app.route('/pets')
def pets():
    return("<html><h1>Pets's Gallery:)</h1><img src='https://t3.ftcdn.net/jpg/04/81/85/46/360_F_481854656_gHGTnBscKXpFEgVTwAT4DL4NXXNhDKU9.jpg'<br><a href='/'>Go Back To The Main Page</a><br><a href='/wildanimals'>For Wild Animals Page Press Here</a><br><a href='outerspace'>For The Next Page Press Here</a><br><a href='/food'>To The Previous Page</a></html>")

@app.route('/outerspace')
def outerspace():
    return("<html><h1>OuterSpace's Gallery:)</h1><img src='https://cdn.unifiedcommerce.com/content/product/media/large/09615-index-html.jpg'><br><a href='/saturn'>Press To Know More About Saturn Planet</a><br><a href='/mars'>Press To Know More About Mars Planet</a><br><a href='mercury'>Press To Know More About Mercury Planet</a><br><a href='/'>Go Back To The Main Page</a><br><a href='/pets'>To The Previous Page</a></html>")
 
@app.route('/arabicfood')
def arabicfood():
    return("<html><h1>Arabic Food!</h1><img src='https://img.turkishstylecooking.com/wp-content/uploads/2021/03/mansaf3.jpg'<br><a href='/food'>Go Back To The Main Food Gallery</a></html>")  

@app.route('/fastfood')
def fasfood():
    return("<html><h1>Fast Food:)</h1><img src='https://media.timeout.com/images/106090008/750/422/image.jpg'><br><a href='/food'>Go Back To The Main Food Page</a></html>")

@app.route('/dessert')
def dessert():
    return("<html><h1>Here Is The Dessert:)</h1><img src='https://i.pinimg.com/564x/de/37/2b/de372b38a360f5dbfdffbcc7cf9d0221.jpg'><br><a href='/food'>Go Back To The Main Food Page</a></html>")

@app.route('/wildanimals')
def wildanimals():
    return("<html><h1>Here You Can See The Wild Animals:)</h1><img src='https://asm.org/ASM/media/Article-Images/2022/August/wild_animals_feature.jpg?ext=.jpg'><br><img src='https://extension.usu.edu/images/fox-937049_1920.jpg'<br><img src'https://static.toiimg.com/thumb/96352420.cms?resizemode=4&width=400'<br><a href='/pets'>Go Bact To The Main Pets Page</a></html>")

@app.route('/saturn')
def saturn():
    return("<html><h1>Here Is Saturn's Page:)</h1><img src='https://cdn.mos.cms.futurecdn.net/TWpr5dTCno77m2J2aFgLxD-1200-80.jpg'><br><a href=/outerspace>Go Back To The OuterSpace Main Page</a></html>")

@app.route('/mars')
def mars():
    return("<html><h1>Here Is Mars's Page:)</h1><img src='https://assets3.thrillist.com/v1/image/2863548/414x310/crop;webp=auto;jpeg_quality=60;progressive.jpg'><br><a href='/outerspace'>Go Back To The OuterSpace Main Page</a></html>")

@app.route('/mercury')
def mercury():
    return("<html><h1>Here Is Mercury's Page:)</h1><img src='https://cdn.mos.cms.futurecdn.net/fjbeeRiPRQjQNhizwy7cWX-1200-80.jpg'><br><a href='/outerspace'>Back To The Main Murcury Page</a></html>")

if __name__ == '__main__':
    app.run(debug=True)







