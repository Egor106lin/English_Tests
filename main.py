from flask import Flask
from flask import render_template, make_response, redirect, url_for
from flask import request

import random
from word_exercise import create_random_words_for_user

from cookie_set import from_cookie_to_dict, from_dict_to_cookie
from check_answer import check_answer

from words_list import english_excercices_first_test, answers_eng_keys
from words_list import english_excercices_second_test, answers_second_test

app = Flask(__name__)


def create_seed() -> int:
    '''This function generate random int as a seed for user.'''
    seed = random.randint(0, 10**10)
    return seed


@app.route('/', methods=['GET'])
def index():
    res = make_response()
    value_of_words = request.cookies.get('words', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    words_value_dictionary = from_cookie_to_dict(value_of_words)
    value_of_simple_tenses = request.cookies.get('simple_tenses', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    simple_tenses_value_dictionary = from_cookie_to_dict(value_of_simple_tenses)
    res = make_response(render_template('index.html'))
    res.set_cookie('words', from_dict_to_cookie(words_value_dictionary))
    res.set_cookie('simple_tenses', from_dict_to_cookie(simple_tenses_value_dictionary))
    return res


@app.route('/', methods=['POST'])
def index_post():
    if request.form.get('game_button') == 'test1':
        return redirect(url_for('words'))
    elif request.form.get('game_button') == 'test2':
        return redirect(url_for('simple_tenses'))
    elif request.form.get('game_button') == 'test3':
        return redirect(url_for('simple_tenses'))
    elif request.form.get('game_button') == 'test4':
        return redirect(url_for('simple_tenses'))
    elif request.form.get('game_button') == 'test5':
        return redirect(url_for('simple_tenses'))


@app.route('/words', methods=['GET', 'POST'])
def words():
    res = make_response()
    value_of_cookie = request.cookies.get('words', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    if request.method == 'POST':
        if cookie_value_dictionary['question'] >= len(english_excercices_first_test):
            return redirect(url_for('finish_words'))
        elif cookie_value_dictionary['question'] < len(english_excercices_first_test):   
            my_seed = cookie_value_dictionary['seed']
            question =  cookie_value_dictionary['question']         
            user_list_for_check = create_random_words_for_user(my_seed, english_excercices_first_test)
            answer = request.form.get('word')
            if check_answer(question, answer, answers_eng_keys, user_list_for_check):
                cookie_value_dictionary['count'] += 1
            cookie_value_dictionary['question'] += 1
            res = redirect(url_for('words'))
            res.set_cookie('words', from_dict_to_cookie(cookie_value_dictionary))
            return res
    else:
        if cookie_value_dictionary['question'] >= len(english_excercices_first_test):
            return redirect(url_for('finish_words'))
        else:
            my_seed = cookie_value_dictionary['seed']
            question = cookie_value_dictionary['question']
            dictionary_dict = create_random_words_for_user(my_seed, english_excercices_first_test)[question]
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


@app.route('/simple_tenses', methods=['GET', 'POST'])
def simple_tenses():
    res = make_response()
    value_of_cookie = request.cookies.get('simple_tenses', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    if request.method == 'POST':
        if cookie_value_dictionary['question'] >= len(english_excercices_second_test):
            return redirect(url_for('finish_simple_tenses'))
        elif cookie_value_dictionary['question'] < len(english_excercices_second_test):   
            my_seed = cookie_value_dictionary['seed']
            question =  cookie_value_dictionary['question']         
            user_list_for_check = create_random_words_for_user(my_seed, english_excercices_second_test)
            answer = request.form.get('word')
            if check_answer(question, answer, answers_second_test, user_list_for_check):
                cookie_value_dictionary['count'] += 1
            cookie_value_dictionary['question'] += 1
            res = redirect(url_for('simple_tenses'))
            res.set_cookie('simple_tenses', from_dict_to_cookie(cookie_value_dictionary))
            return res
    else:
        if cookie_value_dictionary['question'] >= len(english_excercices_second_test):
            return redirect(url_for('finish_simple_tenses'))
        else:
            my_seed = cookie_value_dictionary['seed']
            question = cookie_value_dictionary['question']
            dictionary_dict = create_random_words_for_user(my_seed, english_excercices_second_test)[question]
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
            res = make_response(render_template('simple_tenses.html', **exercise))
            return res


@app.route('/finish_words', methods=['GET', 'POST'])
def finish_words():
    res = make_response()
    if request.method == 'POST':
        res = redirect(url_for('index'))
        res.set_cookie('words', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
        return res
    elif request.method == 'GET':
        value_of_cookie = request.cookies.get('words')
        if value_of_cookie == None:
            return redirect(url_for('index'))
        else:
            cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
            count = cookie_value_dictionary['count']
            res = make_response(render_template('finish_words.html', result=count))
            return res


@app.route('/finish_simple_tenses', methods=['GET', 'POST'])
def finish_simple_tenses():
    res = make_response()
    if request.method == 'POST':
        res = redirect(url_for('index'))
        res.set_cookie('simple_tenses', from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
        return res
    elif request.method == 'GET':
        value_of_cookie = request.cookies.get('simple_tenses')
        if value_of_cookie == None:
            return redirect(url_for('index'))
        else:
            cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
            count = cookie_value_dictionary['count']
            res = make_response(render_template('finish_simple_tenses.html', result=count))
            return res
        

if __name__ == "__main__":
    app.run(debug=True) 
