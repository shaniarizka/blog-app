from django.shortcuts import render, get_object_or_404
from .models import Article
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q')

    # 🔎 Search
    if query:
        article_list = Article.objects.filter(
            Q(title__icontains=query)
        )
    else:
        article_list = Article.objects.all()

    # 📄 Pagination
    paginator = Paginator(article_list, 5)  # 5 artikel per halaman
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'public/home.html', {
        'articles': articles,
        'query': query
    })


def detail(request, id):
    article = get_object_or_404(Article, id=id)

    return render(request, 'public/detail.html', {
        'article': article
    })

@login_required
def dashboard(request):
    total = Article.objects.count()
    return render(request, 'dashboard/index.html', {
        'total': total
    })