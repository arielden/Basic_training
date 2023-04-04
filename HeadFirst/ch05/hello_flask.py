from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
@app.route('/search4')
def do_search() -> str:
    phrase = 'life, the universe, and everything'
    letters = 'eiru,!'
    return str(search4letters(phrase, letters))

app.run()