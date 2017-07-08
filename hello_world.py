from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
def say_whatup():
	return "Whatup!"

@app.route("/hello")
def say_hi():
	return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://kittenrescue.org/wp-content/uploads/2017/03/KittenRescue_KittenCareHandbook.jpg">
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first,last):
	html = """
		<h1>
			Your Jedi name is {0}{1}
		</h1>
	"""
	return html.format(last[0:3],first[0:3])


if __name__ == "__main__":
	app.run()
