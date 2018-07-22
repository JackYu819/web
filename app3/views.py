from django.shortcuts import render

# Create your views here.
from .models import Book
from django.shortcuts import render_to_response
from django.http import HttpResponse

def latest_books(request):
    book_list = Book.objects.order_by('pub_date')[:10]
    # print(book_list._fetch_all())
    context = {'book_list1':book_list, 'date_type': [i for i in range(10)]}
    return render_to_response('latest_books.html', context)


def index(request):
    return HttpResponse('欢迎你, Jackyu')


def add(request, a, b):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    return HttpResponse(str(c))
