from flask import Flask, render_template, request, make_response
from random import choice

from word_exercise import context
from words_list import words

from cookie_set import from_cookie_to_dict, from_dict_to_cookie

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/words/", methods=["GET", "POST"])
def words_page():
    context = {
        "number": "",
        "english_word": "",
        "translate1": "",
        "translate2": "",
        "translate3": "",
        "translate4": ""
    }
    res = make_response()
    res.set_cookie('universal', "")
    # make a dictionary with cookie value
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'state': 'start', 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    # code
    if cookie_value_dictionary['state'] == 'start':
        res = make_response(render_template('words.html'))
        cookie_value_dictionary = {
            'state': 'words',
            'question': 0,
            'count': 0
        }
    elif cookie_value_dictionary["state"] == 'words':
        if cookie_value_dictionary["question"] <= 100:
            
        else:
            cookie_value_dictionary["state"] = 'finish'
            res = make_response(render_template('finish.html'))
    elif cookie_value_dictionary['state'] == 'finish':
        cookie_value_dictionary["state"] = 'start'
    # make a string from dictionary
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    return res

if __name__ == "__main__":
    app.run(debug=True)
    