from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .models import Juice
from .models import drinkHot
from .models import Snack

# def index(request):
#     return HttpResponse("Привет мир!")

def homePage(request):
    title = "Main Page"
    return render(request, "index.html",  {
        'title': title
    })

def menuPage (request):
    posts = Post.objects.all().order_by('-postDate')
    juices = Juice.objects.all()
    drinks = drinkHot.objects.all()
    snacks = Snack.objects.all()
    return render(request, "menu.html", {
        'posts': posts,
        'juices': juices,
        'drinks': drinks,
        'snacks': snacks
    })
def newBurgers(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "newBurgers.html", {
        'posts': posts
    })
def newJuices(request):
    juices = Juice.objects.all()
    return render(request, "newJuices.html", {
        'juices': juices
    })
def newdrinkHot(request):
    drinks = drinkHot.objects.all()
    return render(request, "drinkHot.html", {
        'drinks': drinks
    })
def newSnack(request):
    snacks = Snack.objects.all()
    return render(request, "newSneaks.html", {
        'snacks': snacks
    })


def t_shirt (request):
    h1 = "T-Shirt"
    return render(request, "t-shirt.html",{
        't-shirt': t_shirt
    })

def pants (request):
    return render(request, "pants.html")

def cap (request):
    return render(request, "cap.html")



def newsPage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "news.html", {
        'posts': posts
    })

def adminPanels(request):
    return render(request, "adminPanels.html")