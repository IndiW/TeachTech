from django.shortcuts import render

from .models import Question
# Create your views here.
def question_detail_view(request):
    obj = Question.objects.get(id=1)
    context = {
        'object' : obj
        }
    return render(request,"questions/detail.html",context)