from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

import copy


# def paginate(objects_list, request, per_page=10):
#     # do smth with Paginator, etc…
#     return page


QUESTIONS = [
    {
        'title': f"title {i}",
        'id': i,
        'text': f"text {i}"
    } for i in range(1, 31)
]

# 'id': 0, # 'questions_amount': 4
TAGS = {
    'coding':               ['Coding', 0, 4],
    'c++':                  ['C++', 1, 5],
    'work_while_sleeping':  ['Work while sleeping', 2, 3],
    'interesting_facts':    ['Interesting facts', 3, 6],
    'how_to_eat_faster':    ['How to eat faster', 4, 2],
    'python':               ['Python', 5, 7]
}


def index(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request,
        template_name="index.html",
        context={
            "questions": page.object_list,
            'page_obj': page
        }
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()

    return render(
        request,
        template_name="hot.html",
        context={
            "questions": hot_questions
        }
    )


def question(request, question_id):
    one_question = QUESTIONS[question_id - 1]
    return render(
        request,
        template_name="question.html",
        context={
            'question': one_question
        }
    )


def tag(request, tag_name):
    tag = TAGS[tag_name]
    questions_for_tag = QUESTIONS[:tag[2]]
    return render(
        request,
        template_name="tag.html",
        context={
            "questions": questions_for_tag,
            "tag": tag[0],
        }
    )
