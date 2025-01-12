answers_grammar_test = {}
answers_modals_test = {}
answers_comparisons_test = {}
answers_there_is_are_test = {}
answers_plurals_test = {}
answers_sports_hobbies_test = {}
answers_house_test = {}
answers_daily_routine_test = {}
answers_shopping_test = {}
answers_life_exp_test = {}

grammar_test_original = [
    {'I ___ to go outside yesterday.': ['wanted', 'want', 'will want', 'wants']},
    {'She ___ her mother tommorow.': ['will visit', 'visited', 'visit', 'visits']},
    {'He ___ his old brother every day.': ['visits', 'will visit', 'visited', 'visit']},
    {'They ___ about yesterday news.': ['gossip', 'will gossip', 'gossiped', 'gossips']},
    {'He says that it ___ yesterday.': ['worked', 'work', 'works', 'will work']},
    {'Covid ___ seven million people all over the world.': ['killed', 'will kill', 'kill', 'kills']},
    {'He ___ on his girlfriend birthday after two hours.': ['will go', 'went', 'goes', 'go']},
    {'She ___ this huge, tasty burger.': ['ate', 'eat', 'eats', 'will eat']},
    {'It ___ you a lot of energy.': ['gives', 'give', 'will give', 'gave']},
    {'This car ___ a revolution in industry in next four years.': ['will make', 'make', 'makes', 'made']},
    {'Mike ___ cake on his birthday every year': ['eats', 'eat', 'will eat', 'ate']},
    {'Users of apple smartphones ___ high quality.': ['love', 'loves', 'loved', 'will love']},
    {'Next week it ___ the best party of this year': ['will be', 'was', 'is', 'will it']},
    {'I am really sad about tragedy in our city, that ___ 2 years ago.': ['was', 'were', 'been', 'will be']},
    {'I ___ English twice a week.': ['study', 'studied', 'will study', 'studies']},
    {'Our mother ___ us to be brave in our ideas in my childhood.': ['teached', 'teach', 'will teach', 'teachs']},
    {'I ___ this one only after salad.': ['will eat', 'ate', 'eats', 'eat']},
    {'He ___ pancakes with honey on breakfast every morning.': ['eats', 'eat', 'ate', 'will eat']},
    {'I will buy this car and ___ every day.': ['drive', 'drives', 'will drive', 'drove']},
    {'My dad ___ this home 10 years ago.': ['bought', 'buy', 'will buy', 'was buy']},
    {'She ___ up and ___ to school every day at 7 am.': ['wakes, goes', 'wake, goes', 'woke, go', 'wake, goes']},
    {'In future, people ___ new planets.': ['will explore', 'explore', 'explores', 'explored']},
    {'Peter the Great ___ Saint-Petersburg in 1703.': ['founded', 'found', 'will found', 'find']},
    {'They ___ in the center of their city every month.': ['walk', 'walks', 'go', 'went']},
    {'I ___ go to school tommorow, because I feel me bad.': ['will not', 'need', 'will', 'want']},
    {'Yesterday, I ___ outside with my mother.': ['went', 'was', 'were not', 'go']},
    {'He ___ go to this shop, because he ___ a lot of time to go here.': ['does not, needs', 'always, needed', 'prefer to, wanted', 'wanted, spent']},
    {'She ___ celebrate New Year, because she is sick.': ['will not', 'will', 'was', 'is']},
    {'His father ___ this travel.': ['forbidden', 'will forbidden', 'cancel', 'was cancel']},
    {'They ___ to go here, because there are a lot of insects.': ['did not want', 'wanted', 'wants', 'want']},
]


