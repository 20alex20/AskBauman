from django.shortcuts import render
from django.core.paginator import Paginator


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
    } for i in range(150)
]
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
    } for i in range(150, 150 + 90)
]
tags = ["analytics", "Computer", "Developer", "Google", "Interview", "Programmer", "Salary", "University", "Employee"]
users = [
    {
        "id": i,
        "nickname": "alex_fnaf",
        "points": 206,
        "type": "Гений"
    } for i in range(5)
]


def paginate(objects_list, request, name='page', per_page=20):
    paginator = Paginator(objects_list, per_page)
    max_num = paginator.num_pages
    page_num = int(request.GET.get(name, 1))
    if page_num < 1:
        page_num = 1
    elif page_num > max_num:
        page_num = max_num
    return paginator.page(page_num).object_list, page_num, max_num


def index(request):
    obj1, page_num1, max_num1 = paginate(qs, request, 'page1')
    obj2, page_num2, max_num2 = paginate(qs2, request, 'page2')
    return render(request, 'index.html', {"directory": None, "page": "Главная", "leaders": users, "tags": tags,
                                          "authorized": False, "questions": obj1, "questions2": obj2,
                                          "page_num1": page_num1, "max_num1": max_num1,
                                          "range1": range(1, max_num1 + 1), "page_num2": page_num2,
                                          "max_num2": max_num2, "range2": range(1, max_num2 + 1)})


def tag(request, page):
    obj, page_num, max_num = paginate(qs, request)
    return render(request, 'tag.html', {"directory": "Вопросы по тегам", "page": page, "leaders": users, "tags": tags,
                                        "authorized": True, "questions": obj, "page_num": page_num, "max_num": max_num,
                                        "range": range(1, max_num + 1)})


def question(request, page):
    answers = [
        {
            "user": {
                "id": i,
                "nickname": "alex_fnaf"
            },
            "datetime": "01.01.2023 12:00",
            "text": " Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit omnis animi et iure laudantium "
                    "vitae, praesentium optio, sapiente distinctio illo?"
        } for i in range(45)
    ]
    qs0 = {
        "title": "How Did You Hear About This Position?",
        "answers": 28,
        "likes": 78,
        "datetime": "01.01.2023 12:00",
        "tags": ["Developer", "Computer"],
        "solved": True,
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi adipiscing gravida odio, sit amet "
                "suscipit risus ultrices eu. Fusce viverra neque at purus laoreet consequat. Vivamus vulputate posuere "
                "nisl quis consequat. Donec congue commodo mi, sed commodo velit fringilla ac. Fusce placerat "
                "venenatis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis "
                "egestas. Cras ornare, dolor a aliquet rutrum, dolor turpis condimentum leo, a semper lacus purus in "
                "felis. Quisque blandit posuere turpis, eget auctor felis pharetra eu.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi adipiscing gravida odio, sit amet "
                "suscipit risus ultrices eu. Fusce viverra neque at purus laoreet consequat. Vivamus vulputate posuere "
                "nisl quis consequat. Donec congue commodo mi, sed commodo velit fringilla ac. Fusce placerat "
                "venenatis mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis "
                "egestas. Cras ornare, dolor a aliquet rutrum, dolor turpis condimentum leo, a semper lacus purus in "
                "felis. Quisque blandit posuere turpis, eget auctor felis pharetra eu.".split('\n')
    }

    obj, page_num, max_num = paginate(answers, request, per_page=30)
    return render(request, 'question.html', {"directory": "Вопрос", "page": page, "leaders": users, "tags": tags,
                                             "authorized": True, "question": qs0, "user": users[0], "answers": obj,
                                             "page_num": page_num, "max_num": max_num, "range": range(1, max_num + 1)})


def login(request):
    return render(request, 'login.html', {"title": "Вход"})


def signup(request):
    return render(request, 'signup.html', {"title": "Регистрация"})


def ask(request):
    return render(request, 'ask_question.html', {"directory": "Личный кабинет", "page": "Задать вопрос",
                                                 "leaders": users, "tags": tags, "authorized": True})


def settings(request):
    user = {
        "id": 2,
        "login": "alexf",
        "nickname": "alex_fnaf",
        "email": "alex@gmail.com"
    }
    return render(request, 'user_info.html', {"directory": "Личный кабинет", "page": "Задать вопрос", "leaders": users,
                                              "tags": tags, "authorized": True, "user": user})


def my_qs(request):
    obj, page_num, max_num = paginate(qs[:5], request)
    return render(request, 'tag.html', {"directory": "Личный кабинет", "page": "Мои вопросы", "leaders": users,
                                        "tags": tags, "authorized": True, "questions": obj, "page_num": page_num,
                                        "max_num": max_num, "range": range(1, max_num + 1)})

