from django.shortcuts import render
from .models import Question
from django.shortcuts import redirect

def index(request):
    question_set = Question.objects.all()
    context = {"questions": question_set}
    return render(request, 'questionnarie/index.html', context)


def question_post(request):
    question = Question(
        text=request.POST.get("q_area", ""),
    )
    question.save()
    return redirect('/')


