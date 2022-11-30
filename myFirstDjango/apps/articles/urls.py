from django.urls import path
from . import views

urlpatterns = [
    # Создаем контреллер
    path('', views.homePage, name='homePage'),
    path('menu/', views.menuPage, name='menuPage'),
    path('newBurgers/', views.newBurgers, name='newBurgers'),
    path('newJuices/', views.newJuices, name='newJuices'),
    path('drinkHots/', views.newdrinkHot, name='drinkHot'),
    path('newSnack/', views.newSnack, name='newSnack'),

    path('t-shirt/', views.t_shirt, name='t-shirt'),
    path('pants/', views.pants,name='pants'),
    path('cap/', views.cap, name='cap'),

    path('news/', views.newsPage, name='newsPage'),
    path('admin/', views.adminPanels, name='adminPanels'),
]