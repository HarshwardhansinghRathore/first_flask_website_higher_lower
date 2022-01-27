from random import randint
from flask import Flask

app = Flask(__name__)

random_number = randint(0,10)

@app.route('/')
def home_page():
    return "<h1>Guess a number between 0 and 9<h1>" \
        "<img src=https://media3.giphy.com/media/iDJQRjTCenF7A4BRyU/giphy.webp?cid" \
           "=ecf05e470wwfh7v1u2v9wp983z24maiob5s10cfulb07s4g6&rid=giphy.webp&ct=g> "

@app.route('/<int:number>')
def get_result(number):
    if number < random_number:
        return "<h1>too low<h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    elif number < random_number:
        return "<h1>too high<h1>" \
               "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy>"
    else:
        return"<h1>correct you guessed it right<h1>" \
              "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
if __name__ == '__main__':
    app.run()
