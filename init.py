from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def MainPage():
    return render_template("MainPage.html")

@app.route("/about")
def About():
    return render_template("about.html")   


@app.route("/gasapp")
def GasApp():
    return render_template("Gas_app.html")


@app.route("/book")
def Book():
    return render_template("Book_Store.html")

@app.route("/bikerent")
def bikerent():
    return render_template("Bike Renting project.html") 


@app.route("/gym")
def gym():
    return render_template("Gym_website.html")   


@app.route("/movie")
def movie():
    return render_template("Movie_booking.html")  

@app.route("/portfolio")
def port():
    return render_template("My_Portfolio_Website.html")     

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello copy.html", fat7i = name)

# if __name__ == "__main__":
#    app.run(host="0.0.0.0",debug=True)
