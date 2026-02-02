class Quiz:
    def __init__(self):
        self.questions = [
    {
        "question": "Из чего была сделана карета Золушки?",
        "options": ["Кабачок", "Арбуз", "Тыква", "Дыня"],
        "correct": "Тыква",
        "image": "cinderella.jpg"
    },
    {
        "question": "Какой гном из «Белоснежки» никогда не разговаривал?",
        "options": ["Ворчун", "Простачок", "Соня", "Скромник"],
        "correct": "Простачок",
        "image": "dwarfs.jpg"
    },
    {
        "question": "Какое «оружие» Рапунцель использовала против Флина Райдера?",
        "options": ["Скалка", "Сковородка", "Швабра", "Расческа"],
        "correct": "Сковородка",
        "image": "rapunzel_pan.jpg"
    },
    {
        "question": "Как звали верного хамелеона Рапунцель?",
        "options": ["Максимус", "Паскаль", "Себастьян", "Флаундер"],
        "correct": "Паскаль",
        "image": "pascal.jpg"
    },
    {
        "question": "Что Грю пытался украсть в первой части «Гадкий я»?",
        "options": ["Статую Свободы", "Эйфелеву башню", "Луну", "Пирамиду"],
        "correct": "Луну",
        "image": "gru_moon.jpg"
    },
    {
        "question": "На каком языке говорят миньоны?",
        "options": ["Эльфийский", "Миньонский", "Французский", "Язык жестов"],
        "correct": "Миньонский",
        "image": "minions.jpg"
    },
    {
        "question": "Кем был лидер команды в мультфильме «Плохие парни»?",
        "options": ["Пиранья", "Акула", "Волк", "Змея"],
        "correct": "Волк",
        "image": "bad_guys_wolf.jpg"
    },
    {
        "question": "Какое животное в «Плохих парнях» было мастером маскировки?",
        "options": ["Акула", "Тарантул", "Волк", "Пиранья"],
        "correct": "Акула",
        "image": "shark_mask.jpg"
    },
    {
        "question": "Какого цвета шерсть у Гринча?",
        "options": ["Красная", "Синяя", "Зеленая", "Желтая"],
        "correct": "Зеленая",
        "image": "grinch_green.jpg"
    },
    {
        "question": "Как зовут единственного друга Гринча (собаку)?",
        "options": ["Бадди", "Макс", "Чарли", "Рокки"],
        "correct": "Макс",
        "image": "grinch_dog.jpg"
    },
    {
        "question": "Кто из Смешариков живет в домике-ананасе и любит огород?",
        "options": ["Крош", "Копатыч", "Лосяш", "Пин"],
        "correct": "Копатыч",
        "image": "kopatych.jpg"
    },
    {
        "question": "Какой Смешарик говорит с немецким акцентом и строит роботов?",
        "options": ["Кар-Карыч", "Бараш", "Пин", "Совунья"],
        "correct": "Пин",
        "image": "pin_inventor.jpg"
    },
    {
        "question": "О чем постоянно пишет стихи Бараш?",
        "options": ["О еде", "О печали и вдохновении", "О гонках", "О науке"],
        "correct": "О печали и вдохновении",
        "image": "barash_poetry.jpg"
    },
    {
        "question": "Кто в Смешариках лучший врач и повар?",
        "options": ["Нюша", "Совунья", "Лосяш", "Ежик"],
        "correct": "Совунья",
        "image": "sovunya.jpg"
    },
    {
        "question": "Какой Смешарик любит кактусы и коллекционирует фантики?",
        "options": ["Крош", "Лосяш", "Ежик", "Бараш"],
        "correct": "Ежик",
        "image": "ezhik.jpg"
    }
]
            
        

    def get_question(self, index):
        if index < len(self.questions):
            return self.questions[index]
        return None

    def total_questions(self):
        return len(self.questions)