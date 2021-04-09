import wikipedia
from random_word import RandomWords
import re
from flask import Flask, request
from pyhtml import *
import string

app = Flask(__name__)

def generatePuzzle():
    global tgt
    answer = RandomWords().get_random_word()
    print(answer)
    tgt = wikipedia.search(answer,results=1)[0]
    print(tgt)
    result = wikipedia.summary(tgt)
    result = re.sub(tgt,"?????", result)
    result = re.sub(tgt.lower(), "?????", result)
    return result
@app.route('/')
def survey():
    word = generatePuzzle()
    example_form = form(action="analysis", name="any")(
        input_(type="textbox", name="word", placeholder="Please type in your answer"),
        input_(type="submit"),
        input_(type="button", value="new puzzle"))
    response = html(
        # header,
        body(
            example_form
        )
    )
    
    return "Welcome to the wiki guesser"+ str(response) + word 

@app.route('/analysis', methods=["GET", "POST"])
def analysis():
   
    global tgt
    if tgt.lower() == request.form['word'].lower():
        message = "You are correct"
    else:
        message = "You are wrong"
    return message
if __name__ == '__main__':
   app.run()

