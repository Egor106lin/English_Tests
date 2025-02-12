answers_english_tenses_test = {}
answers_modals_test = {}
answers_comparisons_test = {}
answers_there_is_are_test = {}
answers_plurals_test = {}
answers_sports_hobbies_test = {}
answers_house_test = {}
answers_daily_routine_test = {}
answers_shopping_test = {}
answers_life_exp_test = {}

english_tenses_test_original = [
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
    {'She ___ up and ___ to school every day at 7 am.': ['wakes, goes', 'wake, goes', 'woke, go', 'wake, go']},
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
    {'Sally ___ argument with her parents.': ['should not', 'do not have to', 'have to', 'should']},
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
    {'What a nice cat! It is ___ (beautiful) than mine.': ['more beautiful', 'beautiful', 'beautifuler', 'beautifulest']},
    {'Here is Masha. She is five, her brother is nine. He is ___ (old)': ['older', 'the oldest', 'more old', 'most old']},
    {'This is ___ (difficult) exercise in the test.': ['the most difficult', 'difficulter', 'difficultest', 'more difficult']},
    {'My mother thinks that teaching is ___ (good) job in the world.': ['the best', 'good', 'better', 'the goodest']},
    {'Rugby is ___ (dangerous) than soccer.': ['more dangerous', 'dangerouser', 'dangerousest', 'the most dangerous']},
    {'Failing an exam is ___ (bad) thing that could ever happen to me.': ['the worst', 'the worse', 'bad', 'more bad']},
    {'Bungee jumping is ___ (exciting) than skateboarding.': ['more exciting', 'the exciting', 'the most exciting', 'excitinger']},
    {'To my opinion, swimming is ___ (easy) than running.': ['easier', 'more easy', 'the most easy', 'easiest']},
    {'This e-reader is ___ (cheap) than that one.': ['cheaper', 'more cheap', 'the most cheap', 'cheapest']},
    {'Russia has got ___ (many) gold medals at the Olympics.': ['the most', 'more', 'many', 'maniest']},
    {'Oksana is seven month ___ (old) than me.': ['older', 'more old', 'oldest', 'the oldest']},
    {'She is ___ (tall) than me.': ['taller', 'more tall', 'the tallest', 'tall']},
    {'She is ___ (fast) swimmer in the team.': ['the fastest', 'faster', 'the most fast', 'fastest']},
    {'She is ___ (successful) athlete in the team.': ['the most successful', 'the successful', 'successfulest', 'successfuler']},
    {'Is the Mersedes ___ (long) than BMW?': ['longer', 'more long', 'the longest', 'the longer']},
    {'Which building is ___ (high) in London?': ['the highest', 'the most high', 'higher', 'more high']},
    {'Today the weather is ___ (cold) than it was yesterday.': ['colder', 'more colder', 'more cold', 'the coldest']},
    {'Our town is ___ (old) in our region.': ['the oldest', 'older than', 'the most old', 'oldest']},
    {'This is ___ (beautiful) car in this room.': ['the most beautiful', 'the beautifulest', 'beautifuler', 'more beautiful']},
    {'Jane is ___ (short) of the five girls.': ['the shortest', 'shorter', 'more short', 'shortest']},
    {'Tim is ___ (good) person in his class.': ['the best', 'the goodest', 'better', 'the good']},
    {'This bear is ___ (big) in the zoo.': ['the biggest', 'the most big', 'biggest', 'the bigger']},
    {'Our flag is ___ (beautiful) than their flag.': ['more beautiful', 'beautifuler', 'beautifulest', 'the more beautiful']},
    {'Today is ___ (hot) day of month.': ['the hottest', 'hotter', 'more hot', 'hottest']},
    {'The mouse is ___ (small) than cat.': ['smaller', 'smallest', 'more small', 'the smaller']},
    {'My hands are ___ (clean) than yours.': ['cleaner', 'cleanest', 'more clean', 'the cleaner']},
    {'Russia is ___ (large) country.': ['the largest', 'larger', 'the larger', 'more large']},
    {'This is ___ (funny) story I have ever heard.': ['the funniest', 'most funny', 'funnier', 'the more funny']},
    {'The room is ___ (small) of all the rooms in the house.': ['the smallest', 'smaller', 'more small', 'the small']},
    {'Which is ___ (hot) day in the month.': ['the hottest', 'more hot', 'most hot', 'hotter']},
]

