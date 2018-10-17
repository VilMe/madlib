"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Send user to game or say goodbye."""

    game_answer = request.args.get("game_choice")

    if game_answer == "no":
        return render_template("goodbye.html")
        # how to inherit name??? 
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    r1_checked = request.args.get("randomthing1")
    r2_checked = request.args.get("randomthing2")
    r3_checked = request.args.get("randomthing3")

    if not r1_checked:
        r1_checked = "gorilla"
    if not r2_checked:
        r2_checked ="cheeseburger"
    if not r3_checked:
        r3_checked = "spaceship"

    return render_template("madlib.html", 
                        color=color, 
                        noun=noun, 
                        person=person, 
                        adjective=adjective,
                        r1=r1_checked,
                        r2= r2_checked,
                        r3= r3_checked)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
