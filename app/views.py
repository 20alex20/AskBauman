from django.shortcuts import render


qs = [
    {
        "id": i + 1,
        "title": "How Did You Hear About This Position?",
        "answers": 28,
        "likes": 78,
        "datetime": "4 мин назад",
        "tags": ["Developer", "Computer"],
        "solved": True,
        "text": "Wouldn’t it be great if you knew exactly what questions a hiring manager would be asking you in "
                "your next job interview?\nWe can’t read minds, unfortunately, but we’ll give you the next best "
                "thing: a list of more than 40 of the most commonly asked interviewquestions, along with advice "
                "for answering them all.\nWhile we don’t recommend having a canned response for every interview "
                "question (in fact, please don’t), we do recommend spending some time getting comfortable with "
                "what you might be asked, what hiring managers are really looking for in your responses, and what "
                "it takes to show that you’re the right person for the job."
    } for i in range(20)
]
tags = ["analytics", "Computer", "Developer", "Google", "Interview", "Programmer", "Salary", "University", "Employee"]
leaders = [
    {
        "id": i,
        "nickname": "alex_fnaf",
        "points": 206,
        "type": "Гений"
    } for i in range(5)
]


def index(request):
    qs2 = [
        {
            "id": i + 1,
            "title": "Why Do You Want This Job?",
            "answers": 10,
            "likes": 10,
            "datetime": "01.01.2023",
            "tags": [],
            "solved": False,
            "text": "Duis dapibus aliquam mi, eget euismod sem scelerisque ut. Vivamus at elit quis urna adipiscing "
                    "iaculis.Duis dapibus aliquam mi, eget euismod sem scelerisque ut. Vivamus at elit quis urna "
                    "adipiscing iaculis."
        } for i in range(20, 40)
    ]
    return render(request, 'index.html', {"directory": None, "page": "Главная", "leaders": leaders,
                                          "questions": qs, "questions2": qs2, "tags": tags})


def tag(request, page):
    return render(request, 'tag.html', {"directory": "Вопросы по тегам", "page": page, "leaders": leaders,
                                        "questions": qs, "tags": tags})


def question(request, id):
    return render("", {"id": id})


def ask(request):
    return render(request, 'ask_question.html', {"directory": "Личный кабинет", "page": "Задать вопрос",
                                                 "leaders": leaders, "tags": tags})


def settings(request):
    user = {
        "id": 2,
        "login": "alexf",
        "nickname": "alex_fnaf",
        "email": "alex@gmail.com"
    }
    return render(request, 'user_info.html', {"directory": "Личный кабинет", "page": "Задать вопрос",
                                              "leaders": leaders, "tags": tags, "user": user})


def my_qs(request):
    qs3 = [
        {
            "id": i + 1,
            "title": "How Did You Hear About This Position?",
            "answers": 28,
            "likes": 78,
            "datetime": "4 мин назад",
            "tags": ["Developer", "Computer"],
            "solved": True,
            "text": "Wouldn’t it be great if you knew exactly what questions a hiring manager would be asking you in "
                    "your next job interview?\nWe can’t read minds, unfortunately, but we’ll give you the next best "
                    "thing: a list of more than 40 of the most commonly asked interviewquestions, along with advice "
                    "for answering them all.\nWhile we don’t recommend having a canned response for every interview "
                    "question (in fact, please don’t), we do recommend spending some time getting comfortable with "
                    "what you might be asked, what hiring managers are really looking for in your responses, and what "
                    "it takes to show that you’re the right person for the job."
        } for i in range(5)
    ]
    return render(request, 'tag.html', {"directory": "Личный кабинет", "page": "Мои вопросы", "leaders": leaders,
                                        "questions": qs3, "tags": tags})