there_is_are_test_original = [
    {'___ a cofee table in your living room?': ['Is there', 'Are there', 'There is', 'There are']},
    {'___ a sofa in your living room?': ['Is there', 'Are there', 'There is', 'There are']},
    {'___ any cushions on the sofa in your room?': ['Are there', 'Is there', 'There are', 'There is']},
    {'___ any chairs in the kitchen?': ['Are there', 'Is there', 'There are', 'There is']},
    {'___ any curtains at the windows of your bathroom?': ['Are there', 'Is there', 'There is', 'There are']},
    {'___ a mirror in the bedroom?': ['Is there', 'Are there', 'There is', 'There are']},
    {'___ a picture in your room?': ['Is there', 'Are there', 'There is', 'There are']},
    {'___ a portrait on the wall.': ['There is', 'There are', 'Is there', 'Are there']},
    {'___ any orange in the fridge?': ['Is there', 'Are there', 'There is', 'There are']},
    {'___ any computer in the room.': ['There is not', 'There are not', 'There is', 'There are']},
    {'___ some newspapers on the floor.': ['There are', 'There is', 'Is there', 'There are not']},
    {'___ any cupboards in the bathroom.': ['There are not', 'There is not', 'There are', 'There is']},
    {'___ any new sofas in the hotel?': ['Are there', 'Is there', 'Are nor there', 'Is not there']},
    {'___ any window in the bedroom.': ['There is not', 'There are not', 'There is', 'There are']},
    {'___ an armchair in the room.': ['There is', 'There are', 'There is not', 'There are not']},
    {'___ some chairs in the kitchen.': ['There are', 'There is', 'There are not', 'Are there']},
    {'___ a mirror in the bathroom.': ['There is', 'There are', 'Is there', 'Are there']},
    {'___ a bottle of water?': ['Is there', 'Are there', 'Is not there', 'There is']},
    {'___ a knife and scissors.': ['There is', 'There are', 'Is there', 'Are there']},
    {'___ a bottle of water and bottle of coke.': ['There is', 'There are', 'It is', 'There are not']},
    {'___ exercises in this book.': ['There are', 'There is', 'Is there', 'Are there']},
    {'___ grammar exercises and vocabulary exercises in this book.': ['There is', 'There are', 'Are there', 'Is there']},
    {'___ some eggs in the fridge.': ['There are', 'There is', 'Are there', 'Is there']},
    {'___ an egg in the fridge.': ['There is', 'There are', 'Are there', 'Is there']},
    {'___ an egg, a banana and a chicken in the fridge.': ['There is', 'There are', 'Are there', 'Is there']},
    {'___ some cats, and they want to live in house with big family. ': ['There are', 'There is', 'There are not', 'There is not']},
    {'___ some kilos of tomatos.': ['There are', 'There is', 'There are not', 'There is not']},
    {'___ a lot of beautiful flowers in the garden.': ['There are', 'There is', 'There are not', 'There is not']},
    {'___ some vegetables in the kitchen.': ['There are', 'There is', 'There are not', 'There is not']},
    {'___ any pedants.': ['There are not', 'There is', 'There are', 'There is not']},
]

