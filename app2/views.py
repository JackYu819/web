from django.shortcuts import render

# Create your views here.

from .models import Article
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world, you're at the app2 index")


def year_archive(request, year):
    a_list = Article.objects.filter()
    # a_list = [1, 2, 34]
    context = {'year': year, 'a_list': a_list}
    return render(request, 'year_archive.html', context)
