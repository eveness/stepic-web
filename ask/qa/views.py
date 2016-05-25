from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib.auth.models import User
from models import Question
from models import Answer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator


@require_GET
def index(request, *args, **kwargs):

    try:
        page = int(request.GET.get("page"))
    except (ValueError, TypeError):
        page = 1

    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(
        request, 'list.html',
        {'title': 'Lastest question', 'paginator': paginator,
         'questions': page.object_list, 'page': page,
         'user': request.user, 'session': request.session})


@require_GET
def popular(request, *args, **kwargs):

    try:
        page = int(request.GET.get("page"))
    except (ValueError, TypeError):
        page = 1

    questions = Question.objects.popular()

    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(
        request, 'list.html',
        {'title': 'Popular question', 'paginator': paginator,
         'questions': page.object_list, 'page': page,
         'user': request.user, 'session': request.session})


def question(request, pk_question):
    gs = get_object_or_404(Question, id=pk_question)
    answers = gs.answer_set.all()

    return render(
        request, 'question.html',
        {'question': gs, 'answers': answers,
         'user': request.user, 'session': request.session})


def question_detail(request, pk_question):
    qs = get_object_or_404(Question, id=pk_question)
    answers = qs.answer_set.all()
    return render(request, 'question.html', {
        'question': qs, 'answers': answers,
        'user': request.user, 'session': request.session
    })