plurals_test_original = [
    {'woman': ['women', 'womans', 'womanies', 'womaners']},
    {'child': ['children', 'childs', 'childrens', 'childrenies']},
    {'person': ['people', 'persons', 'peopler', 'peoplies']},
    {'man': ['men', 'mans', 'mens', 'manies']},
    {'fish': ['fish', 'fishs', 'fishes', 'fishers']},
    {'foot': ['feet', 'foots', 'feet', 'feeties']},
    {'tooth': ['teeth', 'tooths', 'toothes', 'teeths']},
    {'mouse': ['mice', 'mouses', 'mousers', 'mices']},
    {'roof': ['roofs', 'roofes', 'rouf', 'roofers']},
    {'radio': ['radios', 'radio', 'radioes', 'radioies']},
    {'piano': ['pianos', 'pianers', 'pianoes', 'piano']},
    {'photo': ['photos', 'photo', 'photografs', 'photoes']},
    {'video': ['videos', 'videoes', 'video', 'videous']},
    {'rhino': ['rhinos', 'rhinoes', 'rhinoies', 'rhinoues']},
    {'hippo': ['hippos', 'hippo', 'hippoes', 'hippoies']},
    {'raspberry': ['raspberries', 'raspberrys', 'raspberry', 'raspberryes']},
    {'baby': ['babies', 'babys', 'babyes', 'baby']},
    {'wolf': ['wolves', 'wolfs', 'wolfes', 'wolf']},
    {'wife': ['wives', 'wifes', 'wifies', 'wifeses']},
    {'sofa': ['sofas', 'sofa', 'sofaes', 'sofies']},
    {'sheep': ['sheeps', 'shep', 'sheepes', 'sheepos']},
    {'son': ['sons', 'sun', 'sones', 'sonies']},
    {'butterfly': ['butterflies', 'butterflys', 'butterfly', 'butterflie']},
    {'city': ['cities', 'citys', 'cites', 'city']},
    {'family': ['families', 'familyes', 'familys', 'family']},
    {'day': ['days', 'daies', 'dayses', 'dayes']},
    {'story': ['stories', 'storys', 'stores', 'stors']},
    {'country': ['countries', 'countrys', 'countres', 'countreses']},
    {'zebra': ['zebras', 'zebraes', 'zebra', 'zebraies']},
    {'strong man': ['strong men', 'strongs men', 'strong mens', 'strong mans']},
]

sports_hobbies_test_original = [
    {'horse-riding': ['езда на лощади', 'уход за лошадью', 'езда на велосипеде', 'седло']},
    {'volleyball': ['воллейбол', 'играть в воллейбол', 'воллейболист', 'воллейбольный мяч']},
    {'photography': ['фотографирование', 'фотограф', 'скриншот', 'пейзаж']},
    {'playing music': ['играть музыку', 'слушать музыку', 'песня', 'музыкальный инструмент']},
    {'woodwork': ['работа с деревом', 'изделие из дерева', 'столяр', 'плотник']},
    {'reading': ['чтение', 'книга', 'страница', 'записывание']},
    {'cycling': ['езда на велосипеде', 'путешествовать', 'езда на мотоцикле', 'рисование']},
    {'painting': ['рисование', 'картина', 'художник', 'скульптура']},
    {'playing computer games': ['играть в компьютерные игры', 'компьютерная игра', 'играть в настолки', 'киберспортсмен']},
    {'writing': ['письмо', 'книга', 'автор', 'чтение']},
    {'student': ['ученик', 'учитель', 'учебник', 'обучение']},
    {'basketball player': ['баскетболист', 'тренер по баскетболу', 'баскетбольный мяч', 'капитан баскетбольной команды']},
    {'hero': ['персонаж', 'главный герой', 'игрок', 'тренер']},
    {'team': ['команда', 'состязание', 'игрок', 'матч']},
    {'tennis club': ['теннисный клуб', 'клуб интересов', 'спортшкола', 'теннисный корт']},
    {'famous': ['известный', 'крутой', 'популярный', 'соцсеть']},
    {'favourite': ['любимый', 'избранный', 'плохой', 'другой']},
    {'football': ['футбол', 'вратарь', 'футболист', 'хоккей']},
    {'boxing': ['бокс', 'боксер', 'коробка', 'упаковать']},
    {'golf': ['гольф', 'игрок в гольф', 'шарик для гольфа', 'гольфкар']},
]

