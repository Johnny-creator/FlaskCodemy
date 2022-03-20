from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask Instance
app = Flask(__name__)
app.config.from_pyfile('config.py')

#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name:", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a route decorator
@app.route('/') 

def index():
    first_name = "John"
    stuff = "This is bold text"

    favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
        first_name=first_name,
        stuff=stuff,
        favourite_pizza = favourite_pizza)

# localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)


# Create custom error page
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    
    return render_template("name.html", name=name, form=form)