modals_test_original = [
    {'We ___ do our homework.': ['must', 'have to', 'do not have to', 'should']},
    {'We ___ be late at school.': ['must not', 'do not have to', 'should not', 'must']},
    {'We ___ be quiet at the lessons.': ['must', 'should', 'have to', 'do not have to']},
    {'You ___ take your rubbish.': ['must', 'have to', 'should', 'do not have to']},
    {'Students ___ run in classes.': ['must not', 'do not have to', 'should not', 'must']},
    {'You ___ feed animals in our zoo!': ['must not', 'must', 'should', 'have to']},
    {'Your mum ___ wear sun hat when it is hot outside.': ['must', 'has to', 'goes', 'go']},
    {'You ___ be kind to others.': ['must', 'should', 'have to', 'should not']},
    {'You ___ be polite with your teachers and parents.': ['must', 'should', 'do not have to', 'have to']},
    {'We ___ speak loudly at the library.': ['must not', 'should not', 'do not have to', 'must']},
    {'You ___ see the new film! It is great!': ['should', 'must', 'have to', 'should not']},
    {'You ___ smoke! It is very bad habit.': ['should not', 'should', 'must not', 'do not have to']},
    {'Your temperature is high. You ___ call to a doctor.': ['should', 'must', 'have to', 'do not have to']},
    {'Sally ___ with her parents.': ['should not', 'do not have to', 'have to', 'should']},
    {'It is so hot outside! You ___ wear a t-shirt.': ['should', 'have to', 'must not', 'should not']},
    {'You ___ eat here. It is a museum.': ['should not', 'do not have to', 'must', 'should']},
    {'Tanya ___ visit her grandparents more often.': ['should', 'have to', 'should not', 'must not']},
    {'You ___ talk to this rude man, it is bad idea.': ['should not', 'should', 'must', 'have to']},
    {'Mike ___ take care of your cat.': ['should', 'should not', 'have to', 'must']},
    {'We ___ help people, who need our help.': ['should', 'do not have to', 'must', 'must not']},
    {'She ___ wake up and go to school every day at 7 am.': ['has to', 'have to', 'should', 'must']},
    {'She does not have to write the test tommorow.': ['does not have to', 'should not', 'must not', 'have to']},
    {'My parents ___ go to supermarket tommorow.': ['have to', 'has to', 'must', 'should not']},
    {'I ___ get up early everyday.': ['have to', 'has to', 'should not', 'must not']},
    {'My sister ___ tidy up her room.': ['has to', 'have to', 'must not', 'should not']},
    {'Jane ___ do her homework.': ['has to', 'have to', 'must not', 'should']},
    {'I ___ take my car to the garage to get it fix.': ['have to', 'has to', 'must', 'should not']},
    {'You ___ attend the meeting if you are sick.': ['do not have to', 'have to', 'has to', 'must']},
    {'We ___ study for our next grammar test.': ['have to', 'has to', 'does not have to', 'should not']},
    {'Your sister ___ help to your mother.': ['has to', 'have to', 'must not', 'should not']},
]

comparisons_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

there_is_are_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

plurals_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

sports_hobbies_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

house_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

daily_routine_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

shopping_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]

life_exp_test_original = [
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
    {'': ['', '', '', '']},
]


for w in grammar_test_original:
    for k, v in w.items():
        answers_grammar_test[k] = v[0]

for w in modals_test_original:
    for k, v in w.items():
        answers_modals_test[k] = v[0]

for w in comparisons_test_original:
    for k, v in w.items():
        answers_comparisons_test[k] = v[0]

for w in there_is_are_test_original:
    for k, v in w.items():
        answers_there_is_are_test[k] = v[0]

for w in plurals_test_original:
    for k, v in w.items():
        answers_plurals_test[k] = v[0]

for w in sports_hobbies_test_original:
    for k, v in w.items():
        answers_sports_hobbies_test[k] = v[0]

for w in house_test_original:
    for k, v in w.items():
        answers_house_test[k] = v[0]

for w in daily_routine_test_original:
    for k, v in w.items():
        answers_daily_routine_test[k] = v[0]

for w in shopping_test_original:
    for k, v in w.items():
        answers_shopping_test[k] = v[0]

for w in life_exp_test_original:
    for k, v in w.items():
        answers_life_exp_test[k] = v[0]
