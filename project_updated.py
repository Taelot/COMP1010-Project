import yaml
import wikipedia
from random_word import RandomWords
import re
from flask import Flask, request
from pyhtml import html, body, h1, p, form, input_, label, button, head, link, br
import string

app = Flask(__name__)
global tgt

def generatePuzzle():
    global tgt
    puzzle_form = form(action="quiz")(
        label(
            input_(type="submit", value="New Puzzle")))
    hint_form = form(action = "hint", name='any1')(
        input_(type="submit", id="button1", value="Hint"),
        br()
    )
    response = html(
        head(
            link(rel="stylesheet",type="text/css", href="main.css")
        ),
        body(
            puzzle_form,
            hint_form
            
        )
    )
    try:
        answer = RandomWords().get_random_word()
        print(answer)
        tgt = wikipedia.search(answer,results=1)[0]
        print(tgt)
        result = wikipedia.summary(tgt)
        result = re.sub(tgt,"?????", result)
        result = re.sub(tgt.lower(), "?????", result)
    except: 
        return "A disambiguation error occured, please try a new word." + str(response)
    
    return result + str(response)

@app.route('/')
def survey():
    initial_form = form(action='quiz')(
        label(
            input_(type="submit", value='Begin')
        )
    )
    response = html(
        head(
            link(rel="stylesheet",type="text/css", href="main.css")
        ),
        body(
            h1('Wiki Guesser'),
            p('Welcome to Wiki Guesser, a game designed to test your general knowledge.'),
            initial_form
        )
    )
    return  str(response) 

@app.route('/quiz', methods=["GET", "POST"])
def begin():
    word = generatePuzzle()
    
    guessing_form = form(action="analysis", name="any")(
        input_(type="textbox", name="word", placeholder="Please type in your answer"),
        input_(type="submit"),
        
    )
    
    response = html(
        head(
            link(rel="stylesheet",type="text/css", href="{{ url_for('static', filename='main.css') }}")
        ),
        body(
            guessing_form,
            
        )
    )
    return str(response) + word
@app.route('/hint', methods = ['GET', 'POST'])
def hint():
    global tgt
    return tgt

@app.route('/analysis', methods=["GET", "POST"])
def analysis():
   
    global tgt
    if tgt.lower() == request.form['word'].lower():
        message = "You are correct"
    else:
        message = "You are wrong. Try again."
    final_form = form(action='quiz')(
        label(
            input_(type="submit", value='New Puzzle')
        )
    )
    final_response = html(
        body(
            final_form
        )
    )
    return message +  str(final_response)

if __name__ == "__main__":
    app.run(debug=True)