house_test_original = [
    {'fridge': ['холодильник', 'кофеварка', 'заморозка', 'стиральная машина']},
    {'washing machine': ['стиральная машина', 'посудомоечная машина', 'сушильная машина', 'гараж']},
    {'dishwasher': ['посудомоечная машина', 'стиральная машина', 'сушилка', 'шкаф для посуды']},
    {'toaster': ['тостер', 'утюг', 'полотенцесушитель', 'туалет']},
    {'iron': ['утюг', 'железо', 'шкаф', 'гардероб']},
    {'cooker': ['плита', 'микроволновая печь', 'повар', 'обед']},
    {'vacuum cleaner': ['пылесос', 'вакуумный очиститель', 'духовка', 'робот-пылесос']},
    {'wash': ['мыть', 'помытый', 'посуда', 'мытье']},
    {'catch': ['ловить', 'опоздать', 'поймать', 'починить']},
    {'neighbourhood': ['район', 'сосед', 'соседство', 'внутренний двор']},
    {'chore': ['обязанность', 'благотворительность', 'обязательство', 'обещать']},
    {'floating dust': ['взвешенная пыль', 'летающая пыль', 'уборка', 'пыль на полках']},
    {'pipe': ['труба', 'средство для мытья посуды', 'средство для влажной уборки', 'подушка']},
    {'mealtime': ['прием пищи', 'ужин', 'обед', 'приготовление пищи']},
    {'tin': ['жестяная банка', 'галстук', 'вареная сгущенка', 'кладовая']},
    {'packet': ['пакет', 'коробка', 'хранилище', 'подвал']},
    {'disposable clothes': ['одноразовая одежда', 'старая одежда', 'рваная одежда', 'грязная одежда']},
    {'wet': ['мокрый', 'питомец', 'сухой', 'вода']},
    {'bathroom': ['ванная комната', 'влажная уборка', 'туалет', 'бассейн']},
    {'wardrobe': ['гардероб', 'шкаф', 'спальня', 'гардеробщик']},
]

daily_routine_test_original = [
    {'get up': ['проснуться', 'идти', 'засыпать', 'понять']},
    {'have a shower': ['принять душ', 'умываться', 'чистить', 'помыть голову']},
    {'have breakfast': ['позавтракать', 'поужинатать', 'пообедать', 'перекусить']},
    {'go to school': ['идти в школу', 'идти из школы', 'перейти в новую школу', 'прийти на урок']},
    {'have lessons': ['сидеть на уроках', 'учить уроки', 'стаивть отметки', 'проверять задания']},
    {'do sport': ['заниматься спортом', 'урок физкультуры', 'соревноваться', 'спортсмен']},
    {'have dinner': ['ужинать', 'завтракать', 'обедать', 'готовить завтрак']},
    {'do my homework': ['делать домашнее задание', 'написать контрольную работу', 'домашнее сочинение', 'домашка от репетитора']},
    {'walk the dog': ['гулять с собакой', 'завести собаку', 'выгуливать кота', 'покормить собаку']},
    {'watch a DVD': ['смотреть DVD', 'смотреть фильмы', 'слушать музыку с DVD', 'смотреть сериал']},
    {'brush my teeth': ['чистить зубы', 'умываться', 'использовать зубную нить', 'лечить зуб']},
    {'go to bed': ['идти спать', 'заправлять кровать', 'проснуться', 'спать']},
    {'office work': ['работа в офисе', 'офисный работяга', 'офис', 'работать удаленно']},
    {'comb hair': ['расчесывать волосы', 'укладывать волосы', 'мыть голову', 'стричься']},
    {'put on make up': ['краситься', 'одеваться', 'собираться', 'прихорашиваться']},
    {'get dressed': ['одеваться', 'надеть платье', 'одеть кого-либо', 'купить одежду']},
    {'turn off the alarm': ['выключать будильник', 'поставить будильник', 'проснуться по будильнику', 'проснуться раньше будильника']},
    {'make the bed': ['заправлять постель', 'ложиться спать', 'проснуться', 'купить кровать']},
    {'wash face': ['умывать лицо', 'мыться', 'чистить зубы', 'краситься']},
    {'do my project': ['работать над проектом', 'делать домашнее задание', 'помогать учителю', 'придумать идею для проекта']},
]

