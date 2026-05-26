from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.detail, name='detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]