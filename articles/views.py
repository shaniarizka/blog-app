from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout

def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    articles = Article.objects.all().order_by('-created_at')

    # SEARCH
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # FILTER CATEGORY
    if category_id:
        articles = articles.filter(
            category_id=category_id
        )

    categories = Category.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'public/home.html', {
        'articles': articles,
        'categories': categories,
    })

def detail(request, id):
    article = get_object_or_404(Article, id=id)

    return render(request, 'public/detail.html', {
        'article': article
    })

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponse('Akses ditolak')
    total = Article.objects.count()

    return render(request, 'dashboard/index.html', {
        'total': total
    })

def logout_view(request):
    logout(request)
    return redirect('/')