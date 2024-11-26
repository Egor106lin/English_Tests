from flask import Flask, render_template, make_response, redirect, url_for
from flask import request

from word_exercise import context

from cookie_set import from_cookie_to_dict, from_dict_to_cookie
from check_answer import check_answer

app = Flask(__name__)
                    

@app.route('/', methods=['GET', 'POST'])
def index():
    res = make_response()
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'state': 'start', 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    res = make_response(render_template('index.html'))
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    if request.method == 'POST':
        return redirect(url_for('start'))
    return res


@app.route('/start', methods=['GET', 'POST'])
def start():
    res = make_response()
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'state': 'start', 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    res = make_response(render_template('start.html'))
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    if request.method == 'POST':
        return redirect(url_for('words'))
    return res


@app.route('/words', methods=['GET', 'POST'])
def words():
    res = make_response()
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'state': 'words', 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    if cookie_value_dictionary['question'] >= 10:
        return redirect(url_for('finish'))
    elif cookie_value_dictionary['question'] < 10:
        context_list = []
        for key in context:
            context_list.append(key)
        for name in ['word1', 'word2', 'word3', 'word4']:
            answer = request.form.get(name)
            if answer != None:
                cookie_value_dictionary = check_answer(cookie_value_dictionary, answer)
            else:
                continue
        dictionary_list = context[context_list[cookie_value_dictionary['question']]]
        exercise = {
                'number': cookie_value_dictionary['question'] + 1,
                'english_word': dictionary_list[0],
                'translate1': dictionary_list[1],
                'translate2': dictionary_list[2],
                'translate3': dictionary_list[3],
                'translate4': dictionary_list[4],
        }
        cookie_value_dictionary['question'] += 1
        res = make_response(render_template('words.html', **exercise))
        res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
        return res


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    res = make_response()
    value_of_cookie = request.cookies.get('universal')
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    count = cookie_value_dictionary['count']
    res = make_response(render_template('finish.html', result=count))
    cookie_value_dictionary = {'state': 'start', 'question': 0, 'count': 0}
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    if request.method == 'POST':
        return redirect(url_for('start'))
    return res


if __name__ == "__main__":
    app.run(debug=True) 
