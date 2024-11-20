from flask import Flask, render_template, request, make_response
from random import choice

from word_exercise import context
from words_list import words

from cookie_set import from_cookie_to_dict, from_dict_to_cookie
from check_answer import check_answer

app = Flask(__name__)
                    

@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/words/", methods=["GET", "POST"])
def words_page():
    # create res
    res = make_response()
    res.set_cookie('universal', "")
    # make a dictionary with cookie value
    value_of_cookie = request.cookies.get('universal', from_dict_to_cookie({'state': 'start', 'question': 0, 'count': 0}))
    cookie_value_dictionary = from_cookie_to_dict(value_of_cookie)
    # code
    if cookie_value_dictionary['state'] == 'start':
        res = make_response(render_template('start.html'))
        cookie_value_dictionary = {
            'state': 'words',
            'question': 0,
            'count': 0
        }
    elif cookie_value_dictionary['state'] == 'words':
        if cookie_value_dictionary['question'] < 100:
            context_list = []
            answer = []
            for key in context:
                context_list.append(key)
            for name in ['word1', 'word2', 'word3', 'word4']:
                answer.append(request.form.get(name))
            print(answer)
            if cookie_value_dictionary['question'] != 0:
                check_answer(cookie_value_dictionary, answer)
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
        else:
            cookie_value_dictionary['state'] = 'finish'
            res = make_response(render_template('finish.html', result=cookie_value_dictionary['count']))
    elif cookie_value_dictionary['state'] == 'finish':
        cookie_value_dictionary['state'] = 'start'
        res = make_response(render_template('start.html'))
    # make a string from dictionary
    res.set_cookie('universal', from_dict_to_cookie(cookie_value_dictionary))
    return res

if __name__ == "__main__":
    app.run(debug=True) 
