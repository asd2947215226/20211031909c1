from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
<<<<<<< HEAD

# Create your views here.
=======
from .models import Articles

# FBV functions based view 基于函数的视图


def index(request):
    articles = Articles.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'index.html', context)


def detail(request,pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'single_article.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
>>>>>>> 564e3f7... 加入了页面以及完成了部分功能
>>>>>>> edfc092... 加上了页面并完成了一部分功能