shopping_test_original = [
    {'flat shoes': ['туфли на плоской подошве', 'официальные туфли', 'летающие ботинки', 'сапоги']},
    {'high heels': ['высокие каблуки', 'низкие каблуки', 'кеды', 'туфли']},
    {'leggings': ['леггинсы', 'спортивки', 'велосипедки', 'высокие носки']},
    {'socks': ['носки', 'штаны', 'бант', 'школьные носки']},
    {'sandals': ['сандали', 'кроссовки', 'кепка', 'солнечные очки']},
    {'boots': ['обувь', 'кроссовки', 'штаны', 'туфли']},
    {'trainers': ['кроссовки', 'спортивки', 'майка', 'спортивные шорты']},
    {'trousers': ['брюки', 'тренировочная одежда', 'штаны', 'шорты']},
    {'skirt': ['юбка', 'галстук', 'рубашка', 'брюки']},
    {'top': ['топ', 'кепка', 'верхняя одежда', 'бахилы']},
    {'coat': ['пальто', 'свитер', 'джемпер', 'худи']},
    {'dress': ['платье', 'одежда', 'постельное бельё', 'юбка']},
    {'gloves': ['перчатки', 'одежда', 'штаны', 'шорты']},
    {'hat': ['шляпа', 'кепка', 'бейсболка', 'пальто']},
    {'sunglasses': ['солнечные очки', 'прозрачные очки', 'очки', 'яркий стакан']},
    {'scarve': ['шарф', 'юбка', 'балаклава', 'маска']},
    {'cap': ['кепка', 'пуговица', 'бейсболка', 'маска']},
    {'bag': ['сумка', 'рюкзак', 'шоппер', 'мешок']},
    {'sweatshirt': ['фуфайка', 'шорты', 'футболка с длинным рукавом', 'свитшот']},
    {'shirt': ['рубашка', 'юбка', 'шарф', 'шорты']},
]

life_exp_test_original = [
    {'fly over a place in a helicopter': ['пролететь над каким-нибудь местом на вертолете', 'полетать на частном вертолете', 'путешествовать на вертолете', 'посмотреть на место на квадрокоптере']},
    {'go camping': ['жить в палатке', 'дом на колесах', 'путешествовать на велосипеде', 'купить палатку']},
    {'travel in a camper van': ['путешествовать в доме на колесах', 'путешествие на пароме', 'путешествие в автобусе', 'купить дом на колесах']},
    {'cycle across country': ['проехать на велосипеде через страну', 'чемпионат страны по езде на велосипеде', 'проехать деревню на велосипеде', 'лучший велосипедист страны']},
    {'sail on a yacht': ['ходить под парусом на яхте', 'распродажа яхт', 'кататься на яхте', 'кататься на лодке']},
    {'ride an elephant': ['ездить верхом на слоне', 'приручить слона', 'покататься на верблюде', 'цирковой слон']},
    {'drive a quad bike': ['кататься на аквабайке', 'медленно ездить на мотоцикле', 'кататься на цирковом мотоцикле', 'починить мотоцикл']},
    {'climb a volcano': ['взбираться на вулкан', 'наблюдать за извержением вулкана', 'упасть в жерло вулкана', 'фотографировать вулкан']},
    {'ride a camel': ['ездить верхом на верблюде', 'ездить верхом на лошади', 'путешествовать по пустыне', 'арендовать верблюда']},
    {'go bungee jumping': ['пргынуть с таразанки', 'путешествовать в джунглях', 'прыгать с деревьев', 'охотиться в джунглях']},
    {'dive with sharks': ['плавать под водой с акулами', 'дайвинг с дельфинами', 'рисовать акул', 'мультик с акулами']},
    {'ski down a mountain': ['кататься на лыжах с горы', 'прыгать с горы', 'ходить под парусом на горном озере', 'спускаться вниз по горной реке']},
    {'jump out of a plane': ['прыгать с парашютом из самолета', 'прыгать с парашютом с моста', 'покинуть рейс', 'лететь на самолете']},
    {'swim with dolphins': ['плавать с дельфинами', 'сходить в дельфинариум', 'поругаться с дельфинами', 'бассейн с дельфинами']},
    {'try ice climbing': ['попробовать ледолазание', 'поскользнуться на льду', 'попробовать лед на вкус', 'разбить лед']},
    {'river cruise': ['речной круиз', 'речной паром', 'сплав по реке', 'речная переправа']},
    {'canoe': ['каноэ', 'лодка', 'плот', 'катамаран']},
    {'ferry ride': ['поездка на пароме', 'отправиться в круиз', 'путешествие по реке', 'морской паром']},
    {'explore ancient ruins': ['исследовать древние руины', 'попробовать себя в роли археолога', 'извержение вулкана на месте древнего города', 'посмотреть на памятник древним цивилизациям']},
    {'make a dream come true': ['исполнить мечту', 'загадать желание', 'стать счастливым', 'выполнить цель']},
]


for w in english_tenses_test_original:
    for k, v in w.items():
        answers_english_tenses_test[k] = v[0]

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
