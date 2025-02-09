from flask import Flask
from flask import request

from flask import render_template, make_response, redirect, url_for
import random

from word_exercise import create_random_words_for_user
from cookie_set import from_cookie_to_dict, from_dict_to_cookie

from check_answer import check_answer
from words_list import *

app = Flask(__name__)


def create_seed() -> int:
    '''This function generate random int as a seed for user.'''
    seed = random.randint(0, 10**10)
    return seed


def test(page_name: str, exercises_list: list[dict[list]], answers: dict):
    '''This function return page with question and answers and check previous answers.'''
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
                    'option1': dictionary_list[0],
                    'option2': dictionary_list[1],
                    'option3': dictionary_list[2],
                    'option4': dictionary_list[3],
                    'form_path': f'/{page_name}'
            }
            res = make_response(render_template('test.html', **exercise))
            return res


def finish(page_name: str, max_result: str):
    '''This function return page with user's answers count.'''
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
            test_names = {
                'grammar': 'Простые времена',
                'modals': 'Модальные глаголы',
                'comparisons': 'Степени сравнения прилагательных',
                'there_is_are': 'Конктркции There is/are',
                'plurals': 'Грамматическое число',
                'sports_hobbies': 'Спорт и хобби',
                'house': 'Дом',
                'daily_routine': 'Ежедневная рутина',
                'shopping': 'Шоппинг',
                'life_exp': 'Жизненный опыт',
            }
            result_feed = {
                'result': count,
                'max_result': max_result,
                'test_name': test_names[page_name]
            }
            if max_result == 30:
                result_feed['mark2'] = '0-10'
                result_feed['mark3'] = '11-17'
                result_feed['mark4'] = '18-25'
                result_feed['mark5'] = '26-30'
            elif max_result == 20:
                result_feed['mark2'] = '0-5'
                result_feed['mark3'] = '6-12'
                result_feed['mark4'] = '13-17'
                result_feed['mark5'] = '18-20'
            res = make_response(render_template('finish.html', **result_feed))
            return res


@app.route('/', methods=['GET'])
def index():
    return make_response(render_template('index.html'))


@app.route('/', methods=['POST'])
def index_post():
    return redirect(url_for(request.form.get('game_button')))


@app.route('/grammar', methods=['GET', 'POST'])
def grammar():
    return test('grammar', grammar_test_original, answers_grammar_test)
        

@app.route('/modals', methods=['GET', 'POST'])
def modals():
    return test('modals', modals_test_original, answers_modals_test)


@app.route('/comparisons', methods=['GET', 'POST'])
def comparisons():
    return test('comparisons', comparisons_test_original, answers_comparisons_test)


@app.route('/there_is_are', methods=['GET', 'POST'])
def there_is_are():
    return test('there_is_are', there_is_are_test_original, answers_there_is_are_test)


@app.route('/plurals', methods=['GET', 'POST'])
def plurals():
    return test('plurals', plurals_test_original, answers_plurals_test)


@app.route('/sports_hobbies', methods=['GET', 'POST'])
def sports_hobbies():
    return test('sports_hobbies', sports_hobbies_test_original, answers_sports_hobbies_test)


@app.route('/house', methods=['GET', 'POST'])
def house():
    return test('house', house_test_original, answers_house_test)


@app.route('/daily_routine', methods=['GET', 'POST'])
def daily_routine():
    return test('daily_routine', daily_routine_test_original, answers_daily_routine_test)


@app.route('/shopping', methods=['GET', 'POST'])
def shopping():
    return test('shopping', shopping_test_original, answers_shopping_test)


@app.route('/life_exp', methods=['GET', 'POST'])
def life_exp():
    return test('life_exp', life_exp_test_original, answers_life_exp_test)


@app.route('/finish_grammar', methods=['GET', 'POST'])
def finish_grammar():
    return finish('grammar', 30)


@app.route('/finish_modals', methods=['GET', 'POST'])
def finish_modals():
    return finish('modals', 30)


@app.route('/finish_comparisons', methods=['GET', 'POST'])
def finish_comparisons():
    return finish('comparisons', 30)


@app.route('/finish_there_is_are', methods=['GET', 'POST'])
def finish_there_is_are():
    return finish('there_is_are', 30)


@app.route('/finish_plurals', methods=['GET', 'POST'])
def finish_plurals():
    return finish('plurals', 30)


@app.route('/finish_sports_hobbies', methods=['GET', 'POST'])
def finish_sports_hobbies():
    return finish('sports_hobbies', 20)


@app.route('/finish_house', methods=['GET', 'POST'])
def finish_house():
    return finish('house', 20)


@app.route('/finish_daily_routine', methods=['GET', 'POST'])
def finish_daily_routine():
    return finish('daily_routine', 20)


@app.route('/finish_shopping', methods=['GET', 'POST'])
def finish_shopping():
    return finish('shopping', 20)


@app.route('/finish_life_exp', methods=['GET', 'POST'])
def finish_life_exp():
    return finish('life_exp', 20)


if __name__ == "__main__":
    app.run() 
