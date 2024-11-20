from flask import Flask, render_template, request, make_response, redirect, url_for
from random import choice

from word_exercise import context

from cookie_set import from_cookie_to_dict, from_dict_to_cookie
from check_answer import check_answer

app = Flask(__name__)
                    

@app.route('/')
def index():
    pass


@app.route('/start')
def start():
    pass


@app.route('/words')
def words():
    pass


@app.route('/finish')
def finish():
    pass

if __name__ == "__main__":
    app.run(debug=True) 
