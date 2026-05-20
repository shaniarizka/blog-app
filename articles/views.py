from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'public/home.html', {
        'articles': articles
    })

def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'public/detail.html', {
        'article': article
    })