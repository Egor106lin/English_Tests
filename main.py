from flask import Flask
from flask import request

from flask import render_template, make_response, redirect, url_for
import random

from word_exercise import create_random_words_for_user
from cookie_set import from_cookie_to_dict, from_dict_to_cookie

from check_answer import check_answer
from words_list import english_excercices_first_test, answers_eng_keys

from words_list import english_excercices_second_test, answers_second_test
from words_list import english_excercices_third_test, answers_third_test

app = Flask(__name__)


def create_seed() -> int:
    '''This function generate random int as a seed for user.'''
    seed = random.randint(0, 10**10)
    return seed


def test(page_name: str, exercises_list, answers):
    res = make_response()
    value_of_cookie = request.cookies.get(page_name, from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    if request.method == 'POST':
        if cookie_value_dictionary['question'] >= len(exercises_list):
            return redirect(url_for('finish_words'))
        elif cookie_value_dictionary['question'] < len(exercises_list):   
            my_seed = cookie_value_dictionary['seed']
            question =  cookie_value_dictionary['question']         
            user_list_for_check = create_random_words_for_user(my_seed, exercises_list)
            answer = request.form.get('option')
            if check_answer(question, answer, answers, user_list_for_check):
                cookie_value_dictionary['count'] += 1
            cookie_value_dictionary['question'] += 1
            res = redirect(url_for(page_name))
            res.set_cookie(page_name, from_dict_to_cookie(cookie_value_dictionary))
            return res
    else:
        if cookie_value_dictionary['question'] >= len(exercises_list):
            return redirect(url_for(f'finish_{page_name}'))
        else:
            my_seed = cookie_value_dictionary['seed']
            question = cookie_value_dictionary['question']
            dictionary_dict = create_random_words_for_user(my_seed, exercises_list)[question]
            dictionary_key = next(iter(dictionary_dict))
            dictionary_list = dictionary_dict[dictionary_key]
            exercise = {
                    'number': cookie_value_dictionary['question'] + 1,
                    'english_word': dictionary_key,
                    'translate1': dictionary_list[0],
                    'translate2': dictionary_list[1],
                    'translate3': dictionary_list[2],
                    'translate4': dictionary_list[3],
                    'form_path': f'/{page_name}'
            }
            res = make_response(render_template('test.html', **exercise))
            return res


def finish(page_name: str):
    res = make_response()
    if request.method == 'POST':
        res = redirect(url_for('index'))
        res.set_cookie(page_name, from_dict_to_cookie({'seed': create_seed(), 'question': 0, 'count': 0}))
        return res
    elif request.method == 'GET':
        value_of_cookie = request.cookies.get(page_name)
        if value_of_cookie == None:
            return redirect(url_for('index'))
        else:
            cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
            count = cookie_value_dictionary['count']
            res = make_response(render_template(f'finish.html', result=count))
            return res


@app.route('/', methods=['GET'])
def index():
    return make_response(render_template('index.html'))


@app.route('/', methods=['POST'])
def index_post():
    test = request.form.get('game_button')
    return redirect(url_for(test))


@app.route('/grammar', methods=['GET', 'POST'])
def grammar():
    return test('grammar', english_excercices_second_test, answers_second_test)
        

@app.route('/modals', methods=['GET', 'POST'])
def modals():
    return test('modals', english_excercices_third_test, answers_third_test)


@app.route('/finish_grammar', methods=['GET', 'POST'])
def finish_grammar():
    return finish('grammar')


@app.route('/finish_modals', methods=['GET', 'POST'])
def finish_modals():
    return finish('modals')


if __name__ == "__main__":
    app.run(debug=True) 
