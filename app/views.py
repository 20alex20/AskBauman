from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import *


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
    obj1, page_num1, max_num1 = paginate(Question.objects.sorted_by_date(), request, 'page1')
    obj2, page_num2, max_num2 = paginate(Question.objects.sorted_by_likes(), request, 'page2')
    return render(request, 'index.html', {"directory": None, "page": "Главная", "leaders": Profile.objects.leaders(),
                                          "tags": Tag.objects.popular(), "authorized": False, "questions": obj1,
                                          "questions2": obj2, "page_num1": page_num1, "max_num1": max_num1,
                                          "range1": range(1, max_num1 + 1), "page_num2": page_num2,
                                          "max_num2": max_num2, "range2": range(1, max_num2 + 1)})


def tag(request, page):
    obj, page_num, max_num = paginate(Question.objects.with_tag(page), request)
    return render(request, 'tag.html', {"directory": "Вопросы по тегам", "page": page,
                                        "leaders": Profile.objects.leaders(), "tags": Tag.objects.popular(),
                                        "authorized": True, "questions": obj, "page_num": page_num, "max_num": max_num,
                                        "range": range(1, max_num + 1)})


def question(request, page):
    qobj = Question.objects.get_question(page)
    obj, page_num, max_num = paginate(Answer.objects.of_question(qobj), request, per_page=30)
    return render(request, 'question.html', {"directory": "Вопрос", "page": page, "leaders": Profile.objects.leaders(),
                                             "tags": Tag.objects.popular(), "authorized": True, "question": qobj,
                                             "answers": obj,
                                             "page_num": page_num, "max_num": max_num, "range": range(1, max_num + 1)})


def login(request):
    return render(request, 'login.html', {"title": "Вход"})


def signup(request):
    return render(request, 'signup.html', {"title": "Регистрация"})


def ask(request):
    return render(request, 'ask_question.html', {"directory": "Личный кабинет", "page": "Задать вопрос",
                                                 "leaders": Profile.objects.leaders(), "tags": Tag.objects.popular(),
                                                 "authorized": True})


id = 10902


def settings(request):
    return render(request, 'user_info.html', {"directory": "Личный кабинет", "page": "Задать вопрос",
                                              "leaders": Profile.objects.leaders(), "tags": Tag.objects.popular(),
                                              "authorized": True, "profile": Profile.objects.filter(user_id=id)[0]})


def my_qs(request):
    obj, page_num, max_num = paginate(Question.objects.of_user(id), request)
    return render(request, 'tag.html', {"directory": "Личный кабинет", "page": "Мои вопросы",
                                        "leaders": Profile.objects.leaders(), "tags": Tag.objects.popular(),
                                        "authorized": True, "questions": obj, "page_num": page_num,
                                        "max_num": max_num, "range": range(1, max_num + 1)})


def error_page(request):
    return render(request, '404.html')
