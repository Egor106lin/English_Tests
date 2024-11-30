from flask import Flask, render_template, make_response, redirect, url_for
from flask import request

import random
from word_exercise import create_random_words_for_user

from cookie_set import from_cookie_to_dict, from_dict_to_cookie
from check_answer import check_answer

from words_list import english_excercices

app = Flask(__name__)
                    

def create_seed() -> int:
    seed = random.randint(0, 10**10)
    return seed


@app.route('/', methods=['GET', 'POST'])
def index():
    res = make_response()
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    res = make_response(render_template('index.html'))
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    if request.method == 'POST':
        return redirect(url_for('start'))
    return res


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        return redirect(url_for('words'))
    elif request.method == 'GET':
        return(render_template('start.html'))


@app.route('/words', methods=['GET', 'POST'])
def words():
    res = make_response()
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    if request.method == 'POST':
        if cookie_value_dictionary['question'] >= 10:
            return redirect(url_for('finish'))
        elif cookie_value_dictionary['question'] < 10:
            # for name in ['word1', 'word2', 'word3', 'word4']:
            #   answer = request.form.get(name)
            #   if answer != None:
            #       cookie_value_dictionary = check_answer(cookie_value_dictionary, answer, context)
            #   else:
            #       continue
            my_seed = cookie_value_dictionary['seed']
            question =  cookie_value_dictionary['question']
            print(my_seed, question)
            dictionary_dict = create_random_words_for_user(my_seed, english_excercices)[question]
            dictionary_key = next(iter(dictionary_dict))
            dictionary_list = dictionary_dict[dictionary_key]
            exercise = {
                    'number': cookie_value_dictionary['question'] + 1,
                    'english_word': dictionary_key,
                    'translate1': dictionary_list[0],
                    'translate2': dictionary_list[1],
                    'translate3': dictionary_list[2],
                    'translate4': dictionary_list[3],
            }
            cookie_value_dictionary['question'] += 1
            res = make_response(render_template('words.html', **exercise))
            res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
            return res
    else:
        if cookie_value_dictionary['question'] >= 10:
            return redirect(url_for('finish'))
        else:
            my_seed = cookie_value_dictionary['seed']
            question =  cookie_value_dictionary['question']
            print(my_seed, question)
            dictionary_dict = create_random_words_for_user(my_seed, english_excercices)[question]
            dictionary_key = next(iter(dictionary_dict))
            dictionary_list = dictionary_dict[dictionary_key]
            exercise = {
                    'number': cookie_value_dictionary['question'] + 1,
                    'english_word': dictionary_key,
                    'translate1': dictionary_list[0],
                    'translate2': dictionary_list[1],
                    'translate3': dictionary_list[2],
                    'translate4': dictionary_list[3],
            }
            res = make_response(render_template('words.html', **exercise))
            return res


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    res = make_response()
    if request.method == 'POST':
        res.set_cookie('universal', expires=0)
        return redirect(url_for('index'))
    elif request.method == 'GET':
        value_of_cookie = request.cookies.get('universal')
        if value_of_cookie == None:
            return redirect(url_for('index'))
        else:
            cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
            count = cookie_value_dictionary['count']
            res = make_response(render_template('finish.html', result=count))
            return res
        

if __name__ == "__main__":
    app.run(debug=True) 
