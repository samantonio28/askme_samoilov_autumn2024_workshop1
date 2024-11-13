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
            'page_obj': page,
            "tag_names": TAGS.keys()
        }
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page_num = int(request.GET.get('page', 1))

    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(
        request,
        template_name="hot.html",
        context={
            "questions": page.object_list,
            "page_obj": page, 
            "tag_names": TAGS.keys()
        }
    )


def question(request, question_id):
    if question_id not in range(1, len(QUESTIONS) + 1):
        return render(request, template_name="not_found.html")
    
    one_question = QUESTIONS[question_id - 1]
    return render(
        request,
        template_name="question.html",
        context={
            'question': one_question, 
            "tag_names": TAGS.keys()   
        }
    )

def not_found(request):
    return render(
        request,
        "not_found.html"
    )

def tag(request, tag_name):
    if tag_name not in TAGS:
        return render(request, template_name="not_found.html")
        
    tag = TAGS[tag_name]
    questions_for_tag = QUESTIONS[:tag[2]]
    return render(
        request,
        template_name="tag.html",
        context={
            "questions": questions_for_tag,
            "tag": tag[0],
            "tag_names": TAGS.keys(),
        }
    )
